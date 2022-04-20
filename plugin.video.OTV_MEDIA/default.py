#-*- coding: utf-8 -*-
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

PY3 = False
from resources.lib.youtube_api.youtube_api import YouTube  
from resources.lib.parser import cParser
try:
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import unquote_plus as Unquote_plus
    from urllib.parse import unquote as Unquote
    from urllib.request import HTTPHandler
    from urllib.request import build_opener
    from urllib.request import install_opener
    from urllib.error import HTTPError
    from urllib.request import Request
    from urllib.request import urlopen
    from html.entities import name2codepoint as n2cp
    PY3 = True; unicode = str; unichr = chr; long = int
except:
    from urllib import urlencode as Urlencode
    from urllib import unquote_plus as Unquote_plus
    from urllib import unquote as Unquote
    from urllib2 import HTTPHandler
    from urllib2 import build_opener
    from urllib2 import install_opener
    from urllib2 import HTTPError
    from urllib2 import Request
    from urllib2 import urlopen
    from htmlentitydefs import name2codepoint as n2cp


from resources.lib.util import urlEncode, Unquote
from resources.lib.util import UnquotePlus, Unquote
from resources.lib.util import QuotePlus
from resources.lib.gui.hoster import cHosterGui
from resources.lib.home import cHome
from resources.lib.gui.guui import cGui
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.comaddon import progress, VSlog, addon, window, xbmc
from resources.lib.util import Quote
try:
    # Python 3.x
    from urllib.parse import urlencode
    from urllib.parse import parse_qs
except ImportError:
    # Python 2.x
    from urllib import urlencode
    from urlparse import parse_qs

import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.lib.config import cConfig
#import j2py
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.cconfig import ccConfig
import   sys, os
from resources.lib import common
from resources.lib.comaddon import addon
from os.path import join
from sys import path
from resources.lib.logger import logger 
addons= addon()
_addonPath_ = common.addonPath
path.append(join(_addonPath_, 'resources', 'lib'))
path.append(join(_addonPath_, 'resources', 'lib', 'gui'))
path.append(join(_addonPath_, 'resources', 'lib', 'handler'))
path.append(join(_addonPath_, 'resources', 'art', 'sites'))
path.append(join(_addonPath_,'resources', 'sites'))
#path.append(join(_addonPath_, 'resources', 'lib', 'youtube_api', 'tube'))
#from resources.lib.youtube_api import default
addons = addon()
class main:                                 
 def __init__(self,argv=None):
    if sys.argv:
        argv = sys.argv
    
    self.parseUrl()
   
    
 

 
 def parseUrl(self):
        #if 'search'and 'play' and  'special'and  'users' and  'config' or 'sign' in param:
             
           #  exec("from resources.lib.youtube_api import tube  ")
       # from resources.lib.about import cAbout
       # cAbout().getUpdate()    
        
        params = ParameterHandler()
        oInputParameterHandler =ParameterHandler()
        
        if (oInputParameterHandler.exist('function')):
            #print 'Debug 3'
            sFunction = oInputParameterHandler.getValue('function')
        else:
            #print 'Debug 4'
            cConfig().log('call load methode')
            sFunction = "load"

        if sFunction == 'setSetting':
            if oInputParameterHandler.exist('id'):
                plugin_id = oInputParameterHandler.getValue('id')
            else:
                return

            if oInputParameterHandler.exist('value'):
                value = oInputParameterHandler.getValue('value')
            else:
                return

            setSetting(plugin_id, value)
            return

        if sFunction == 'setSettings':
            setSettings(oInputParameterHandler)
            return

        if sFunction == 'DoNothing':
            return

        if (oInputParameterHandler.exist('site')):
            sSiteName = oInputParameterHandler.getValue('site')
