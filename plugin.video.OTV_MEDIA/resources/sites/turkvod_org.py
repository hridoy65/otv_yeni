#-*- coding: utf-8 -*-
  
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.tools import logger, cParser
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.gui.gui import cGui
from resources.sites.LIVETV2 import *
# -*- coding: utf-8 -*-
import sys, os, re, codecs, xbmcplugin, xbmcgui, xbmcaddon, xbmc, xbmcvfs, threading, webbrowser
import json, hashlib, os.path, time, inspect, codecs
from contextlib import closing
from xbmcvfs import File
from resources.scripts import parsers

import re, re, sys, os 
import urllib as urllib2
import xbmcplugin, xbmcgui

import codecs
import xbmcaddon
import xbmc
#from resources.lib.player import cPlayer
# -*- coding: utf-8 -*-
import os
import xbmc, xbmcaddon, xbmcplugin
import xbmcgui
import sys
import time
import re
import traceback
import threading
import socket

from resources.lib.gui import TURKvodKodiPrsr
TURKVOD_PARSER = TURKvodKodiPrsr.turkvod_parsers()
TRModules = TURKvodKodiPrsr.modules()


addonId ='plugin.video.OTV_MEDIA'
MOVIE_COMMENTS = (True, 'showplayer')
SITE_IDENTIFIER = 'turkvod_org'

mac =  'showplayer'

         
s_key=  'showplayer'
#mac =  "plugin.video.turkvod_9.17"	   
	   
addon = xbmcaddon.Addon(id=addonId)
adultPIN = addon.getSetting("adultPIN")       
adultPINonoff = addon.getSetting( "adultPINonoff" )
serverId = addon.getSetting( "serverId" )
listegorunumu = addon.getSetting( "listegorunumu" )

if addon.getSetting('serverId') == "true":
    server = 'me'
else:
    server = 'xyz'
if addon.getSetting('listegorunumu') == "true":
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
else:
    pass
#Host = 'http://mylist.obovse.ru/top?type=list'
def to_utf8(dct):
    if isinstance(dct, dict):
        return dict((to_utf8(key), to_utf8(value)) for key, value in dct.items())
    elif isinstance(dct, list):
        return [to_utf8(element) for element in dct]
    elif isinstance(dct, unicode):
        dct = dct.encode("utf8")
        if PY3: dct = dct.decode("utf8")
        return dct
    elif PY3 and isinstance(dct, bytes):
        return dct.decode('utf-8')
    else:
        return dct
settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')                                           

vidName = 'seyirTURK'
#vidName = xbmcaddon.Addon(vidName).getAddonInfo('name')
logger.info('vidName>%s' % vidName)
dialog = xbmcgui.Dialog()
if settings.getSetting('uclugorunum') == "true":
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
ttc = hashlib.md5(vidName.encode()).hexdigest()
tc ='b106dc966238b027c5fc2af0327f6280'

def TUrKVod():
    oGui = cGui()     
                    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://cekke.tk/sey/kodi/filmler.php?ct=b106dc966238b027c5fc2af0327f6280')
    oGui.addDir('seyiret', 'Basla','Sinema', '720logo.png', oOutputParameterHandler)

    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    params.addParameter('siteUrl', 'TRModules@https://720pizle.org/@start@720pizle')
    oGui.addDir(SITE_IDENTIFIER,'Liste', '720pIzle', '720logo.png', params)

    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')
    params.addParameter('siteUrl', 'TRModules@https://www.filmmodu.org@start@filmmodu')
    oGui.addDir('filmmodu_org','filmmodu', 'Filmmodu.org', 'filmizlesene.png', params)
                            
    params = cOutputParameterHandler()
    params.addParameter('siteUrl', 'TRModules@https://www.hdfilmcehennemi.net@start@hdfilmcehennemi')
    params.addParameter('sMovieTitle', 'Hdfilmcehennemi izle')

    oGui.addDir(SITE_IDENTIFIER,'Liste', 'Hdfilmcehennemi', 'hdfilmcehennemi1.png', params)
    params = cOutputParameterHandler()
    params.addParameter('siteUrl', 'TRModules@https://www.hdfilmcehennemi.net@start@hdfilmcehennemi')
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    oGui.addDir('bicaps_net','bicaps', 'Fullhdfilmizlesene', 'hdfilmcehennemi1.png', params)

    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    params.addParameter('siteUrl', 'TRModules@https://filmmakinesi.net/@start@filmmakinesi')
    oGui.addDir(SITE_IDENTIFIER,'Liste', 'FilMakinesi', 'logo-mobil-responsive.png', params)
    
    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    params.addParameter('siteUrl', 'TRModules@https://jetfilmizle.live/@start@jetfilmizle')
    oGui.addDir('jetfilmizle_biz','jetfilmizle', 'JetFilmizle', 'jetimages.jpg', params)
    
    params =  cOutputParameterHandler()
   # params.addParameter('sMovieTitle', 'BolumD dizi izle')

    #params.addParameter('siteUrl', 'https://orhan.live/')
    oGui.addDir('koreanturk_com','koreanturk', 'Koreantürk Kore Film ve Dizileri', 'ktfooterlogo3.png', params)

    oGui.setEndOfDirectory()
                                                                         


