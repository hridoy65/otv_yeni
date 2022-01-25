# -*- coding: utf-8 -*-

# Author: FactoryKodi
# Email: factorykodi@yandex.com
# Created on: 15.04.2017
from resources.sites.LIVETV2 import *
import sys, os
from urllib.parse import urlencode
from urllib.parse import parse_qsl
import xbmcgui
import xbmcplugin
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
import json
try:  # Python 2
    import urllib2

except ImportError:  # Python 3
    import urllib.request as urllib2

_url = sys.argv[0]
_handle = int(sys.argv[1])
_base_dir = os.path.abspath(os.path.dirname(__file__))
def load():
    
    router(sys.argv[2][1:])
#param = dict(parse_qsl(paramstring))
class itemModel:
    key = None
    value = None
    thumb = _base_dir + "/thumb.jpg"
    icon = _base_dir + "/icon.png"
    fanart = _base_dir + "/fanart.jpg"
    plot = ""


def turkish_charset(data):
    data = data.replace("İ", "I") \
        .replace("Ş", "S") \
        .replace("Ğ", "G") \
        .replace("Ç", "C") \
        .replace("Ö", "O") \
        .replace("Ü", "U") \
        .replace("ı", "i") \
        .replace("ş", "s") \
        .replace("ğ", "g") \
        .replace("ç", "c") \
        .replace("ö", "o") \
        .replace("ü", "u")
    return data

