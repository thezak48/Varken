from sys import version_info
from typing import NamedTuple
from logging import getLogger

logger = getLogger('temp')
# Check for python3.6 or newer to resolve erroneous typing.NamedTuple issues
if version_info < (3, 6, 2):
    logger.error('Varken requires python3.6.2 or newer. You are on python%s.%s.%s - Exiting...',
                version_info.major, version_info.minor, version_info.micro)
    exit(1)


# Server Structures
class InfluxServer(NamedTuple):
    password: str = 'root'
    port: int = 8086
    ssl: bool = False
    url: str = 'localhost'
    username: str = 'root'
    verify_ssl: bool = False


class SonarrServer(NamedTuple):
    api_key: str = None
    future_days: int = 0
    future_days_run_seconds: int = 30
    id: int = None
    missing_days: int = 0
    missing_days_run_seconds: int = 30
    queue: bool = False
    queue_run_seconds: int = 30
    url: str = None
    verify_ssl: bool = False


class RadarrServer(NamedTuple):
    api_key: str = None
    get_missing: bool = False
    get_missing_run_seconds: int = 30
    id: int = None
    queue: bool = False
    queue_run_seconds: int = 30
    url: str = None
    verify_ssl: bool = False

#TODO - Lidarr support
#class LidarrServer(NamedTuple):
#    api_key: str = None
#    id: int = None
#    queue: bool = False
#    queue_run_seconds: int = 30
#    url: str = None
#    verify_ssl: bool = False

class OmbiServer(NamedTuple):
    api_key: str = None
    id: int = None
    issue_status_counts: bool = False
    issue_status_run_seconds: int = 30
    request_total_counts: bool = False
    request_total_run_seconds: int = 30
    request_type_counts: bool = False
    request_type_run_seconds: int = 30
    url: str = None
    verify_ssl: bool = False


class OverseerrServer(NamedTuple):
    api_key: str = None
    id: int = None
    url: str = None
    verify_ssl: bool = False
    get_request_total_counts: bool = False
    request_total_run_seconds: int = 30
    num_latest_requests_to_fetch: int = 10
    num_latest_requests_seconds: int = 30
    num_total_issue_counts: int = 300


class TautulliServer(NamedTuple):
    api_key: str = None
    fallback_ip: str = None
    get_activity: bool = False
    get_activity_run_seconds: int = 30
    get_stats: bool = False
    get_stats_run_seconds: int = 30
    id: int = None
    url: str = None
    verify_ssl: bool = None
    maxmind_license_key: str = None


class UniFiServer(NamedTuple):
    get_usg_stats_run_seconds: int = 30
    id: int = None
    password: str = 'ubnt'
    site: str = None
    url: str = 'unifi.domain.tld:8443'
    username: str = 'ubnt'
    usg_name: str = None
    verify_ssl: bool = False


# Shared
class QueuePages(NamedTuple):
    page: int = None
    pageSize: int = None
    sortKey: str = None
    sortDirection: str = None
    totalRecords: str = None
    records: list = None


# Ombi /api/v1/Request/count
class OmbiRequestCounts(NamedTuple):
    approved: int = 0
    available: int = 0
    pending: int = 0

# Ombi /api/v1/Issues/count
class OmbiIssuesCounts(NamedTuple):
    inProgress: int = 0
    pending: int = 0
    resolved: int = 0

# Ombi /api/v1/rRequest/tv
class OmbiTVRequest(NamedTuple):
    background: str = None
    childRequests: list = None
    denied: bool = None # Not listed in Ombi API reference
    deniedReason: None = None # Not listed in Ombi API reference
    externalProviderId: str = None
    id: int = None
    imdbId: str = None
    languageProfile: str = None
    markedAsDenied: str = None # Not listed in Ombi API reference
    overview: str = None
    posterPath: str = None
    qualityOverride: None = None
    releaseDate: str = None
    rootFolder: None = None
    status: str = None
    title: str = None
    totalSeasons: int = None
    tvDbId: int = None
    requestedByAlias: str = None # Not listed in Ombi API reference
    requestStatus: str = None

