#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
#

"""
This python module provides...

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.conf import settings
from vimeo import VimeoClient as VimeoClientBase
from django.contrib.sites.models import Site
from typing import Optional, List, Any
from django.utils.translation import gettext as _
from django.db import models
from enum import Enum
from vimeo import VimeoClient
from datetime import datetime
import uuid

class CPSSAppType:
    name: Optional[str]
    uri: Optional[str]

    def __init__(self, name: Optional[str], uri: Optional[str]) -> None:
        self.name = name
        self.uri = uri


class CPSSTypeEnum(Enum):
    SOURCE = "source"
    VIDEO_MP4 = "video/mp4"


class CPSSDownloadType:
    quality: Optional[str]
    type: Optional[CPSSTypeEnum]
    width: Optional[int]
    height: Optional[int]
    expires: Optional[datetime]
    link: Optional[str]
    created_time: Optional[datetime]
    fps: Optional[float]
    size: Optional[int]
    md5: Optional[str]

    def __init__(self, quality: Optional[str], type: Optional[CPSSTypeEnum], width: Optional[int], height: Optional[int], expires: Optional[datetime], link: Optional[str], created_time: Optional[datetime], fps: Optional[float], size: Optional[int], md5: Optional[str]) -> None:
        self.quality = quality
        self.type = type
        self.width = width
        self.height = height
        self.expires = expires
        self.link = link
        self.created_time = created_time
        self.fps = fps
        self.size = size
        self.md5 = md5


class CPSSLiveType:
    streaming: Optional[bool]
    archived: Optional[bool]

    def __init__(self, streaming: Optional[bool], archived: Optional[bool]) -> None:
        self.streaming = streaming
        self.archived = archived


class CPSSStaffPickType:
    normal: Optional[bool]
    best_of_the_month: Optional[bool]
    best_of_the_year: Optional[bool]
    premiere: Optional[bool]

    def __init__(self, normal: Optional[bool], best_of_the_month: Optional[bool], best_of_the_year: Optional[bool], premiere: Optional[bool]) -> None:
        self.normal = normal
        self.best_of_the_month = best_of_the_month
        self.best_of_the_year = best_of_the_year
        self.premiere = premiere


class CPSSBadgesType:
    hdr: Optional[bool]
    live: Optional[CPSSLiveType]
    staff_pick: Optional[CPSSStaffPickType]
    vod: Optional[bool]
    weekend_challenge: Optional[bool]

    def __init__(self, hdr: Optional[bool], live: Optional[CPSSLiveType], staff_pick: Optional[CPSSStaffPickType], vod: Optional[bool], weekend_challenge: Optional[bool]) -> None:
        self.hdr = hdr
        self.live = live
        self.staff_pick = staff_pick
        self.vod = vod
        self.weekend_challenge = weekend_challenge


class CPSSButtonsType:
    like: Optional[bool]
    watchlater: Optional[bool]
    share: Optional[bool]
    embed: Optional[bool]
    hd: Optional[bool]
    fullscreen: Optional[bool]
    scaling: Optional[bool]

    def __init__(self, like: Optional[bool], watchlater: Optional[bool], share: Optional[bool], embed: Optional[bool], hd: Optional[bool], fullscreen: Optional[bool], scaling: Optional[bool]) -> None:
        self.like = like
        self.watchlater = watchlater
        self.share = share
        self.embed = embed
        self.hd = hd
        self.fullscreen = fullscreen
        self.scaling = scaling


class CPSSCustomType:
    active: Optional[bool]
    link: None
    sticky: Optional[bool]

    def __init__(self, active: Optional[bool], link: None, sticky: Optional[bool]) -> None:
        self.active = active
        self.link = link
        self.sticky = sticky


class CPSSLogosType:
    vimeo: Optional[bool]
    custom: Optional[CPSSCustomType]

    def __init__(self, vimeo: Optional[bool], custom: Optional[CPSSCustomType]) -> None:
        self.vimeo = vimeo
        self.custom = custom


class CPSSTitleType:
    name: Optional[str]
    owner: Optional[str]
    portrait: Optional[str]

    def __init__(self, name: Optional[str], owner: Optional[str], portrait: Optional[str]) -> None:
        self.name = name
        self.owner = owner
        self.portrait = portrait


class CPSSEmbedType:
    buttons: Optional[CPSSButtonsType]
    logos: Optional[CPSSLogosType]
    title: Optional[CPSSTitleType]
    playbar: Optional[bool]
    volume: Optional[bool]
    speed: Optional[bool]
    color: Optional[str]
    uri: None
    html: Optional[str]
    badges: Optional[CPSSBadgesType]

    def __init__(self, buttons: Optional[CPSSButtonsType], logos: Optional[CPSSLogosType], title: Optional[CPSSTitleType], playbar: Optional[bool], volume: Optional[bool], speed: Optional[bool], color: Optional[str], uri: None, html: Optional[str], badges: Optional[CPSSBadgesType]) -> None:
        self.buttons = buttons
        self.logos = logos
        self.title = title
        self.playbar = playbar
        self.volume = volume
        self.speed = speed
        self.color = color
        self.uri = uri
        self.html = html
        self.badges = badges


class CPSSOptionType(Enum):
    DELETE = "DELETE"
    GET = "GET"
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"


class CPSSBasseTerreElephantType:
    uri: Optional[str]
    options: Optional[List[CPSSOptionType]]
    total: Optional[int]

    def __init__(self, uri: Optional[str], options: Optional[List[CPSSOptionType]], total: Optional[int]) -> None:
        self.uri = uri
        self.options = options
        self.total = total


class CPSSRelatedType:
    uri: Optional[str]
    options: Optional[List[CPSSOptionType]]

    def __init__(self, uri: Optional[str], options: Optional[List[CPSSOptionType]]) -> None:
        self.uri = uri
        self.options = options


class CPSSVersionsType:
    uri: Optional[str]
    options: Optional[List[CPSSOptionType]]
    total: Optional[int]
    current_uri: Optional[str]
    resource_key: Optional[str]

    def __init__(self, uri: Optional[str], options: Optional[List[CPSSOptionType]], total: Optional[int], current_uri: Optional[str], resource_key: Optional[str]) -> None:
        self.uri = uri
        self.options = options
        self.total = total
        self.current_uri = current_uri
        self.resource_key = resource_key


class CPSSPurpleConnectionsType:
    comments: Optional[CPSSBasseTerreElephantType]
    credits: None
    likes: Optional[CPSSBasseTerreElephantType]
    pictures: Optional[CPSSBasseTerreElephantType]
    texttracks: Optional[CPSSBasseTerreElephantType]
    related: Optional[CPSSRelatedType]
    recommendations: None
    albums: Optional[CPSSBasseTerreElephantType]
    available_albums: Optional[CPSSBasseTerreElephantType]
    versions: Optional[CPSSVersionsType]

    def __init__(self, comments: Optional[CPSSBasseTerreElephantType], credits: None, likes: Optional[CPSSBasseTerreElephantType], pictures: Optional[CPSSBasseTerreElephantType], texttracks: Optional[CPSSBasseTerreElephantType], related: Optional[CPSSRelatedType], recommendations: None, albums: Optional[CPSSBasseTerreElephantType], available_albums: Optional[CPSSBasseTerreElephantType], versions: Optional[CPSSVersionsType]) -> None:
        self.comments = comments
        self.credits = credits
        self.likes = likes
        self.pictures = pictures
        self.texttracks = texttracks
        self.related = related
        self.recommendations = recommendations
        self.albums = albums
        self.available_albums = available_albums
        self.versions = versions


class CPSSReportType:
    uri: Optional[str]
    options: Optional[List[CPSSOptionType]]
    reason: Optional[List[str]]

    def __init__(self, uri: Optional[str], options: Optional[List[CPSSOptionType]], reason: Optional[List[str]]) -> None:
        self.uri = uri
        self.options = options
        self.reason = reason


class CPSSWatchlaterType:
    uri: Optional[str]
    options: Optional[List[CPSSOptionType]]
    added: Optional[bool]
    added_time: None

    def __init__(self, uri: Optional[str], options: Optional[List[CPSSOptionType]], added: Optional[bool], added_time: None) -> None:
        self.uri = uri
        self.options = options
        self.added = added
        self.added_time = added_time


class CPSSInteractionsType:
    watchlater: Optional[CPSSWatchlaterType]
    report: Optional[CPSSReportType]

    def __init__(self, watchlater: Optional[CPSSWatchlaterType], report: Optional[CPSSReportType]) -> None:
        self.watchlater = watchlater
        self.report = report


class CPSSDatumMetadataType:
    connections: Optional[CPSSPurpleConnectionsType]
    interactions: Optional[CPSSInteractionsType]

    def __init__(self, connections: Optional[CPSSPurpleConnectionsType], interactions: Optional[CPSSInteractionsType]) -> None:
        self.connections = connections
        self.interactions = interactions


class CPSSFluffyConnectionsType:
    items: Optional[CPSSBasseTerreElephantType]
    videos: Optional[CPSSBasseTerreElephantType]
    folders: Optional[CPSSBasseTerreElephantType]

    def __init__(self, items: Optional[CPSSBasseTerreElephantType], videos: Optional[CPSSBasseTerreElephantType], folders: Optional[CPSSBasseTerreElephantType]) -> None:
        self.items = items
        self.videos = videos
        self.folders = folders


class CPSSParentFolderMetadataType:
    connections: Optional[CPSSFluffyConnectionsType]

    def __init__(self, connections: Optional[CPSSFluffyConnectionsType]) -> None:
        self.connections = connections


class CPSSParentFolderPrivacyType:
    view: Optional[str]

    def __init__(self, view: Optional[str]) -> None:
        self.view = view


class CPSSTentacledConnectionsType:
    albums: Optional[CPSSBasseTerreElephantType]
    appearances: Optional[CPSSBasseTerreElephantType]
    categories: Optional[CPSSBasseTerreElephantType]
    channels: Optional[CPSSBasseTerreElephantType]
    feed: Optional[CPSSRelatedType]
    followers: Optional[CPSSBasseTerreElephantType]
    following: Optional[CPSSBasseTerreElephantType]
    groups: Optional[CPSSBasseTerreElephantType]
    likes: Optional[CPSSBasseTerreElephantType]
    membership: Optional[CPSSRelatedType]
    moderated_channels: Optional[CPSSBasseTerreElephantType]
    portfolios: Optional[CPSSBasseTerreElephantType]
    videos: Optional[CPSSBasseTerreElephantType]
    watchlater: Optional[CPSSBasseTerreElephantType]
    shared: Optional[CPSSBasseTerreElephantType]
    pictures: Optional[CPSSBasseTerreElephantType]
    watched_videos: Optional[CPSSBasseTerreElephantType]
    folders: Optional[CPSSBasseTerreElephantType]
    block: Optional[CPSSBasseTerreElephantType]

    def __init__(self, albums: Optional[CPSSBasseTerreElephantType], appearances: Optional[CPSSBasseTerreElephantType], categories: Optional[CPSSBasseTerreElephantType], channels: Optional[CPSSBasseTerreElephantType], feed: Optional[CPSSRelatedType], followers: Optional[CPSSBasseTerreElephantType], following: Optional[CPSSBasseTerreElephantType], groups: Optional[CPSSBasseTerreElephantType], likes: Optional[CPSSBasseTerreElephantType], membership: Optional[CPSSRelatedType], moderated_channels: Optional[CPSSBasseTerreElephantType], portfolios: Optional[CPSSBasseTerreElephantType], videos: Optional[CPSSBasseTerreElephantType], watchlater: Optional[CPSSBasseTerreElephantType], shared: Optional[CPSSBasseTerreElephantType], pictures: Optional[CPSSBasseTerreElephantType], watched_videos: Optional[CPSSBasseTerreElephantType], folders: Optional[CPSSBasseTerreElephantType], block: Optional[CPSSBasseTerreElephantType]) -> None:
        self.albums = albums
        self.appearances = appearances
        self.categories = categories
        self.channels = channels
        self.feed = feed
        self.followers = followers
        self.following = following
        self.groups = groups
        self.likes = likes
        self.membership = membership
        self.moderated_channels = moderated_channels
        self.portfolios = portfolios
        self.videos = videos
        self.watchlater = watchlater
        self.shared = shared
        self.pictures = pictures
        self.watched_videos = watched_videos
        self.folders = folders
        self.block = block


class CPSSUserMetadataType:
    connections: Optional[CPSSTentacledConnectionsType]

    def __init__(self, connections: Optional[CPSSTentacledConnectionsType]) -> None:
        self.connections = connections


class CPSSSizeType:
    width: Optional[int]
    height: Optional[int]
    link: Optional[str]
    link_with_play_button: Optional[str]

    def __init__(self, width: Optional[int], height: Optional[int], link: Optional[str], link_with_play_button: Optional[str]) -> None:
        self.width = width
        self.height = height
        self.link = link
        self.link_with_play_button = link_with_play_button


class CPSSPicturesType:
    uri: Optional[str]
    active: Optional[bool]
    type: Optional[str]
    sizes: Optional[List[CPSSSizeType]]
    resource_key: Optional[str]

    def __init__(self, uri: Optional[str], active: Optional[bool], type: Optional[str], sizes: Optional[List[CPSSSizeType]], resource_key: Optional[str]) -> None:
        self.uri = uri
        self.active = active
        self.type = type
        self.sizes = sizes
        self.resource_key = resource_key


class CPSSVideosPrivacyType:
    view: Optional[str]
    comments: Optional[str]
    embed: Optional[str]
    download: Optional[bool]
    add: Optional[bool]

    def __init__(self, view: Optional[str], comments: Optional[str], embed: Optional[str], download: Optional[bool], add: Optional[bool]) -> None:
        self.view = view
        self.comments = comments
        self.embed = embed
        self.download = download
        self.add = add


class CPSSVideosType:
    privacy: Optional[CPSSVideosPrivacyType]

    def __init__(self, privacy: Optional[CPSSVideosPrivacyType]) -> None:
        self.privacy = privacy


class CPSSPreferencesType:
    videos: Optional[CPSSVideosType]

    def __init__(self, videos: Optional[CPSSVideosType]) -> None:
        self.videos = videos


class CPSSWebsiteType:
    name: Optional[str]
    link: Optional[str]
    description: None

    def __init__(self, name: Optional[str], link: Optional[str], description: None) -> None:
        self.name = name
        self.link = link
        self.description = description


class CPSSUserType:
    uri: Optional[str]
    name: Optional[str]
    link: Optional[str]
    location: Optional[str]
    bio: None
    short_bio: None
    created_time: Optional[datetime]
    pictures: Optional[CPSSPicturesType]
    websites: Optional[List[CPSSWebsiteType]]
    metadata: Optional[CPSSUserMetadataType]
    preferences: Optional[CPSSPreferencesType]
    content_filter: Optional[List[str]]
    resource_key: Optional[str]
    account: Optional[str]

    def __init__(self, uri: Optional[str], name: Optional[str], link: Optional[str], location: Optional[str], bio: None, short_bio: None, created_time: Optional[datetime], pictures: Optional[CPSSPicturesType], websites: Optional[List[CPSSWebsiteType]], metadata: Optional[CPSSUserMetadataType], preferences: Optional[CPSSPreferencesType], content_filter: Optional[List[str]], resource_key: Optional[str], account: Optional[str]) -> None:
        self.uri = uri
        self.name = name
        self.link = link
        self.location = location
        self.bio = bio
        self.short_bio = short_bio
        self.created_time = created_time
        self.pictures = pictures
        self.websites = websites
        self.metadata = metadata
        self.preferences = preferences
        self.content_filter = content_filter
        self.resource_key = resource_key
        self.account = account


class CPSSParentFolderType:
    created_time: Optional[datetime]
    modified_time: Optional[datetime]
    last_user_action_event_date: Optional[datetime]
    name: Optional[str]
    privacy: Optional[CPSSParentFolderPrivacyType]
    resource_key: Optional[str]
    uri: Optional[str]
    user: Optional[CPSSUserType]
    metadata: Optional[CPSSParentFolderMetadataType]

    def __init__(self, created_time: Optional[datetime], modified_time: Optional[datetime], last_user_action_event_date: Optional[datetime], name: Optional[str], privacy: Optional[CPSSParentFolderPrivacyType], resource_key: Optional[str], uri: Optional[str], user: Optional[CPSSUserType], metadata: Optional[CPSSParentFolderMetadataType]) -> None:
        self.created_time = created_time
        self.modified_time = modified_time
        self.last_user_action_event_date = last_user_action_event_date
        self.name = name
        self.privacy = privacy
        self.resource_key = resource_key
        self.uri = uri
        self.user = user
        self.metadata = metadata


class CPSSReviewPageType:
    active: Optional[bool]
    link: Optional[str]

    def __init__(self, active: Optional[bool], link: Optional[str]) -> None:
        self.active = active
        self.link = link


class CPSSStatsType:
    plays: Optional[int]

    def __init__(self, plays: Optional[int]) -> None:
        self.plays = plays


class CPSSStickyConnectionsType:
    videos: Optional[CPSSBasseTerreElephantType]

    def __init__(self, videos: Optional[CPSSBasseTerreElephantType]) -> None:
        self.videos = videos


class CPSSTagMetadataType:
    connections: Optional[CPSSStickyConnectionsType]

    def __init__(self, connections: Optional[CPSSStickyConnectionsType]) -> None:
        self.connections = connections


class CPSSTagType:
    uri: Optional[str]
    name: Optional[str]
    tag: Optional[str]
    canonical: Optional[str]
    metadata: Optional[CPSSTagMetadataType]
    resource_key: Optional[str]

    def __init__(self, uri: Optional[str], name: Optional[str], tag: Optional[str], canonical: Optional[str], metadata: Optional[CPSSTagMetadataType], resource_key: Optional[str]) -> None:
        self.uri = uri
        self.name = name
        self.tag = tag
        self.canonical = canonical
        self.metadata = metadata
        self.resource_key = resource_key


class CPSSTranscodeType:
    status: Optional[str]

    def __init__(self, status: Optional[str]) -> None:
        self.status = status


class CPSSUploadType:
    status: Optional[str]
    link: None
    upload_link: None
    complete_uri: None
    form: None
    approach: None
    size: None
    redirect_url: None

    def __init__(self, status: Optional[str], link: None, upload_link: None, complete_uri: None, form: None, approach: None, size: None, redirect_url: None) -> None:
        self.status = status
        self.link = link
        self.upload_link = upload_link
        self.complete_uri = complete_uri
        self.form = form
        self.approach = approach
        self.size = size
        self.redirect_url = redirect_url


class CPSSDatumType:
    uri: Optional[str]
    name: Optional[str]
    description: Optional[str]
    type: Optional[str]
    link: Optional[str]
    duration: Optional[int]
    width: Optional[int]
    language: None
    height: Optional[int]
    embed: Optional[CPSSEmbedType]
    created_time: Optional[datetime]
    modified_time: Optional[datetime]
    release_time: Optional[datetime]
    content_rating: Optional[List[str]]
    license: None
    privacy: Optional[CPSSVideosPrivacyType]
    pictures: Optional[CPSSPicturesType]
    tags: Optional[List[CPSSTagType]]
    stats: Optional[CPSSStatsType]
    categories: Optional[List[Any]]
    metadata: Optional[CPSSDatumMetadataType]
    user: Optional[CPSSUserType]
    review_page: Optional[CPSSReviewPageType]
    parent_folder: Optional[CPSSParentFolderType]
    last_user_action_event_date: Optional[datetime]
    files: Optional[List[CPSSDownloadType]]
    download: Optional[List[CPSSDownloadType]]
    app: Optional[CPSSAppType]
    status: Optional[str]
    resource_key: Optional[str]
    upload: Optional[CPSSUploadType]
    transcode: Optional[CPSSTranscodeType]

    def __init__(self, uri: Optional[str], name: Optional[str], description: Optional[str], type: Optional[str], link: Optional[str], duration: Optional[int], width: Optional[int], language: None, height: Optional[int], embed: Optional[CPSSEmbedType], created_time: Optional[datetime], modified_time: Optional[datetime], release_time: Optional[datetime], content_rating: Optional[List[str]], license: None, privacy: Optional[CPSSVideosPrivacyType], pictures: Optional[CPSSPicturesType], tags: Optional[List[CPSSTagType]], stats: Optional[CPSSStatsType], categories: Optional[List[Any]], metadata: Optional[CPSSDatumMetadataType], user: Optional[CPSSUserType], review_page: Optional[CPSSReviewPageType], parent_folder: Optional[CPSSParentFolderType], last_user_action_event_date: Optional[datetime], files: Optional[List[CPSSDownloadType]], download: Optional[List[CPSSDownloadType]], app: Optional[CPSSAppType], status: Optional[str], resource_key: Optional[str], upload: Optional[CPSSUploadType], transcode: Optional[CPSSTranscodeType]) -> None:
        self.uri = uri
        self.name = name
        self.description = description
        self.type = type
        self.link = link
        self.duration = duration
        self.width = width
        self.language = language
        self.height = height
        self.embed = embed
        self.created_time = created_time
        self.modified_time = modified_time
        self.release_time = release_time
        self.content_rating = content_rating
        self.license = license
        self.privacy = privacy
        self.pictures = pictures
        self.tags = tags
        self.stats = stats
        self.categories = categories
        self.metadata = metadata
        self.user = user
        self.review_page = review_page
        self.parent_folder = parent_folder
        self.last_user_action_event_date = last_user_action_event_date
        self.files = files
        self.download = download
        self.app = app
        self.status = status
        self.resource_key = resource_key
        self.upload = upload
        self.transcode = transcode


class CPSSPagingType:
    next: Optional[str]
    previous: None
    first: Optional[str]
    last: Optional[str]

    def __init__(self, next: Optional[str], previous: None, first: Optional[str], last: Optional[str]) -> None:
        self.next = next
        self.previous = previous
        self.first = first
        self.last = last


class CPSSVimeoCollectionType:
    total: Optional[int]
    page: Optional[int]
    per_page: Optional[int]
    paging: Optional[CPSSPagingType]
    data: Optional[List[CPSSDatumType]]

    def __init__(self, total: Optional[int], page: Optional[int], per_page: Optional[int], paging: Optional[CPSSPagingType], data: Optional[List[CPSSDatumType]]) -> None:
        self.total = total
        self.page = page
        self.per_page = per_page
        self.paging = paging
        self.data = data

    def __init__(self, input):
        dictList = []
        for key, value in input.items():
            self.__dict__[key] = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class VimeoClientManager(models.Manager):
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class VimeoClientType(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    vimeo_user_id = models.CharField(
        verbose_name=_("Vimeo User ID"), max_length=100, default="")
    vimeo_client_id = models.CharField(
        verbose_name=_("Vimeo Client ID"), max_length=100, default="")
    vimeo_client_secret = models.CharField(
        verbose_name=_("Vimeo Client Secret"), max_length=100, default="")
    vimeo_access_token = models.CharField(
        verbose_name=_("Vimeo Access Token"), max_length=100, default="")
    vimeo_project_id = models.CharField(
        verbose_name=_("Vimeo Project ID/Folder ID"), unique=True, max_length=100, default="")
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, verbose_name=_('Site'), blank=True)

    class Meta:
        abstract = True


class VimeoClientOption(VimeoClientType):
    objects = VimeoClientManager()

    class Meta:
        db_table = 'vimeo_django_settings'
        verbose_name = _('CPSS Vimeo Client Setting')
        verbose_name_plural = _('CPSS Vimeo Client Settings')

    def __str__(self):
        return str(self.site.domain) + ": " + str(self.vimeo_project_id)

    def get_folder_contents(self):
        v = VimeoClient(
            token=self.vimeo_access_token,
            key=self.vimeo_client_id,
            secret=self.vimeo_client_secret
        )
        response = v.get('/users/' + self.vimeo_user_id +
                         '/projects/' + self.vimeo_project_id + '/videos')
        assert response.status_code == 200
        return CPSSVimeoCollectionType(response.json())

