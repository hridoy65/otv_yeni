#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        YouTube
# Purpose:
#
# Author:      orhan
#
# Created:     29.04.2021
# Copyright:   (c) orhan 2021
# Licence:     <your licence>
from resources.lib.youtube_api.youtube.provider import Provider
provider = Provider()
from resources.lib.youtube_api.kodion.impl import Context
context = Context(plugin_id='plugin.video.OTV_MEDIA')
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

from resources.lib.youtube_api.functions import build_url, delete_database, get_folders, add_folder, remove_folder, get_channels, get_channel_id_from_uploads_id, add_channel, remove_channel, search_channel, search_channel_by_username, get_latest_from_channel, get_playlists, add_sort_db, init_sort, move_up, move_down, check_sort_db, change_folder, set_folder_thumbnail, get_folder_thumbnail, check_thumb_db, add_thumb_db, get_livestreams

from resources.sites.LIVETV2 import *
from resources.lib.youtube_api.youtube_api import YouTube  
SITE_IDENTIFIER = 'youtubecom_tr'
SITE_NAME = 'YouTube'
SITE_DESC = 'YouTube'

uqp = urllib.parse.unquote_plus       
YUPA = 'https://www.y2mate.com/mates/analyze/ajax'
URL_MAIN = 'http://www.youtube.com/embed/'
URL_PIC = 'http://s.dogannet.tv/'
URL_LIVE = 'https://www.youtube.com/watch?v='
MOVIE_MOVIE = ('http://', 'showAlpha')
MOVIE_GENRES = (True, 'showGenre')

api_key='AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
URL_SEARCH = ('', 'showMovies')
def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)

USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))

playlistsFile2 = os.path.join(USER_DATA_DIR, "playLists.txt")
playlistsFile3 = os.path.join(USER_DATA_DIR, "FolderListe3.txt")

playlistsFile4 = os.path.join(USER_DATA_DIR, "FolderLists.txt")
nextlists = os.path.join(USER_DATA_DIR, "nextlists.txt")

from resources.lib.peewee import (
    SqliteDatabase,
    Model,
    IntegerField,
    TextField,
    ForeignKeyField,
    FloatField,
    chunked,
)

from requests.utils import requote_uri
def read_url(url):
	url = requote_uri(url)
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0')
	response = urllib.request.urlopen(req)
	link=response.read()
	response.close()
	return link.decode('utf-8')

def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
from resources.lib.youtube_api.yardim import datetime_parser
from resources.lib.youtube_api.yardim.OAuth import OAuth, API_KEY

from collections import OrderedDict				
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
from resources.lib.comaddon import dialog
from resources.lib.util import Unquote, Quote


                  #  'title': 'ANKARA PAVYON HAVALARI'

def yyvideos(v_id,itag):
         #sourcestr = 'https://raw.githubusercontent.com/iptv-org/iptv/master/scripts/data/countries.json'
         #sHtmlContent = getHtml(sourcestr) 
        # logger.info("metin-%s " %metin)
         from youtubesearchpython.extras import Video
         video = Video.get("https://www.youtube.com/watch?v=%s"%v_id )
		
                      
         
         sPattern = "'itag': "+itag+", 'url': '(.+?)'"
         oParser = cParser()
         aResult = oParser.parse(video, sPattern)
         if (aResult[0] == True):
              return  aResult[1][0] 



def youtubeHtml(sUrl):  # S'occupe des requetes
       # Host ='www.youtube.com'
        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        headers = {"User-Agent": UA}
        req = urllib2.Request(sUrl, None, headers)
        try:
            response = urllib2.urlopen(req)
        except UrlError as e:
            print(e.read())
            print(e.reason)

        data = response.read()
        head = response.headers
        response.close()
        return to_utf8(data )
        logger.info("data : %s" % str(data))
        logger.info("sUrl : %s" % str(head))
addon = xbmcaddon.Addon()
def get_unix_timestamp():
    """ User defined function for SQLite """
    return int(time.time())






def kkYouTUBE():   
    oGui = cGui()
    from resources.lib.youtube_api import default
    tarzlistesi = []
    tarzlistesi.append(("Search videos", "showSearch1"))
    
#    tarzlistesi.append(("Search channels", "Searchchannel"))
    tarzlistesi.append(("Search playlists", "Searchplaylist"))                                     
    tarzlistesi.append(("live broadcasts on youtube", "showSearch3")) 
    tarzlistesi.append(("canli yayin", "showSearch3")) 
    tarzlistesi.append(("canli radyo", "showSearch3")) 
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, sUrl2, sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
#from resources.lib.youtube_api import default