# Ombi /api/v1/Request/movie
class OmbiMovieRequest(NamedTuple):
    approved: bool = None
    approved4K: bool = None
    available: bool = None
    available4K: bool = None
    background: str = None
    canApprove: bool = None
    denied: bool = None
    denied4K: None = None
    deniedReason: None = None
    deniedReason4K: None = None
    digitalRelease: bool = None
    digitalReleaseDate: None = None
    has4KRequest: bool = None
    id: int = None
    imdbId: str = None
    is4kRequest: bool = None
    issueId: None = None
    issues: None = None
    langCode: str = None
    # languageCode: str = None # Not listed in Ombi API reference
    markedAsApproved: str = None
    markedAsApproved4K: str = None
    markedAsAvailable: None = None
    markedAsAvailable4K: None = None
    markedAsDenied: str = None
    markedAsDenied4K: str = None
    overview: str = None
    playedByUsersCount: int = None # May or may not work
    posterPath: str = None
    qualityOverride: int = None
    released: bool = None
    releaseDate: str = None
    requestedByAlias: str = None
    requestedDate: str = None
    requestedDate4k: str = None
    requestedUser: dict = None
    requestedUserId: str = None
    requestStatus: str = None
    requestType: int = None
    rootPathOverride: int = None
    showSubscribe: bool = None
    source: int = None
    status: str = None
    subscribed: bool = None
    theMovieDbId: int = None
    title: str = None
    watchedByRequestedUser: bool = None # May or may not work

# Overseerr /api/v1/request/count
class OverseerrRequestCounts(NamedTuple):
    approved: int = None
    available: int = None
    declined: int = None
    movie: int = None
    pending: int = None
    processing: int = None
    total: int = None
    tv: int = None

# Overseerr /api/v1/issue/count
class OverseerrIssuesCounts(NamedTuple):
    audio: int = 0
    closed: int = 0
    open: int = 0
    others: int = 0
    subtitles: int = 0
    total: int = 0
    video: int = 0

# Sonarr /api/v3/series
class SonarrTVShow(NamedTuple):
    added: str = None
    addOptions = dict = None # May or may not work
    airTime: str = None
    alternateTitles: list = None
    certification: str = None
    cleanTitle: str = None
    ended: bool = None
    episodesChanged: bool = None # May or may not work
    firstAired: str = None
    folder: str = None # May or may not work
    genres: list = None
    id: int = None
    images: list = None
    imdbId: str = None
    languageProfileId: int = None # Deprecated, varken still expects this value
    lastAired: str = None # May or may not work
    monitored: bool = None
    monitorNewItems: str = None # May or may not work
    nextAiring: str = None
    network: str = None
    originalLanguage: str = None
    overview: str = None
    path: str = None
    previousAiring: str = None
    profileName: str = None
    qualityProfileId: int = None
    ratings: dict = None
    remotePoster: str = None # May or may not work
    rootFolderPath: str = None
    runtime: int = None
    seasonFolder: bool = None
    seasons: list = None
    seriesType: str = None
    sortTitle: str = None
    statistics: dict = None
    status: str = None
    tags: list = None
    title: str = None
    titleSlug: str = None
    tvdbId: int = None
    tvMazeId: int = None
    tvRageId: int = None
    useSceneNumbering: bool = None
    year: int = None

# Sonarr Episode /api/v3/episode
class SonarrEpisode(NamedTuple):
    absoluteEpisodeNumber: int = None
    airDate: str = None
    airDateUtc: str = None
    endTime: str = None # May or may not work
    episodeFile: dict = None # Might work as dict
    episodeFileId: int = None
    episodeNumber: int = None
    finaleType: str = None # May or may not work
    grabDate: str = None # May or may not work
    grabbed: bool = None
    hasFile: bool = None
    id: int = None
    images: list = None
    monitored: bool = None
    overview: str = None
    runtime: int = None
    sceneAbsoluteEpisodeNumber: int = None
    sceneEpisodeNumber: int = None
    sceneSeasonNumber: int = None
    seasonNumber: int = None
    series: SonarrTVShow = None
    seriesId: int = None
    seriesTitle: str = None
    title: str = None
    tvdbId: int = None
    unverifiedSceneNumbering: bool = None

