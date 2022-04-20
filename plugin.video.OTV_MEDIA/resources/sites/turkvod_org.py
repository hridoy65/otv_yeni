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

#from resources.lib.gui import TURKvodKodiPrsr


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
    oGui.addDir('hdfilmcehennemi_com', 'showSearch','ARA', '720logo.png', oOutputParameterHandler)
                    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://cekke.tk/sey/kodi/filmler.php?ct=b106dc966238b027c5fc2af0327f6280')
    oGui.addDir('seyiret', 'Basla','Sinema', '720logo.png', oOutputParameterHandler)

#    params =  cOutputParameterHandler()
#    params.addParameter('sMovieTitle', 'BolumD dizi izle')

#    params.addParameter('siteUrl', 'TRModules@https://720pizle.org/@start@720pizle')
#    oGui.addDir(SITE_IDENTIFIER,'Liste', '720pIzle', '720logo.png', params)

    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')
    params.addParameter('siteUrl', 'TRModules@https://www.filmmodu.org@start@filmmodu')
    oGui.addDir('hdfilmcehennemi2_pw','hdfilmcehennemi2', 'Hdfilmcehennemi 2', 'hdfilmcehennemi1.png', params)
                            
    params = cOutputParameterHandler()
    params.addParameter('siteUrl', 'TRModules@https://www.hdfilmcehennemi.mx@start@hdfilmcehennemi')
    params.addParameter('sMovieTitle', 'Hdfilmcehennemi izle')

    oGui.addDir('hdfilmcehennemi_com','hdfilmcehennemi', 'Hdfilmcehennemi', 'hdfilmcehennemi1.png', params)
    params = cOutputParameterHandler()
    params.addParameter('siteUrl', 'TRModules@https://www.hdfilmcehennemi.net@start@hdfilmcehennemi')
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    oGui.addDir('bicaps_net','bicaps', 'Fullhdfilmizlesene', 'hdfilmcehennemi1.png', params)

    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    params.addParameter('siteUrl', 'TRModules@https://filmmakinesi.pro/@start@filmmakinesi')
    oGui.addDir('filmakinesi_org','filmmakinesi', 'FilMakinesi', 'logo-mobil-responsive.png', params)
    
    params =  cOutputParameterHandler()
    params.addParameter('sMovieTitle', 'BolumD dizi izle')

    params.addParameter('siteUrl', 'TRModules@https://jetfilmizle.live/@start@jetfilmizle')
    oGui.addDir('jetfilmizle_biz','jetfilmizle', 'JetFilmizle', 'jetimages.jpg', params)
    
    params =  cOutputParameterHandler()
   # params.addParameter('sMovieTitle', 'BolumD dizi izle')

    #params.addParameter('siteUrl', 'https://orhan.live/')
    oGui.addDir('koreanturk_com','koreanturk', 'Koreantürk Kore Film ve Dizileri', 'ktfooterlogo3.png', params)

    oGui.setEndOfDirectory()
                                                                         