#            if params.exist('mode'):
#               from resources.sites import adult 
               
            
            if params.exist('playMode'):
               
               from resources.lib.gui.ahoster import HosterGui
               url = False
               playMode = params.getValue('playMode')
               isHoster = params.getValue('isHoster')
               url = params.getValue('url')
               manual = params.exist('manual')
               if ccConfig().getSetting(
                       'hosterSelect') == 'Auto' and playMode != 'jd' and playMode != 'jd2' and playMode != 'pyload' and not manual:
                   HosterGui().streamAuto(playMode, sSiteName, sFunction)
               else:
                   HosterGui().stream(playMode, sSiteName, sFunction, url)
               return             
            
        if (not oInputParameterHandler.exist('site')):
            #mise a jour
            try:
                
                plugins = __import__('resources.lib.about', fromlist=['about']).cAbout()
                function = getattr(plugins, 'getUpdate')
                function()
            except:
                pass
            #charge home
            plugins = __import__('resources.lib.home', fromlist=['home']).cHome()
            function = getattr(plugins, 'load')
            function()
            return


        if (oInputParameterHandler.exist('site')):
            sSiteName = oInputParameterHandler.getValue('site')
            if (oInputParameterHandler.exist('title')):
                sTitle = oInputParameterHandler.getValue('title')
            else: sTitle = "none"

            VSlog('load site ' + sSiteName + ' and call function ' + sFunction)
            #cStatistic().callStartPlugin(sSiteName, sTitle)

            if (isHosterGui(sSiteName, sFunction) == True):
                return

            if (isGui(sSiteName, sFunction) == True):
                return

            if (isFav(sSiteName, sFunction) == True):
                return

            if (isLibrary(sSiteName, sFunction) == True):
                return

            if (isDl(sSiteName, sFunction) == True):
                return

            if (isHome(sSiteName, sFunction) == True):
                return

            if (isTrakt(sSiteName, sFunction) == True):
                return
            

    # If global search is called
            if sSiteName == 'globalSearch':
                oGui = cGui()
                searchterm = False
                if params.exist('searchterm'):
                    searchterm = params.getValue('searchterm')
                searchGlobal(searchterm)

            if sSiteName == 'globalRun':
                __import__('resources.lib.runscript', fromlist=['runscript'])
                # function = getattr(plugins, sFunction)
                # function()
                return

            if sSiteName == 'globalSources':
                oGui = cGui()
                aPlugins = oPluginHandler.getAvailablePlugins(force=True)

                if len(aPlugins) == 0:
                    addons = addon()
                    addons.openSettings()
                    oGui.updateDirectory()
                else:
                    for aPlugin in aPlugins:
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                        icon = 'sites/%s.png' % (aPlugin[1])
                        oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

                oGui.setEndOfDirectory()
                return

            if sSiteName == 'globalParametre':
                addons = addon()
                addons.openSettings()
                return
            # if isAboutGui(sSiteName, sFunction) == True:
                # return

            
            try:
                        

                        plugins = __import__('resources.sites.%s' %sSiteName, fromlist=[sSiteName])
                        function = getattr(plugins, sFunction)
                        function()


            except Exception as e:
                progress().VSclose()  # Referme le dialogue en cas d'exception, sinon blocage de Kodi
                VSlog('could not load site: ' + sSiteName + ' error: ' + str(e))
                import traceback
                traceback.print_exc()
                return



def setSetting(plugin_id, value):
    addons = addon()
    setting = addons.getSetting(plugin_id)

    if setting != value:
        addons.setSetting(plugin_id, value)
        return True

    return False
               
def setSettings(oInputParameterHandler):
    addons = addon()

    for i in range(1, 100):
        plugin_id = oInputParameterHandler.getValue('id' + str(i))
        if plugin_id:
            value = oInputParameterHandler.getValue('value' + str(i))
            value = value.replace('\n', '')
            oldSetting = addons.getSetting(plugin_id)
            # modifier si différent
            if oldSetting != value:
                addons.setSetting(plugin_id, value)

    return True
       
        
def isHosterGui(sSiteName, sFunction):
    if (sSiteName == 'cHosterGui'):
        oHosterGui = cHosterGui()
        exec("oHosterGui."+ sFunction +"()")
        return True
    return False
    
def isGui(sSiteName, sFunction):
    if (sSiteName == 'cGui'):
        oGui = cGui()
        exec("oGui."+ sFunction +"()")
        return True
    return False
    
def isFav(sSiteName, sFunction):
    if (sSiteName == 'cFav'):
        from resources.lib.favourite import cFav
        oFav = cFav()
        exec("oFav."+ sFunction +"()")
        return True
    return False
    
def isLibrary(sSiteName, sFunction):
    if (sSiteName == 'cLibrary'):
        from resources.lib.library import cLibrary
        oLibrary = cLibrary()
        exec("oLibrary."+ sFunction +"()")
        return True
    return False

def isDl(sSiteName, sFunction):
    if (sSiteName == 'cDownload'):
        from resources.lib.download import cDownload
        oDownload = cDownload()
        exec("oDownload."+ sFunction +"()")
        return True
    return False

def isHome(sSiteName, sFunction):
    if (sSiteName == 'cHome'):
        oHome = cHome()
        exec("oHome."+ sFunction +"()")
        return True
    return False
def isTrakt(sSiteName, sFunction):
    if sSiteName == 'cTrakt':
        from resources.lib.trakt import cTrakt
        oTrakt = cTrakt()
        exec ("oTrakt." + sFunction + "()")
        return True
    return False