# Sonarr /api/v3/queue
class SonarrQueue(NamedTuple):
    customFormats: list = None
    customFormatScore: int = None
    downloadClient: str = None
    downloadId: str = None
    episode: SonarrEpisode = None
    episodeHasFile: bool = None
    episodeId: int = None
    errorMessage: str = None
    estimatedCompletionTime: str = None
    id: int = None
    indexer: str = None
    languages: list = None
    outputPath: str = None
    protocol: str = None
    quality: dict = None
    seasonNumber: int = None
    series: SonarrTVShow = None
    seriesId: int = None
    size: float = None
    sizeleft: float = None
    status: str = None
    statusMessages: list = None
    timeleft: str = None
    title: str = None
    trackedDownloadState: str = None
    trackedDownloadStatus: str = None

# Radarr /api/v3/movie
class RadarrMovie(NamedTuple):
    added: str = None
    addOptions: str = None
    alternateTitles: list = None
    certification: str = None
    cleanTitle: str = None
    collection: dict = None
    digitalRelease: str = None
    folder: str = None # May or may not work
    folderName: str = None
    genres: list = None
    hasFile: bool = None
    id: int = None
    images: list = None
    imdbId: str = None
    inCinemas: str = None
    isAvailable: bool = None
    minimumAvailability: str = None
    monitored: bool = None
    movieFile: dict = None
    originalLanguage: str = None
    originalTitle: str = None
    overview: str = None
    path: str = None
    popularity: str = None
    physicalRelease: str = None
    physicalReleaseNote: str = None # May or may not work
    qualityProfileId: int = None
    ratings: dict = None
    remotePoster: str = None # May or may not work
    rootFolderPath: str = None
    runtime: int = None
    secondaryYear: int = None
    secondaryYearSourceId: int = None
    sizeOnDisk: float = None
    sortTitle: str = None
    # statistics: dict = None # Deprecated, may or may not work while disabled
    status: str = None
    studio: str = None
    tags: list = None
    title: str = None
    titleSlug: str = None
    tmdbId: int = None
    website: str = None
    year: int = None
    youTubeTrailerId: str = None

# Radarr Queue Details /api/v3/queue
class RadarrQueue(NamedTuple):
    customFormats: list = None
    customFormatScore: int = None # May or May not work
    downloadClient: str = None
    downloadId: str = None
    errorMessage: str = None
    estimatedCompletionTime: str = None
    id: int = None
    indexer: str = None
    languages: list = None
    movie: RadarrMovie = None
    movieId: int = None
    outputPath: str = None
    protocol: str = None
    quality: dict = None
    size: float = None
    sizeleft: float = None
    status: str = None
    statusMessages: list = None
    timeleft: str = None
    title: str = None
    trackedDownloadState: str = None
    trackedDownloadStatus: str = None

