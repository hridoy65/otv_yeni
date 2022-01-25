#-*- coding: utf-8 -*-
import urllib
import os
import json
from resources.sites.LIVETV2 import *
import xbmc,xbmcaddon
from resources.lib.common import addonPath, profilePath

import sys
from .peewee import SqliteDatabase, Model, IntegerField, TextField, chunked, fn, JOIN

db = SqliteDatabase(None, pragmas={"foreign_keys": 1})


## Android K18 ZIP Fix.
if sys.version_info[0] == 2:
    from xbmc import translatePath, LOGNOTICE, LOGERROR, log, executebuiltin, getCondVisibility, getInfoLabel
else:
    from xbmc import LOGINFO as LOGNOTICE, LOGERROR, log, executebuiltin, getCondVisibility, getInfoLabel
    from xbmcvfs import translatePath
# Android K18 ZIP Fix.
if getCondVisibility('system.platform.android') and int(getInfoLabel('System.BuildVersion')[:2]) == 18:
    import fixetzipfile as zipfile
else:
    import zipfile


import requests
from resources.lib.comaddon import addon, progress, dialog, xbmcgui, window, VSlog, xbmc
from resources.lib.handler.requestHandler import cRequestHandler

import urllib
import xbmcvfs
import datetime, time
from resources.lib.config import cConfig
try:
    import json
except:
    import simplejson as json
from resources.lib import ziptools
SITE_IDENTIFIER = 'about'
SITE_NAME = 'About'

AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString
AddonName = Addon.getAddonInfo("name")
icon = Addon.getAddonInfo('icon')
addon_version = Addon.getAddonInfo('version')
addonDir = Addon.getAddonInfo('path')
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
#from resources.lib.handler.pluginHandler import cPluginHandler

ROOT_DIR = addonPath
ADDON_DIR = os.path.abspath(os.path.join(ROOT_DIR, '..'))
XSTREAM_DIRNAME = os.path.basename(ROOT_DIR)
AddonID = 'plugin.video.OTV_MEDIA'
addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ), AddonID)

import xbmcgui
# import urllib2
import socket
#from resources.lib import kodi
import time

try:
    from urllib.request import urlopen, Request  # python 3.x
except ImportError:
    from urllib2 import urlopen, Request  # python 2.x

class MyException(Exception):
    pass
def message(text1, text2="", text3=""):
    if text3 == "":
        xbmcgui.Dialog().ok(text1, text2)
    elif text2 == "":
        xbmcgui.Dialog().ok("", text1)
    else:
        xbmcgui.Dialog().ok( text2, text3)

def download(url, dest, dp = None,timeout = None):
    if not timeout:
        timeout = 120

    try:
        if not dp:        
            dp = xbmcgui.DialogProgress()
            dp.create("Status...","Checking Installation",' ', ' ')
        dp.update(0)
        start_time = time.time()
        u = urlopen(url, timeout=timeout)
        h = u.info()
        totalSize = int(h["Content-Length"])
        fp = open(dest, 'wb')
        blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
        count = 0
        while True:  # and (end - start < 15):
            if time.time() - start_time > timeout:
                message("Slow or no Download available:", 'Files could not be downloaded at this time',
                             'Please try again later, Attempting to continue...')
                break
            chunk = u.read(blockSize)
            if not chunk: break
            fp.write(chunk)
            count += 1
            if totalSize > 0:
                try:
                    percent = int(count * blockSize * 100 / totalSize)
                    dp.update(percent)
                except:
                    percent = 100
                    dp.update(percent)
                if dp.iscanceled():
                    dp.close()
                    raise Exception("Canceled")
        timetaken =  time.time() - start_time
#        kodi.log('Duration of download was %.02f secs ' % timetaken )
        logger.info('Duration of download was %.02f secs ' % timetaken )
    # except socket.timeout as e:
    except Exception as e:
        # For Python 2.7
        message("There was an error: %r" % e, 'Files could not be downloaded at this time', 'Please try again later, Attempting to continue...')
        return
    except Exception as e:
        message("There was an error:", str(e),'Please try again later, Attempting to continue...')
        return





def DownloaderClass(url,dest):
    
    dp = xbmcgui.DialogProgress()
    dp.create("OTV_MEDIA-Downloading File",url)
    download(url,dest,dp)
    DB = os.path.join( dest)
    db.init(DB)
    db.connect()


dinamic_url = "https://netcologne.dl.sourceforge.net/project/e2-orhantv1/plugin.video.OTV_MEDIA.zip"

0
## Filename of the update File.
LOCAL_NIGHTLY_VERSION = os.path.join(profilePath, "orhantv_sha")

LOCAL_FILE_NAME_XSTREAM = 'update_orhantv.zip'


def zipfolder(foldername, target_dir):
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
    zipobj.close()

class cAbout:
    
#    def __init__(self):
		    #self.__oSettings = xbmcaddon.Addon(self.getPluginId())
    

      
    def getUpdate(self):
		
        sUrl = 'https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/version'
#        data = urllib2.urlopen(sUrl).read()
#        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = getHtml(sUrl)
        tag_publicada = re.findall('"tag_name": "(.*?)"', sHtmlContent)[0]
        version_yen = re.findall('"tag_name": "(.*?)"', sHtmlContent)[0]
        version_local =Addon.getAddonInfo('version')
        logger.info("version_local %s" %version_local)
        logger.info("version_yen %s" %version_yen)
        if (version_yen > version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/lastupdate.zip'                
            UPDATE_URL = 'https://github.com/orhantv/otv_media/raw/master/plugin.video.OTV_MEDIA/plugin.video.OTV_MEDIA-' + version_yen + '.zip'
            xbmc.log('START DOWNLOAD UPDATE:' + UPDATE_URL)
                
            DownloaderClass(UPDATE_URL,dest)  
                  
            
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                
            line7 = 'New version installed .....'
            line8 = 'Version: ' + tag_publicada 
            xbmcgui.Dialog().ok('OTV_MEDIA-'+ line7, line8)
                
            if os.remove( dest ):
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.sleep(1500)


        if (version_yen > version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/temp.zip'  
            from urllib.request import urlretrieve        
            urlretrieve(UPDATE_URL,dest)
            xbmc.log('START DOWNLOAD PARTIAL UPDATE: OTV_MEDIA' ) 
                    
            
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                    
            line7 = 'New version installed .....'
            line8 = 'Version: ' + tag_publicada 
            xbmcgui.Dialog().ok('OTV_MEDIA-'+ line7, line8)
                    
            if os.remove( dest ): 
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            u = False
        else:
            xbmc.log('No partial updates are available' )
            u = True
                        