def Liste():
    oGui = cGui() 
    params =  cInputParameterHandler()

    name= params.getValue('sMovieTitle')
    url = params.getValue('siteUrl')

    if "/aramalar/" in url and 'aramalar_list.php' not in url:
        Ara(url)
    if "TEXT" in name:
        ModuldeAra(url)
    if "TURKvod%20HAKKINDA" in name or "TURKvod%20AYARLAR" in name or "ADULT" in name or "XXX" in name or "%2b18" in name or "erotik" in url or "yetiskin" in url or "Erotik" in url or "Yetiskin" in url:
        if adultPINonoff == "true":			
            if path.exists("/usr/lib/enigma2/python/Plugins/Extensions/KodiLite"):
                pin = adultPIN
                if pin != "1234":
                    return
            else:            
                k = xbmc.Keyboard('', 'PIN i giriniz') ; k.doModal()
                pin = k.getText() if k.isConfirmed() else None
                if pin != adultPIN:
                    return
        if adultPINonoff == "false":
            pass
    else:
        pass
		
    if url.endswith(".m3u") or "type=m3u" in url:
        content = Url_Al(url, mac)
        regexcat = 'EXTINF.*?,(.*?)\\n(.*?)\\n'
        match = re.compile(regexcat,re.DOTALL).findall(content)
        for name, url in match:
            name = name.replace("\n", "")
            name = name.replace("\r", "")
            url = url.replace(" ", "")
            url = url.replace("\n", "")
            url = url.replace("\r", "")
            pic = ""
            ListeyeEkle(name, {"name":name, "url":url, "mode":3}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)
		
    if "TRModules" in url:
        try:
    


            url = url.replace('TRModules@', '')
            logger.info("Good TRModules- :" +url )
            iptv_list_temp = TRModules.get_list(url)
            next_page_url = TRModules.next_page_url                  
            next_page_text = TRModules.next_page_text
            prev_page_url = TRModules.prev_page_url
            prev_page_text = TRModules.prev_page_text
            search_text = TRModules.search_text
            search_on = TRModules.search_on
            playlistname = TRModules.playlistname
            content = iptv_list_temp
            oGui = cGui() 
            if "@start" in url or "@category" in url or "@film" in url: 
                for trm in range(len(content)): 
                    name_s = content[trm][1]
                    url_s = content[trm][5]
                    if content[trm][7] == None:
                        pic = ''
                    else:
                        pic = content[trm][7]
                    if content[trm][2] == None:
                        description = ''
                    else:
                        description = content[trm][2]
                    param= cOutputParameterHandler()
                    param.addParameter('siteUrl', url_s)
                    logger.info("Good url_s :" +url_s )
                    param.addParameter('sMovieTitle',name_s)
                    oGui.addMovie(SITE_IDENTIFIER, 'Liste', name_s, pic, pic, description, param)
          
            if "@parts" in url: 
                for trm in range(len(content)):
                    #logger.info("Good url_s :" +url_s )
                    mode = 'VideoListe'
                    name_p = content[trm][1]
                    url_p = content[trm][4]
                    if url_p == None :
                       url_p = content[trm][5]
                       mode = 'Liste'
                       logger.info("Liste_url_p :" +url_p )
                    if content[trm][7] == None:
                        pic = ''
                    else:
                        pic = content[trm][7]
                    if content[trm][2] == None:
                        description = ''
                    else:
                        description = content[trm][2]
                    param= cOutputParameterHandler()
                    param.addParameter('siteUrl', url_p)
                    logger.info("parts url_p:" +url_p)
                    logger.info("Good name_p :" +name_p )
                    param.addParameter('sMovieTitle',name_p)
                    oGui.addMovie(SITE_IDENTIFIER, mode, name_p, pic, pic, description, param)
            
            if next_page_url :
                name_n = ">>"
                nex_url = next_page_url
                pic = ""
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', nex_url)
                oOutputParameterHandler.addParameter('sMovieTitle', name_n)
                oGui.addDir(SITE_IDENTIFIER,'Liste', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
            oGui.setEndOfDirectory()
        except:
            pass
    else:
        if "AYARLAR" in name:
            addon.openSettings()
            xbmc.executebuiltin('Container.Refresh')
            return
             

class MyPlayer(xbmc.Player):
    def __init__( self, *args, **kwargs ):
        xbmc.Player.__init__( self )
        self.s = 0
        self.isfirst = 1
        self.curPos = 0
            
    def newplay(self, playlist,s,m_id,isFragman,isTv="0",lang= -1):
        self.play(playlist)
        self.s = s
        self.m_id = m_id
        self.isFragman = isFragman
        self.lang = lang
        while self.isPlaying():
            xbmc.sleep(100)
            try:
                self.curPos = int(self.getTime())
            except:
                a=1
            try:
                self.total = int(self.getTotalTime())
            except:
                pass
                
    def __del__(self) :
        self.user_id = int(settings.getSetting( "user_id" ))
        kokd = kok()
        if self.user_id != 0 and self.curPos > 100 and self.m_id !=0 :
            self.mili = self.curPos * 1000
            self.toplam = self.total * 1000
            self.percent = 100*self.mili/self.toplam
            bit = 90
            if isTv == "1":
                bit = 85
            if self.percent > bit:
                self.isDone = '1'
            else:
                self.isDone = '0'
            if  isTv == "0":
                temp_watched = settings.getSetting('temp_watched')
                if str(self.m_id) not in temp_watched:
                    temp_watched += "," + str(self.m_id)
                    settings.setSetting("temp_watched",temp_watched)
                self.ur = kokd + "save.php?type=s&m_id=" + str(self.m_id) +"&mili=" + str(self.mili)
            else:
                self.ur = kokd + "save.php?isTv=1&type=s&&m_id=" + str(self.m_id) +"&mili=" + str(self.mili) + '&isDone=' + self.isDone
            if not self.isFragman:
                page = parsers.fetch(self.ur, head={'User-agent': 'Mozilla/5.0 seyirTURK__KODI',settings.getSetting("key"): settings.getSetting("answer"), 'Connection': 'Close'})
    if ver >= 18:
        def onAVStarted(self):
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            if self.isfirst == 1 :
                self.isfirst = 0
                if self.s !=0 :
                    self.seekTime(self.s)
            self.langs = self.getAvailableAudioStreams()
            if self.lang == 1:
                self.audiostream = int([i for i, elem in enumerate(self.langs) if 'en' in elem][0])
            elif self.lang == 0:
                self.audiostream = int([i for i, elem in enumerate(self.langs) if 'tr' in elem][0])
            self.setAudioStream(self.audiostream)
    else:
        def onPlayBackStarted(self):
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            if self.isfirst == 1 :
                self.isfirst = 0
                if self.s !=0 :
                    self.seekTime(self.s)
            self.langs = self.getAvailableAudioStreams()
            if self.lang == 1:
                self.audiostream = int([i for i, elem in enumerate(self.langs) if 'en' in elem][0])
            elif self.lang == 0:
                self.audiostream = int([i for i, elem in enumerate(self.langs) if 'tr' in elem][0])
            self.setAudioStream(self.audiostream)
             

url=None
name=None
mode=None
desc=None
resim=None
m_id=None
konu=None
isTv = '0'
timestamp = 0

def mVideoListe():
    oGui = cGui() 
    params =  cInputParameterHandler()
    name= params.getValue('sMovieTitle')
    url = params.getValue('siteUrl')
    play_url = TURKVOD_PARSER.get_parsed_link(url)
    if (play_url == []) or (play_url == ""):
        play_url = url
        Oynat(name, url)
    else:
        if type(play_url) == str:
            url = play_url
            Oynat(name, url)
        elif type(play_url) == tuple:
            names = []
            urls = []
            names = play_url[2]
            urls = play_url[1]
            if names == []:
                pic = ""
                url = url
                name = name
                Oynat(name, url)
            else:       
                i = 0
                for name in names:
                    pic = ""
                    url = urls[i]
                    i = i+1
                    Oynat(name, url)
                xbmcplugin.endOfDirectory(thisPlugin)  


def VideoListe():
        oGui = cGui() 
        params =  cInputParameterHandler()
        name= params.getValue('sMovieTitle')
        main_url = params.getValue('siteUrl')
        if  ':ref:' in  main_url:
           main_url= re.findall('host:(.*?):ref:.*?', main_url, re.IGNORECASE)[0]
        logger.info("main_url_:" +main_url)
        url = parsers.parse(main_url)
        logger.info("Video url_:" +url)
        sThumbnail= 'sThumbnail'
        title ='[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name
        liz = xbmcgui.ListItem(title)
        

        liz.setInfo(type='video', infoLabels={'Title':title})
        liz.setArt({'thumb': sThumbnail, 'icon': sThumbnail, 'fanart': sThumbnail})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok    



def Oynat(name=False,url=False):
    url = url.replace('#', '|')
    logger.info("Oynat _url:" +url)
#    name = 'sMovieTitle'
    sThumbnail= 'sThumbnail'
    title ='[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name
    liz = xbmcgui.ListItem(title)

    liz.setInfo(type='video', infoLabels={'Title':title})
    liz.setArt({'thumb': sThumbnail, 'icon': sThumbnail, 'fanart': sThumbnail})
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 

   
   
     