# Tautulli
class TautulliStream(NamedTuple):
    # get_activity
    actors: list = None
    added_at: str = None
    allow_guest: int = None
    art: str = None
    aspect_ratio: str = None
    audience_rating: str = None
    audience_rating_image: str = None
    audio_bitrate: str = None
    audio_bitrate_mode: str = None
    audio_channel_layout: str = None
    audio_channels: str = None
    audio_codec: str = None
    audio_decision: str = None
    audio_language: str = None
    audio_language_code: str = None
    audio_profile: str = None
    audio_sample_rate: str = None
    bandwidth: str = None
    banner: str = None
    bif_thumb: str = None
    bitrate: str = None
    channel_call_sign: str = None # May or may not work
    channel_identifier: str = None # May or may not work
    #channel_icon: str = None # Not listed in Tautulli API reference
    channel_stream: int = None
    channel_thumb: str = None
    # channel_title: str = None # Not listed in Tautulli API reference
    children_count: str = None
    collections: list = None
    container: str = None
    container_decision: str = None # May or may not work
    content_rating: str = None
    # current_session: str = None # Not listed in Tautulli API reference
    # date: str = None # Not listed in Tautulli API reference
    deleted_user: int = None
    device: str = None
    directors: list = None
    do_notify: int = None
    duration: str = None
    email: str = None
    # extra_type: str = None # Not listed in Tautulli API reference
    file: str = None
    file_size: str = None
    friendly_name: str = None
    full_title: str = None
    genres: list = None
    grandparent_guid: str = None
    grandparent_rating_key: str = None
    grandparent_thumb: str = None
    grandparent_title: str = None
    # group_count: int = None # Not listed in Tautulli API reference
    # group_ids: str = None # Not listed in Tautulli API reference
    guid: str = None
    height: str = None
    id: str = None
    indexes: int = None
    ip_address: str = None
    ip_address_public: str = None
    is_admin: int = None
    is_allow_sync: int = None
    is_home_user: int = None
    is_restricted: int = None
    keep_history: int = None
    labels: list = None
    last_viewed_at: str = None
    library_name: str = None
    live: int = None
    live_uuid: str = None
    local: str = None
    location: str = None
    machine_id: str = None
    media_index: str = None
    media_type: str = None
    optimized_version: int = None
    optimized_version_profile: str = None
    optimized_version_title: str = None
    original_title: str = None
    originally_available_at: str = None
    parent_guid: str = None
    parent_media_index: str = None
    parent_rating_key: str = None
    parent_thumb: str = None
    parent_title: str = None
    # paused_counter: int = None # Not listed in Tautulli API reference
    # percent_complete: int = None # Not listed in Tautulli API reference
    platform: str = None
    platform_name: str = None
    platform_version: str = None
    player: str = None
    # pre_tautulli: str = None # Not listed in Tautulli API reference
    product: str = None
    product_version: str = None
    profile: str = None
    progress_percent: str = None
    quality_profile: str = None
    rating: str = None
    rating_image: str = None
    rating_key: str = None
    # reference_id: int = None # Not listed in Tautulli API reference
    relay: int = None
    # relayed: int = None # Not listed in Tautulli API reference
    # row_id: int = None # Not listed in Tautulli API reference
    section_id: str = None
    secure: str = None
    # selected: int = None # Not listed in Tautulli API reference
    session_id: str = None
    session_key: str = None
    shared_libraries: list = None
    sort_title: str = None
    # started: int = None # Not listed in Tautulli API reference
    state: str = None
    # stopped: int = None # Not listed in Tautulli API reference
    stream_aspect_ratio: str = None
    stream_audio_bitrate: str = None
    stream_audio_bitrate_mode: str = None
    stream_audio_channel_layout: str = None
    stream_audio_channel_layout_: str = None
    stream_audio_channels: str = None
    stream_audio_codec: str = None
    stream_audio_decision: str = None
    stream_audio_language: str = None
    stream_audio_language_code: str = None
    stream_audio_sample_rate: str = None
    stream_bitrate: str = None
    stream_container: str = None
    stream_container_decision: str = None
    stream_duration: str = None
    stream_subtitle_codec: str = None
    stream_subtitle_container: str = None
    stream_subtitle_decision: str = None
    stream_subtitle_forced: int = None
    stream_subtitle_format: str = None
    stream_subtitle_language: str = None
    stream_subtitle_language_code: str = None
    stream_subtitle_location: str = None
    stream_video_bit_depth: str = None
    stream_video_bitrate: str = None
    stream_video_chroma_subsampling: str = None # May or may not work
    stream_video_codec: str = None
    stream_video_codec_level: str = None
    stream_video_color_primaries: str = None # May or may not work
    stream_video_color_range: str = None # May or may not work
    stream_video_color_space: str = None # May or may not work
    stream_video_color_trc: str = None # May or may not work
    stream_video_decision: str = None
    stream_video_dynamic_range: str = None
    stream_video_framerate: str = None
    stream_video_full_resolution: str = None
    stream_video_height: str = None
    stream_video_language: str = None
    stream_video_language_code: str = None
    stream_video_ref_frames: str = None
    stream_video_resolution: str = None
    stream_video_scan_type: str = None
    stream_video_width: str = None
    studio: str = None
    # sub_type: str = None # Not listed in Tautulli API reference
    subtitle_codec: str = None
    subtitle_container: str = None
    subtitle_decision: str = None
    subtitle_forced: int = None
    subtitle_format: str = None
    subtitle_language: str = None
    subtitle_language_code: str = None
    subtitle_location: str = None
    subtitles: int = None
    summary: str = None
    synced_version: int = None
    synced_version_profile: str = None
    tagline: str = None
    throttled: str = None
    thumb: str = None
    title: str = None
    transcode_audio_channels: str = None
    transcode_audio_codec: str = None
    transcode_container: str = None
    transcode_decision: str = None
    transcode_height: str = None
    transcode_hw_decode: str = None
    transcode_hw_decode_title: str = None
    transcode_hw_decoding: int = None
    transcode_hw_encode: str = None
    transcode_hw_encode_title: str = None
    transcode_hw_encoding: int = None
    transcode_hw_full_pipeline: int = None
    transcode_hw_requested: int = None
    transcode_key: str = None
    transcode_progress: int = None
    transcode_protocol: str = None
    transcode_speed: str = None
    transcode_throttled: int = None
    transcode_video_codec: str = None
    transcode_width: str = None
    type: str = None
    updated_at: str = None
    user: str = None
    user_id: int = None
    user_rating: str = None
    user_thumb: str = None
    username: str = None
    video_bit_depth: str = None
    video_bitrate: str = None
    video_chroma_subsampling: str = None # May or may not work
    video_codec: str = None
    video_codec_level: str = None
    video_color_primaries: str = None # May or may not work
    video_color_range: str = None # May or may not work
    video_color_space: str = None # May or may not work
    video_color_trc: str = None # May or may not work
    video_decision: str = None
    video_dynamic_range: str = None
    video_frame_rate: str = None
    video_framerate: str = None
    video_full_resolution: str = None
    video_height: str = None
    video_language: str = None
    video_language_code: str = None
    video_profile: str = None
    video_ref_frames: str = None
    video_resolution: str = None
    video_scan_type: str = None
    video_width: str = None
    view_offset: str = None
    # watched_status: int = None # Not listed in Tautulli API reference
    width: str = None
    writers: list = None
    year: str = None