def get_url(**kwargs):
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_group_source():
    req = urllib2.Request('https://puhutv.com/api/title_groups')
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_search_source(param):
    param = turkish_charset(param).lower()
    req = urllib2.Request('https://puhutv.com/search/search?query={0}'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_programs_source(param):
    req = urllib2.Request('https://puhutv.com/api/slug/{0}?s_page=1&s_per=100'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_seasons_source(param):
    req = urllib2.Request('https://puhutv.com/api/slug/{0}'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_episodes_source(param):
    req = urllib2.Request('https://puhutv.com/api/seasons/{0}/episodes?e_page=1&e_per=100'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_video_source(param):
    req = urllib2.Request('https://puhutv.com/api/assets/{0}/videos'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data


def get_segment_list_source():
    req = urllib2.Request('https://puhutv.com/api/containers/main?c_page=1&c_per=40')
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data

def get_segment_source(param):
    req = urllib2.Request('https://puhutv.com/api/segments/{0}?s_page=1&s_per=50'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data

def get_playlist_source(param):
    req = urllib2.Request('https://puhutv.com/api/playlists/{0}?p_page=1&p_per=40'.format(param))
    response = urllib2.urlopen(req)
    groups_page = response.read()
    data = json.loads(groups_page)
    return data

def list_segments():
    segment_list = []
    data = get_segment_list_source()["data"]
    for x in data["container_items"]:
        if x['containable_type']=='Segment':
            item = itemModel()
            item.key = x['containable']["display_name"]
            item.value = x['containable']["id"]
            segment_list.append(item)
    list_items("segments", segment_list)

def list_segment_items(param):
    segment_item_list = []
    data = get_segment_source(param)["data"]
    for x in data["titles"]:
        item = itemModel()
        item.key = x["name"]
        item.value = x["slug_path"]
        item.thumb = "http://" + x["images"]["vertical_thumbnail"]["main"]
        item.fanart = "http://" + x["images"]["super_wide"]["main"]
        item.plot = x["short_description"]
        segment_item_list.append(item)
    list_items("season", segment_item_list)


def list_playlist_items(param):
    segment_item_list = []
    data = get_playlist_source(param)["data"]
    for x in data["assets"]:
        item = itemModel()
        item.key = x['content']["display_name"]
        item.value = x["id"]
        item.thumb = "http://" + x['content']["images"]["wide"]["main"]
        item.fanart = "http://" + x['content']["images"]["wide"]["main"]
        item.plot = x['title']["description"]
        segment_item_list.append(item)
    list_items("videos", segment_item_list)


def list_playlist():
    play_list = []
    data = get_segment_list_source()["data"]
    for x in data["container_items"]:
        if x['containable_type']=='Playlist':
            item = itemModel()
            item.key = x['containable']["display_name"]
            item.value = x['containable']["id"]
            play_list.append(item)
    list_items("playlist", play_list)



def list_programs(param):
    programs_list = []
    data = get_programs_source(param)["data"]
    for x in data["titles"]:
        item = itemModel()
        item.key = x["name"]
        item.value = x["slug_path"]
        item.thumb = "http://" + x["search_images"]["vertical_thumbnail"]["main"]
        item.fanart = "http://" + x["search_images"]["super_wide"]["main"]
        item.plot = x["short_description"]
        programs_list.append(item)
    list_items("season", programs_list)


def list_search(param):
    search_list = []
    data = get_search_source(param)
    for x in data["data"]:
        item = itemModel()
        item.key = x["name"]
        item.value = x["slug_path"]
        item.thumb = "http://" + x["search_images"]["vertical_thumbnail"]["main"]
        item.fanart = "http://" + x["search_images"]["super_wide"]["main"]
        item.plot = x["short_description"]
        search_list.append(item)
    list_items("season", search_list)


def list_genres(param):
    subcategory_list = []
    if param == "search_item":
        search = xbmcgui.Dialog().input("Ara")
        if search == '':
            return
        list_search(search)
    elif param == "segments":
        list_segments()
    elif param == "playlist":
        list_playlist()

    else:
        data = list(filter(lambda x: x["name"] == param, get_group_source()["data"]))
        logger.info("param-%s " %param)
        for x in data["data"]:
            item = itemModel()
            item.key = x["display_name"]
            item.value = x["slug_path"]
            subcategory_list.append(item)
        if not subcategory_list:
            item = itemModel()
            item.key = data[0]["display_name"]                   
            item.value = data[0]["slug_path"]
            subcategory_list.append(item)
        list_items("programs", subcategory_list)


def list_season(param):
    season_list = []
    data = get_seasons_source(param)["data"]
    for x in data["seasons"]:
        item = itemModel()
        item.key = x["name"] + " " + str(x["position"])
        item.value = str(x["id"])
        item.thumb = "http://" + data["images"]["vertical_thumbnail"]["main"]
        item.fanart = "http://" + data["images"]["super_wide"]["main"]
        season_list.append(item)
    if season_list:
        list_items("episodes", season_list)
    else:
        item = itemModel()
        item.key = data["assets"][0]["name"]
        item.value = str(data["assets"][0]["id"])
        item.thumb = "http://" + data["images"]["vertical_thumbnail"]["main"]
        item.fanart = "http://" + data["images"]["super_wide"]["main"]
        list_items("videos", [item])


def list_episodes(param):
    episode_list = []
    data = get_episodes_source(param)["data"]
    for ep in data["episodes"]:
        for x in ep["assets"]:
            if x["content"]["content_type"] == "main":
                item = itemModel()
                item.key = x["name"]
                item.value = str(x["id"])
                item.thumb = "http://" + ep["images"]["wide"]["main"]
                item.fanart = "http://" + ep["images"]["wide"]["main"]
                episode_list.append(item)
    list_items("videos", episode_list)


def list_videos(param):
    video_list = []
    data = get_video_source(param)["data"]
    for x in data["videos"]:
        item = itemModel()
        name = x["url"].split('?')[0].split('/')
        item.key = name[-1] + " - " + name[-2]
        item.value = x["url"]
        video_list.append(item)
    list_items("play", video_list)


def list_categories():
    category_list = []
    data = get_group_source()
    for x in data["data"]:
        item = itemModel()
        item.key = x["display_name"]
        item.value = x["name"]
        category_list.append(item)
    item = itemModel()
    item.key = "[COLOR blue][B]Kategoriler[/B][/COLOR]"
    item.value = "segments"
    category_list.append(item)
    item = itemModel()
    item = itemModel()
    item.key = "[COLOR red][B]Listeler[/B][/COLOR]"
    item.value = "playlist"
    category_list.append(item)
    item = itemModel()
    item.key = "[COLOR yellow][B]Ara[/B][/COLOR]"
    item.value = "search_item"
    category_list.append(item)
    list_items("genres", category_list)

def list_items(action, categories):
    for category in categories:
        
        logger.info("category-%s " %category)
        list_item = xbmcgui.ListItem(label=category.key)
        list_item.setInfo(type='Video', infoLabels={'plot': category.plot, 'thumb': category.thumb})
        list_item.setArt({'thumb': category.thumb,
                          'icon': category.icon,
                          'fanart': category.fanart})

        url = get_url(action=action, category=category.value)
        if action == "play":
            list_item.setProperty('IsPlayable', 'true')
        is_folder = not action == "play"
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    if not action in ["genres","segments"]:
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    play_item = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def router(paramstring):
    params = dict(parse_qsl(paramstring))
    logger.info("category-%s " %params)
    if params:
        if params['action'] == 'genres':
            list_genres(params)
        elif params['action'] == 'programs':
            list_programs(params['category'])
        elif params['action'] == 'season':
            list_season(params['category'])
        elif params['action'] == 'episodes':
            list_episodes(params['category'])
        elif params['action'] == 'videos':
            list_videos(params['category'])
        elif params['action'] == 'play':
            play_video(params['category'])
        elif params['action'] == 'search_item':
            list_search(params['category'])
        elif params['action'] == 'segments':
            list_segment_items(params['category'])
        elif params['action'] == 'playlist':
            list_playlist_items(params['category'])
        else:
            logger.info("category-%s " %params)
    else:
        list_categories()


if __name__ == '__main__':
    router(sys.argv[2][1:])