#from resources.lib.youtube_api.kodion.impl import Context
#context = Context(plugin_id='plugin.video.OTV_MEDIA')
#plugin_handle = context.get_params()
def YouTUBE():   
    from resources.lib.youtube_api import default




    tarzlistesi = []
    tarzlistesi.append(("Search videos", "showSearch1"))
    
#    tarzlistesi.append(("Search channels", "Searchchannel"))
    tarzlistesi.append(("Search playlists", "Searchplaylist"))                                     
    tarzlistesi.append(("live broadcasts on youtube", "showSearch3")) 
    tarzlistesi.append(("canli yayin", "showSearch3")) 
    tarzlistesi.append(("canli radyo", "showSearch3")) 
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, sUrl2, sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def Searchchannel():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'Searchchannel2', 'Search channels', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile3)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]                                                
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'Searchchannel5', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil3', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()   
def listeyisil3():
   from resources.lib import comon
   comon.DelFile(playlistsFile3)
   return      

def Searchchannel2():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile3)
       listUrl = '1'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile3, list):

            #from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTube()
            
            data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
            
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', channel_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   
def Searchchannel5():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')
        from resources.lib.youtube_api.youtube_api import YouTube 
       
        yt = YouTube()
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #sTitle =cat['Title']
            sPicture=cat['video_thumbnail']
            sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            channel_id=cat['channel_id']
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   

def Searchchannel3():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            channel_id = oInputParameterHandler.getValue('siteUrll')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.get_channel_metadata(channel_id)                   
            logger.info("Searchchannel3channel_id: %s" % data) 
            for cat in data:
                #video_id =cat['video_id']
            #sTitle =cat['Title']
                           
                sTitle=cat['title']
                des=cat['description']
                channel_id=cat['channel_id']
             
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', playlist_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel4', sTitle, sPicture, sPicture, "-- Bölüm- %s" %str(des) , oOutputParameterHandler)
            oGui.setEndOfDirectory()   


def Searchchannel4():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sTitle  = oInputParameterHandler.getValue('sMovieTitle')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            s_num = 0
            data =yt.get_video_metadata_gen(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video =cat['video_id']
            #sTitle =cat['Title']
               
                #sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                #des=cat['playlist_n_videos']
                #playlist_id=cat['playlist_id']
                s_num += 1 
              
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video)
               # oOutputParameterHandler.addParameter('siteUrll', video)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox3', sTitle+"-Video- %s" % str(s_num+0),'','', sTitle, oOutputParameterHandler)
            oGui.setEndOfDirectory()   


def Searchplaylist():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'Searchplaylist2', 'Search playlists', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile4)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'Searchplaylist5', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil2', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()   
def Searchplaylist5():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #sTitle =cat['Title']
            sPicture=cat['video_thumbnail']
            sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            channel_id=cat['channel_id']
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   

def listeyisil2():
   from resources.lib import comon
   comon.DelFile(playlistsFile4)
   return

def Searchplaylist2():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile4)
       listUrl = '1'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile4, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
            
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   
def Searchplaylist3():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            yt = YouTube()
            
            data =yt.get_playlists(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                #video_id =cat['video_id']
            #sTitle =cat['Title']
               
                sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                des=cat['playlist_n_videos']
                playlist_id=cat['playlist_id']
             
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', playlist_id)
                oOutputParameterHandler.addParameter('siteUrll', playlist_id)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist4', sTitle, sPicture, sPicture, "-- Videos- %s" %str(des) , oOutputParameterHandler)
            oGui.setEndOfDirectory()   

def Searchplaylist4():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sTitle  = oInputParameterHandler.getValue('sMovieTitle')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            s_num = 0
            data =yt.get_videos_from_playlist_id(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video =cat['video_id']
            #sTitle =cat['Title']
               
                #sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                #des=cat['playlist_n_videos']
                #playlist_id=cat['playlist_id']
                s_num += 1 
              
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video)
               # oOutputParameterHandler.addParameter('siteUrll', video)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox3', sTitle+"-Bölüm- %s" % str(s_num+0),'','', sTitle, oOutputParameterHandler)
            oGui.setEndOfDirectory()   


def showSearch():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
      # sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile2)
       listUrl = '1'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile2, list):

            yt = YouTube()
            
            data =yt.search(sSearchText)                   
            logger.info("showSearch-video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
                des=videoDetails(video_id)
                logger.info("video_id-des : %s" % des)
                
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
                desc=desc+'--------' + des
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   

def showSearch1():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Search', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile2)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'myeniplay', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()                   
def listeyisil():
   from resources.lib import comon
   comon.DelFile(playlistsFile2)
   return
def raw_json_with_datetime(item):
    '''
    Returns the raw json output from the API.
    '''
    item['collection_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    return item

def showSearch3():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        yt = YouTube()
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #des=videoDetails(video_id)
            #logger.info("video_id-des : %s" % des)
            sPicture=cat['video_thumbnail']
            name=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            de=cat['collection_date'] #= datetime.datetime.now()
            channel_id=cat['channel_id']
            desc=desc+"[COLOR red] TIME - %s[/COLOR]" % de
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sSearchText ))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', name, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   