# Lidarr /api/v1/album
class LidarrAlbum(NamedTuple):
    addOptions: dict = None
    albumType: str = None
    anyReleaseOk: bool = None
    artist: dict = None
    # artist: LidarrArtist = None | #TODO - Lidarr support
    artistId: int = None
    disambiguation: str = None
    duration: int = None
    foreignAlbumId: str = None
    genres: list = None
    grabbed: bool = None
    id: int = None
    images: list = None
    links: list = None
    media: list = None
    mediumCount: int = None
    monitored: bool = None
    overview: str = None
    profileId: int = None
    ratings: dict = None
    releases: list = None
    releaseDate: str = None
    remoteCover: str = None
    secondaryTypes: list = None
    statistics: dict = {}
    title: str = None
    
#TODO - Lidarr support
# Lidarr /api/v1/artist
#class LidarrArtist(NamedTuple):
#    added: str = None
#    addOptions: dict = None
#    allMusicId: str = None
#    artistMetadataId: int = None
#    artistName: str = None
#    artistType: str = None
#    cleanName: str = None
#    disambiguation: str = None
#    discogsId: int = None
#    ended: bool = None
#    folder: str = None
#    foreignArtistId: str = None
#    genres: list = None
#    id: int = None
#    images: list = None
#    lastAlbum: LidarrAlbum = None
#    links: list = None
#    mbId: str = None
#    members: list = None
#    metadataProfileId: int = None
#    monitored: bool = None
#    monitorNewItems: str = None
#    nextAlbum: LidarrAlbum = None
#    overview: str = None
#    path: str = None
#    qualityProfileId: int = None
#    ratings: dict = None
#    remotePoster: str = None
#    rootFolderPath: str = None
#    sortName: str = None
#    statistics: dict = None
#    status: str = None
#    tadbId: int = None
#    tags: list = None

# Lidarr /api/v1/queue
class LidarrQueue(NamedTuple):
    album: LidarrAlbum = None
    albumId: int = None
    artist: dict = None
    #artist: LidarrArtist = None | #TODO - Lidarr support
    artistId: int = None
    customFormats: list = None
    customFormatScore: int = None
    downloadClient: str = None
    downloadForced: bool = None
    downloadId: str = None
    errorMessage: str = None
    estimatedCompletionTime: str = None
    id: int = None
    indexer: str = None
    # language: dict = None # Not defined in the /api/v1/queue endpoint reference.
    outputPath: str = None
    protocol: str = None
    quality: dict = None
    size: float = None
    status: str = None
    statusMessages: list = None
    sizeleft: float = None
    timeleft: str = None
    title: str = None
    trackedDownloadState: str = None
    trackedDownloadStatus: str = None

