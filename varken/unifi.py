from logging import getLogger
from requests import Session, Request
from datetime import datetime, timezone

#from varken.helpers import connection_handler


class UniFiAPI(object):
    def __init__(self, server, dbmanager):
        self.dbmanager = dbmanager
        self.server = server
        self.username = server.username
        self.password = server.password
        self.baseurl = server.url
        self.site = server.site if server.site else 'default'
        self.session = Session()
        self.logger = getLogger()

    def login(self):
        endpoint = '/api/auth/login'
        data = {'username': self.username, 'password': self.password}
        headers = {'Content-Type': 'application/json'}
        url = self.baseurl + endpoint
        response = self.session.post(url, json=data, headers=headers, verify=False)
        
        if response.status_code == 200:
            self.logger.debug("UniFi login successful")
            return True
        else:
            self.logger.error("Login failed")
            return False

    def logout(self):
        endpoint = '/api/auth/logout'
        self.session.get(self.baseurl + endpoint, verify=False)
        self.logger.debug("UniFi logout successful")

    def get_usg_stats(self):
        if not self.login():
            return
        
        now = datetime.now(timezone.utc).astimezone().isoformat()
        endpoint = f'/proxy/network/api/s/{self.site}/stat/device'
        headers = {'Content-Type': 'application/json'}
        data = {}
        url = self.baseurl + endpoint
        self.logger.debug("UniFi URL Endpoint: %s", url)
        
        response = self.session.get(url, json=data, headers=headers, verify=False)

        #self.logger.debug("Response: %s", response.text)
        
        if response.status_code != 200:
            self.logger.error("Failed to get USG stats")
            self.logout()
            return
        
        data = response.json()
        
        #self.logger.debug("Data: %s", data)
        devices = {device['name']: device for device in data['data'] if device.get('name')}
        
        if self.server.usg_name not in devices:
            self.logger.error("Could not find a USG named %s from your UniFi Controller", self.server.usg_name)
            self.logout()
            return
        
        device = devices[self.server.usg_name]

        try:
            influx_payload = [
                {
                    "measurement": "UniFi",
                    "tags": {
                        "site": self.site,
                        "device": device['name'],
                        "type": "USG"
                    },
                    "time": now,
                    "fields": {
                        "bytes_current": device['wan1']['bytes-r'],
                        "rx_bytes_total": device['wan1']['rx_bytes'],
                        "rx_bytes_current": device['wan1']['rx_bytes-r'],
                        "tx_bytes_total": device['wan1']['tx_bytes'],
                        "tx_bytes_current": device['wan1']['tx_bytes-r'],
                        "cpu_loadavg_1": float(device['sys_stats']['loadavg_1']),
                        "cpu_loadavg_5": float(device['sys_stats']['loadavg_5']),
                        "cpu_loadavg_15": float(device['sys_stats']['loadavg_15']),
                        "cpu_util": float(device['system-stats']['cpu']),
                        "mem_util": float(device['system-stats']['mem']),
                    }
                }
            ]
            self.dbmanager.write_points(influx_payload)
        except KeyError as e:
            self.logger.error('Error building paylod for unifi. Discarding. Error: %s', e)
            
        self.logout()