def myfeeds():
    oGui = cGui()
  #  from .YouTubeUi import YouTubeSetup
    tarzlistesi = []
    tarzlistesi.append(("My Subscriptions", "my_subscriptions"))
    
    tarzlistesi.append(("Liked videos", "my_liked_videos"))
    tarzlistesi.append(("Uploads", "my_uploads"))                                     
    tarzlistesi.append(("Playlists", "my_playlists")) 
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TÚRK Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeturk', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search2':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch2', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'Arabic Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubearabic', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'German Cinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeargermany', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
          
def nextplay(name,sUrl):
	     
   
	        playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    
	        playlist.clear();
	        listitem = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl,listitem);
	        player_type = sPlayerType()
	        xbmcPlayer = xbmc.Player (); 
	        xbmcPlayer.play (playlist)  
	        sys.exit()
	        return ok 
def sPlayerType():
       
        
        try:
            if (sPlayerType == '0'):
               
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
          
          
              
import datetime 
  
def mconvert(n): 
    return str(datetime.timedelta(seconds = n)) 
          
import time 
  
def kconvert(n): 
    return str(time.strftime("%H:%M:%S", time.gmtime(n))) 



def videoDetails():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =Search(sSearchText).videos()                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #des=videoDetails(video_id)
            #logger.info("video_id-des : %s" % des)
            sPicture=cat['video_thumbnail']
            name=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            #de=cat['collection_date'] = datetime.datetime.now()
            #channel_id=cat['channel_id']
            desc="[COLOR red] TIME - %s[/COLOR]"+ desc
            sPicture=malfabekodla (sPicture)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            #oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sSearchText ))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', name, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory() 