def searchGlobal(sSearchText=False):
    from resources.lib.handler.pluginHandler1 import cPluginHandler
    import threading
    oGui = cGui()
    oGui.globalSearch = True
    oGui._collectMode = True
    if not sSearchText:
        sSearchText = oGui.showKeyBoard()
    if not sSearchText: return True
    aPlugins = []
    aPlugins = cPluginHandler().getAvailablePlugins()
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', 'Searching...')
    numPlugins = len(aPlugins)
    threads = []
    for count, pluginEntry in enumerate(aPlugins):
        #if not pluginEntry['globalsearch']:
            #continue
        dialog.update((count + 1) * 50 // numPlugins, 'Searching: ' + str(pluginEntry['name']) + '...')
        if dialog.iscanceled(): return
        if sys.version_info[0] == 2:
            logger.info('Searching for %s at %s' % (sSearchText.decode('utf-8'), pluginEntry['id']))
        else:
            logger.info('Searching for %s at %s' % (sSearchText, pluginEntry['id']))

        t = threading.Thread(target=_pluginSearch, args=(pluginEntry, sSearchText, oGui), name=pluginEntry['name'])
        threads += [t]
        t.start()
    for count, t in enumerate(threads):
        if dialog.iscanceled(): return
        t.join()
        dialog.update((count + 1) * 50 // numPlugins + 50, t.getName() + ' returned')
    dialog.close()
    # deactivate collectMode attribute because now we want the elements really added
    oGui._collectMode = False
    total = len(oGui.searchResults)
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', 'Gathering info...')
    for count, result in enumerate(sorted(oGui.searchResults, key=lambda k: k['guiElement'].getSiteName()), 1):
        if dialog.iscanceled(): return
        oGui.addFolder(result['guiElement'], result['params'], bIsFolder=result['isFolder'], iTotal=total)
        dialog.update(count * 100 // total, str(count) + ' of ' + str(total) + ': ' + result['guiElement'].getTitle())
    dialog.close()
    oGui.setView()
    oGui.setEndOfDirectory()
    return True


def _pluginSearch(pluginEntry, sSearchText, oGui):
    try:
        #plugin = __import__('sites.%s' % pluginEntry, fromlist=[pluginEntry])
        plugin = __import__(pluginEntry[1], globals(), locals())
        function = getattr(plugin, '_search')
        function(oGui, sSearchText)
    except:
        logger.error(pluginEntry[0] + ': search failed')
        import traceback
        logger.debug(traceback.format_exc())


def encode_log(message=""):
    # Unicode to utf8
    if type(message) == str:
        message = message.encode("utf8")

    # All encodings to utf8
    elif type(message) == str:
        message = str(message, "utf8", errors="replace").encode("utf8")

    # Objects to string
    else:
        message = str(message)

    return message


def get_caller(message=None):
    module = inspect.getmodule(inspect.currentframe().f_back.f_back)

    # En boxee en ocasiones no detecta el modulo, de este modo lo hacemos manual
    if module is None:
        module = ".".join(os.path.splitext(inspect.currentframe().f_back.f_back.f_code.co_filename.split("streamondemand")[1])[0].split(os.path.sep))[1:]
    else:
        module = module.__name__

    function = inspect.currentframe().f_back.f_back.f_code.co_name

    if module == "__main__":
        module = "OTV_MEDIA"
    else:
        module = "OTV_MEDIA." + module
    if message:
        if module not in message:
            if function == "<module>":
                return module + " " + message
            else:
                return module + " [" + function + "] " + message
        else:
            return message
    else:
        if function == "<module>":
            return module
        else:
            return module + "." + function       

from resources.lib.youtube_api.kodion.impl import Context
context = Context(plugin_id='plugin.video.OTV_MEDIA')                                                     
                                                          
plugin_path = context.get_path()
plugin_path = str(plugin_path).replace('/channel/', '/search/channel/').replace('/play/', '/search/').replace('/special/', '/search/').replace('/location/', '/search/').replace('/users/', '/search/').replace('/sign/', '/search/')
logger.info("plugin_path: %s" % str(plugin_path ))
if  '/search/' in plugin_path:
  	from resources.lib.youtube_api import default
            #name='video_id'                                             
#  	        v_id = plugin_param['video_id']                                                
# or '/youtube/' 	        vidbox(v_id)                                                                                                                                                  
plugin_param = context.get_params()
logger.info("param-: %s" % str(plugin_param))                                                                                                                 
params= get_params()
logger.info('params-- %s' % (params))
if  'isTv'in params :
   from resources.sites.seyiret import *
 
if  'adult'in params :
   from resources.sites.adult import *

sys.exit(main())