def mvideoDetails():
    
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile3)
       listUrl = '1'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile3, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            data =Search(sSearchText).videos()  
            #data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                #channel_id=cat['channel_id']
                logger.info("sTitle : %s" % sTitle) 
                
               # oOutputParameterHandler.addParameter('siteUrl', channel_id)
                oOutputParameterHandler.addParameter('siteUrll', video_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   



  


def get_playlists(json_data):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    token= oInputParameterHandler.getValue('sMovieTitle')
	#logger.info("json_data: %s" % str(json_data))
#	playlists = json_data.get('items', [])
    NextPage = json_data.get('nextPageToken')

    videoids = []
    from resources.lib import comon
    listDir = comon.ReadList(nextlists)
    token = listDir["name"]
    for i in range(0, len(json_data['items'])):
	    video_id = json_data['items'][i]['id']['videoId']
	    videoids.append(video_id)
	    video_req_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails&id=%s&key=%s' % (','.join(videoids), API_KEY)
	    video_read = read_url(video_req_url)
	    video_decoded = json.loads(video_read)
	    sorted_data = sorted((video_decoded['items']), key=(lambda i: i['snippet']['publishedAt']), reverse=True)
	    for i in range(0, len(sorted_data)):
  	        title = sorted_data[i]['snippet']['title']
  	        video_id = sorted_data[i]['id']
  	        thumb = sorted_data[i]['snippet']['thumbnails']['high']['url']
  	        desc = sorted_data[i]['snippet']['description']
            #title =snippet.get('title', '').replace('#', '').replace('amp;', '').replace('39;', '')
           # title ="[COLOR blue]%s:[/COLOR]" % str(m)+ ''+title

  	        oOutputParameterHandler = cOutputParameterHandler()
  	        oOutputParameterHandler.addParameter('siteUrl',video_id )
  	        oOutputParameterHandler.addParameter('sMovieTitle', str(title))
  	        #oOutputParameterHandler.addParameter('playlist', str(token))
  	        oOutputParameterHandler.addParameter('sThumbnail',  thumb)
  	        #oGui.addLink(SITE_IDENTIFIER, 'kmsshowBox2', title, sPicture,  desc, oOutputParameterHandler)
  	        #oGui.addEpisode(SITE_IDENTIFIER, 'msshowBox2', title,  sPicture, desc, oOutputParameterHandler)
  	        oGui.addEpisode(SITE_IDENTIFIER, 'msshowBox2', title, '', thumb, desc, oOutputParameterHandler)
    sNextPage = ''
    if (sNextPage != False):
  	        oOutputParameterHandler = cOutputParameterHandler()
  	        oOutputParameterHandler.addParameter('siteUrll',NextPage)
  	        oOutputParameterHandler.addParameter('sMovieTitle', str(token))
  	        oGui.addDir(SITE_IDENTIFIER, 'nextlist', '[COLOR blue]Next >>>[/COLOR]'  , 'next.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def mvidbox(v_id):                       
  #  logger.info("Param-v_id: %s" % str(Param))
    logger.info("v_id---: %s" % str(v_id)) 
def yvideos(v_id,itag,tag):
                                
         yt = YouTube()
         ita='itag='+itag  
         tita='/itag/'+tag                     
         video =yt.get_video_streams(v_id)                     
         title =video[0]['meta']['video']['title']
         logger.info("video : %s" % str(title))
         sPattern = "'url': '(.+?)'"
         oParser = cParser()
         aResult = oParser.parse(video, sPattern)
         if (aResult[0] == True):
                for aEntry in aResult[1]:
                  if  ita in aEntry :
                     return aEntry +'|User-Agent=Mozilla/5.0%20%28Linux%3B%20Android%207.0%3B%20SM-G892A%20Build/NRD90M%3B%20wv%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Version/4.0%20Chrome/67.0.3396.87%20Mobile%20Safari/537.36&Accept=%2A/%2A&DNT=1&Accept-Encoding=gzip%2C%20deflate&Accept-Language=en-US%2Cen%3Bq%3D0.5'

                  if  tita in aEntry:
                     return aEntry+'|User-Agent=Mozilla/5.0%20%28Linux%3B%20Android%207.0%3B%20SM-G892A%20Build/NRD90M%3B%20wv%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Version/4.0%20Chrome/67.0.3396.87%20Mobile%20Safari/537.36&Accept=%2A/%2A&DNT=1&Accept-Encoding=gzip%2C%20deflate&Accept-Language=en-US%2Cen%3Bq%3D0.5'
def Searchchannell():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')
        sSearchText =sSearchText.replace('([COLOR red]', '').replace('[/COLOR]) [B]', '').replace('[/B]', '').replace('–', '-')
        logger.info("sSearchText: %s" % str(sSearchText))
        from resources.lib.youtube_api.youtube_api import YouTube 
       
        yt = YouTube()                                                               
            
        data =yt.search(sSearchText)                   
        logger.info("data: %s" % str(data))
        playlists = data.get('items', [])
        for playlist in playlists:
            snippet = playlist.get('snippet', {})
            
            desc = snippet.get('description', '')
            sPicture = snippet.get('thumbnails', {}).get('high', {}).get('url', context.create_resource_path('media', 'playlist.png'))
             
            pid = playlist.get('id', '')
            
            #playlist_id = pid.get('playlistId', '')
            
            sTitle =snippet.get('title', '').replace('#', '').replace('amp;', '').replace('39;', '')
            video_id  = pid.get('videoId', '')
            if not 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' in video_id:
                
                video_id = re.findall('https://i.ytimg.com/vi/(.+?)/.+?.jpg', sPicture, re.S)[0]
                                                      
            logger.info("video_id: %s" % str(video_id))
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            #oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'YouTubeplay', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   

def YouTubeplay():                       
        oInputParameterHandler = cInputParameterHandler()
        v_id = oInputParameterHandler.getValue('siteUrl')
        logger.info("v_id: %s" % str(v_id))
        yt = YouTube()
        video =yt.get_video_streams(v_id)  
        name =video[0]['meta']['video']['title']
        url=yvideos(v_id, '22','96')                  
        if url == None:
          url=yvideos(v_id, '18','95')
          if url == None:
            url=yvideos(v_id, '84','300')
            if url == None:
               url=yvideos(v_id, '37','94')
        
        adLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url,'')
        #sys.exit()
        #return oPlayer.run(oGuiElement, v_id)

def YouTubeplay2(v_id):                       
        yt = YouTube()
        video =yt.get_video_streams(v_id)  
        name =video[0]['meta']['video']['title']
        url=yvideos(v_id, '22','96')                  
        if url == None:
          url=yvideos(v_id, '18','95')
          if url == None:
            url=yvideos(v_id, '84','300')
            if url == None:
               url=yvideos(v_id, '37','94')
        
        adLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url,'')
    
def adLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
#    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 

def sPlayerType():


        try:
            if (sPlayerType == '0'):

                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):

                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):

                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False	      
def myeniplay():
   oGui = cGui()
   list=[]
   oInputParameterHandler = cInputParameterHandler()
   page= oInputParameterHandler.getValue('siteUrl').replace('https://youtube.otvmedia', '')
  # sNextPage= page
   sSearchText= oInputParameterHandler.getValue('sMovieTitle')
   from resources.lib import comon
  # dicti=urllib.parse.parse_qs(sys.argv[2][1:])
  # page=dicti['page'][0]
   comon.SaveList(nextlists, {"name": sSearchText, "url": "url"})
   livestreams= search_channel(sSearchText,page)#(sSearchText,'',search_type)
   logger.info("items: %s" % str(livestreams))
   for i in range(1,len(livestreams)):
  	        title=livestreams[i][0]
  	        video_id=livestreams[i][1]
  	        thumb=livestreams[i][2]
  	        desc=livestreams[i][3]
  	        dur=livestreams[i][4]
  	        tar=livestreams[i][5]
  	        sNextPage=livestreams[i][6]
  	        m=datetime_parser.parse(dur)
            #title =snippet.get('title', '').replace('#', '').replace('amp;', '').replace('39;', '')
  	        title ="[COLOR blue]%s:[/COLOR]" % str(m)+ ''+title

  	        oOutputParameterHandler = cOutputParameterHandler()
  	        oOutputParameterHandler.addParameter('siteUrl',video_id )
  	        oOutputParameterHandler.addParameter('sMovieTitle', str(title))
  	        #oOutputParameterHandler.addParameter('playlist', str(token))
  	        oOutputParameterHandler.addParameter('sThumbnail',  thumb)
  	        #oGui.addLink(SITE_IDENTIFIER, 'kmsshowBox2', title, sPicture,  desc, oOutputParameterHandler)
  	        #oGui.addEpisode(SITE_IDENTIFIER, 'msshowBox2', title,  sPicture, desc, oOutputParameterHandler)
  	        oGui.addEpisode(SITE_IDENTIFIER, 'smsshowBox2', title, '', thumb, desc, oOutputParameterHandler)
   sNextPage=sNextPage
   if (sNextPage != False):
  	        listDir = comon.ReadList(nextlists)
  	        token = listDir["name"]
  	        oOutputParameterHandler = cOutputParameterHandler()
  	        oOutputParameterHandler.addParameter('siteUrl',sNextPage)
  	        oOutputParameterHandler.addParameter('sMovieTitle', str(token))
  	        oGui.addDir(SITE_IDENTIFIER, 'myeniplay', '[COLOR blue]Next >>>[/COLOR]'  , 'next.png', oOutputParameterHandler)


   oGui.setEndOfDirectory()


    
def vmyeniplay():           
   oGui = cGui()
   list=[]
   oInputParameterHandler = cInputParameterHandler()
   sSearchText= oInputParameterHandler.getValue('sMovieTitle')
   logger.info("sSearchText: %s" %sSearchText)
   from resources.lib import comon
   search_type='video'
   #import scrapetube

#videos = scrapetube.get_search("python")
   comon.SaveList(nextlists, {"name": sSearchText, "url": "url"})
   items= get_search(sSearchText)
   for video in items:
    #print(video['videoId'])  
  	       # logger.info("items: %s" %str(video))
#     logger.info("items: %s" %video['videoId'])
#     logger.info("thumbnail: %s" %video['thumbnail']['thumbnails'][0]['url'])
#     logger.info("text: %s" %video['title']['runs'][0]['text'])
#     logger.info("text: %s" %video['lengthText']['accessibility']['accessibilityData']['label'])
#     logger.info("text: %s" %video['accessibility']['accessibilityData']['label'])
    	      title=video['title']['runs'][0]['text']
    	      video_id=video['videoId']
    	      thumb=video['thumbnail']['thumbnails'][0]['url']
  	      
    	      dur=video['lengthText']['accessibility']['accessibilityData']['label']
    	      desc=''#title['accessibility']['accessibilityData']['label']
    	        
    	      sNextPage=''
  	       # m=datetime_parser.parse(dur)
            #title =snippet.get('title', '').replace('#', '').replace('amp;', '').replace('39;', '')
    	      title ="[COLOR blue]%s:[/COLOR]" % str(dur)+ ''+title

    	      oOutputParameterHandler = cOutputParameterHandler()
    	      oOutputParameterHandler.addParameter('siteUrl',video_id )
    	      oOutputParameterHandler.addParameter('sMovieTitle', str(title))
  	        #oOutputParameterHandler.addParameter('playlist', str(token))
    	      oOutputParameterHandler.addParameter('sThumbnail',  thumb)
  	        #oGui.addLink(SITE_IDENTIFIER, 'kmsshowBox2', title, sPicture,  desc, oOutputParameterHandler)
  	        #oGui.addEpisode(SITE_IDENTIFIER, 'msshowBox2', title,  sPicture, desc, oOutputParameterHandler)
    	      oGui.addEpisode(SITE_IDENTIFIER, 'smsshowBox2', title, '', thumb, desc, oOutputParameterHandler)
   sNextPage=sNextPage
   if (sNextPage != False):
    	      listDir = comon.ReadList(nextlists)
    	      token = listDir["name"]
    	      #data = get_ajax_data(session, api_endpoint, api_key, next_data, client)
           # next_data = get_next_data(data)
            
    	      oOutputParameterHandler = cOutputParameterHandler()
  	       # oOutputParameterHandler.addParameter('siteUrl',sNextPage)
    	      oOutputParameterHandler.addParameter('sMovieTitle', str(token))
    	      oGui.addDir(SITE_IDENTIFIER, 'myeniplay', '[COLOR blue]Next >>>[/COLOR]'  , 'next.png', oOutputParameterHandler)


   oGui.setEndOfDirectory()


   

def nextlist():
   oGui = cGui()
   oInputParameterHandler = cInputParameterHandler()
   page_token= oInputParameterHandler.getValue('siteUrll')
   token= oInputParameterHandler.getValue('sMovieTitle')
   logger.info("page_token: %s" % str(page_token))
   logger.info("token: %s" % str(token))
   items= YouTube().search(token,page_token )
   get_playlists(items)


  
    
class youtub(object):
    def __init__(self, key=''):
        self.list = [] ; self.data = []
        self.content_link = 'https://www.googleapis.com/youtube/v3/videos?id=%s&part=snippet,contentDetails,statistics,status&'
        #self.content_link = 'https://www.googleapis.com/youtube/v3/search?id=%s&part=contentDetails&'
        self.link ='https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=ankara+pavyon&type=video&key=' + API_KEY
    def playlit(self,vid):                                         
        
             
            session = requests.Session()
            session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
            video_ids = [] 
            append = {'url': vid}
            self.list.append(append)
            u = [range(0, len(self.list))[i:i+50] for i in range(len(range(0, len(self.list))))[::50]]
            u = [','.join([self.list[x]['url'] for x in i]) for i in u]
            u = [self.content_link % i +'key='+ API_KEY for i in u]
            u = u[0]
            logger.info("uu_i: %s" % str(u))
            r =  get_initial_data(session, self.link)
            data = json.loads(r)
            logger.info("data_: %s" % str(data)) 
            j = data['items'][0]
            k = j['contentDetails']['duration']

            video_ids.append(k)
            video_ids = video_ids[0]
            duration=datetime_parser.parse(video_ids)
            return  str(duration)
            
           # return duration
    
    
    def youtubeHtml(self,sUrl):  # S'occupe des requetes
       # Host ='www.youtube.com'
        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        headers = {"User-Agent": UA}
        req = urllib2.Request(sUrl, None, headers)
        try:
            response = urllib2.urlopen(req)
        except UrlError as e:
            print(e.read())
            print(e.reason)

        data = response.read()
        head = response.headers
        response.close()
        return to_utf8(data )

    def thread(self, url):
        try:
            logger.info("url_: %s" % str(url)) 
            result = self.youtubeHtml(url)
            logger.info("result_: %s" % str(result)) 
           
        except:
            return result 
          
