#-*- coding: utf-8 -*-


import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    # noinspection PyShadowingBuiltins
    unichr = chr
    # noinspection PyShadowingBuiltins
    unicode = str
    # noinspection PyShadowingBuiltins
    basestring = str
else:
    # noinspection PyUnresolvedReferences
    import __builtin__
    # noinspection PyShadowingBuiltins
    unichr = __builtin__.unichr
    # noinspection PyShadowingBuiltins
    unicode = __builtin__.unicode
    # noinspection PyShadowingBuiltins
    basestring = __builtin__.basestring

from resources.lib.logger import logger 
from resources.lib.config import cConfig
from base64 import b64encode, b64decode
import xbmc, xbmcplugin, xbmcgui, xbmcaddon
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.guui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler3 import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
from itertools import chain
from resources.lib.gui.guuiElement import cGuiElement
from resources.lib.unwise import unwise_process
from resources.lib.packer import cPacker
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.util import cUtil, Quote
from resources.modules import control, client
import  urllib
import re
import os
import base64
import sys
import time
import os.path
import six
from six.moves import urllib_parse
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
try:  # Python 2
    import urllib2

except ImportError:  # Python 3
    import urllib.request as urllib2

from resources.scripts import parsers
from resources.lib.user_agent import generate_user_agent, generate_navigator
#from pprint import pprint
# Ü / Ãœ
# S / Å
# G / Ä
# Ç / Ã‡
# I / Ä°
# Ö / Ã–

# ü / Ã¼
# s / ÅŸ
# g / ÄŸ
# ç / Ã§
# i / Ä±
# ö / Ã¶

try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

try:
    import ssl
    import socket
    timeout = 30
    socket.setdefaulttimeout(timeout)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
except ImportError:
    pass
try:
    import json
    import math
    import httplib
except:
    pass
try:
    import http.cookiejar as cookielib
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import unquote_plus as Unquote_plus
    from urllib.parse import unquote as Unquote
    from urllib.parse import quote 
    from urllib.parse import urlparse 
    from urllib.parse import urljoin 
    from urllib.parse import parse_qsl 
    from urllib.parse import parse_qs 
    from html.parser import HTMLParser
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPHandler
    from urllib.request import install_opener
    PY3 = True; unicode = str; unichr = chr; long = int
except:
    import cookielib
    from HTMLParser import HTMLParser
    from urllib import urlencode as Urlencode
    from urllib import unquote_plus as Unquote_plus
    from urllib import unquote as Unquote
    from urllib import quote 
    from urlparse import urlparse 
    from urlparse import urljoin 
    from urlparse import parse_qsl 
    from urlparse import parse_qs 
    from urllib2 import Request    
    from urllib2 import urlopen
    from urllib2 import HTTPCookieProcessor
    from urllib2 import build_opener
    from urllib2 import HTTPBasicAuthHandler
    from urllib2 import HTTPHandler
    from urllib2 import install_opener  
    
import re, sys
from resources.modules.log_utils import log
try:
	from urllib.parse import urlparse, quote_plus, urlencode
except:
	from urlparse import urlparse
	from urllib import quote_plus, urlencode
from resources.lib.epg import cePg
from resources.lib.player import cPlayer
from datetime import datetime
import re,xbmcgui,unicodedata
import json, base64
import requests
import string
import random
import time
import uuid
from resources.lib.comaddon import progress, addon, dialog, VSupdate, xbmc, isMatrix, VSlog
#from hashlib import md5

#from sqlite3 import dbapi2 as sqlite
import re
import io

import datetime


import urllib as urllib2
import requests
import datetime
from datetime import timedelta
import sys
import os
import io
import time
import json
import requests
import datetime

try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

s = requests.Session()
#try:
#    reload  # Python 2.7
#except NameError:
#    try:
#        import  xiptvozel
#        from importlib import reload  # Python 3.4+
#        reload(xiptvozel)
#    except ImportError:
#        from imp import reload
try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath
from resources.lib.handler.pluginHandler import cPluginHandler
sPluginPath = cPluginHandler().getPluginPath()

UA = generate_user_agent()

#AddonID = 'plugin.video.OTV_MEDIA'
#addon = xbmcaddon.Addon(AddonID)
videolist = []
qualitylist = []
linkler = []
kaynaklar = []
searchKey = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
oParser = cParser()
timestamp = time.time()
modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(timestamp)) 

cdir = os.path.join(xbmc.translatePath("special://temp"),"files")
def info(texto=""):
    if texto:
        xbmc.log(texto)
addonId = "plugin.video.OTV_MEDIA"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
PROPERTY_SESSION_COOKIE = 'oklivetv.cookie'

try:
    from os import path, system
    if not path.exists(dataPath):
        cmd = "mkdir -p " + dataPath
        system(cmd)
except:
    pass


try:  # Python 2
    import urllib2
    from urllib2 import URLError as UrlError

except ImportError:  # Python 3
    import urllib.request as urllib2
    from urllib.error import URLError as UrlError

def SetCookie(vurl):
        ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',vurl)
        Referer='https://' +ref

        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        headers = {"User-Agent": UA}
        req = urllib2.Request(vurl, None, headers)
        try:
            response = urllib2.urlopen(req)
        except UrlError as e:
            print(e.read())
            print(e.reason)

        data = response.read()
        head = response.headers
        response.close()

        # get cookie
        cookies = ''
        if 'Set-Cookie' in head:
            oParser = cParser()
            sPattern = '(?:^|,) *([^;,]+?)=([^;,\/]+?);'
            aResult = oParser.parse(str(head['Set-Cookie']), sPattern)
            # print(aResult)
            if (aResult[0] == True):
                for cook in aResult[1]:
                    cookies = cookies + cook[0] + '=' + cook[1] + ';'

                    return cookies

def _substitute_entity(match):
        ent = match.group(3)
        if match.group(1) == '#':
            # decoding by number
            if match.group(2) == '':
                # number is in decimal
                return unichr(int(ent))
            elif match.group(2) == 'x':
                # number is in hex
                return unichr(int('0x' + ent, 16))
        else:
            # they were using a name
            cp = n2cp.get(ent)
            if cp: return unichr(cp)
            else: return match.group()


def gegetUrl(url, cookieJar=None,post=None, timeout=20, headers=None):
    
    cookie_handler = HTTPCookieProcessor(cookieJar)
    opener =build_opener(cookie_handler, HTTPBasicAuthHandler(), HTTPHandler())
#    opener = urllib2.install_opener(opener)
    req = Request (url)
    req.add_header('User-Agent',generate_user_agent() )
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    link= to_utf8(link)
    return link;
def decode_hex(data):
    if PY2:
        return str(binascii.b2a_hex(data[::-1]))
    if PY3:
        return (
            binascii.b2a_hex(data[::-1].encode('latin-1'))).decode('latin-1')
def shellcoder(shellcode):
    n = 0
    xshellcode = '\\x'
    for w in shellcode:
        n += 1
        xshellcode += str(w)
        if n is 2:
            n = 0
            xshellcode += str('\\x')
    return xshellcode[:-2]

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
        try:
            return dct.decode('utf-8')
        except:
            return dct.decode('ISO-8859-1')
    else:
        return dct
def _redirectHoster(url):
    try:
        from urllib2 import build_opener, HTTPError
    except ImportError:
        from urllib.error import HTTPError
        from urllib.request import build_opener
    opener = build_opener()
    opener.addheaders = [('Referer', url)]
    try:
        resp = opener.open(url)
        if url != resp.geturl():
            return resp.geturl()
        else:
            return url
    except HTTPError as e:
        if e.code == 403:
            if url != e.geturl():
                return e.geturl()
        raise

def gegetHtml(sUrl, data=None):  # S'occupe des requetes
        ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',sUrl)
        Referer='https://' +ref
      
       # cookies = SetCookie(sUrl)
        from resources.lib.handler.requestHandler import cRequestHandler
        oRequestHandler = cRequestHandler(sUrl)
        oRequestHandler.addHeaderEntry('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        oRequestHandler.addHeaderEntry('Host',ref)
        oRequestHandler.addHeaderEntry('Referer',Referer)
#        oRequestHandler.addHeaderEntry('If-None-Match',' W/"6a0ab883bee2a83697e97ea1f173d852"')
        oRequestHandler.addHeaderEntry('Connection','close')
        data = oRequestHandler.request()
        return to_utf8(data )
       
def getHtml(sUrl, data=None):  
        ref = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',sUrl)
        Referer='https://' +ref
        
        oRequestHandler = cRequestHandler(sUrl)
        oRequestHandler.addHeaderEntry('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        oRequestHandler.addHeaderEntry('Referer',Referer)
        oRequestHandler.addHeaderEntry('Connection','close')
        data = oRequestHandler.request()
        return to_utf8(data )


def getHeaders(BASEURL):
    
    
    cookieProperty = getRawWindowProperty(PROPERTY_SESSION_COOKIE)
    cookies = ('' + urllib_parse.quote_plus(cookieProperty)) if cookieProperty else ''

    return  cookies
def rrequest(url, close=True, redirect=True, error=False, proxy=None, post=None, headers=None, mobile=False, XHR=False, limit=None, referer=None, cookie=None, compression=True, output='', timeout='30'):
    try:
        if not url:
            return

        handlers = []

        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            urllib2.install_opener(opener)


        if output == 'cookie' or output == 'extended' or not close == True:
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            urllib2.install_opener(opener)

        if (2, 7, 8) < sys.version_info < (2, 7, 12):
            try:
                import ssl; ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                handlers += [urllib2.HTTPSHandler(context=ssl_context)]
                opener = urllib2.build_opener(*handlers)
                urllib2.install_opener(opener)
            except:
                pass

        if url.startswith('//'): url = 'http:' + url

        _headers ={}
        try: _headers.update(headers)
        except: pass
        if 'User-Agent' in _headers:
            pass
        elif not mobile == True:
            #headers['User-Agent'] = agent()
            _headers['User-Agent'] = cache.get(randomagent, 1)
        else:
            _headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'Referer' in _headers:
            pass
        elif referer is not None:
            _headers['Referer'] = referer
        if not 'Accept-Language' in _headers:
            _headers['Accept-Language'] = 'en-US'
        if 'X-Requested-With' in _headers:
            pass
        elif XHR == True:
            _headers['X-Requested-With'] = 'XMLHttpRequest'
        if 'Cookie' in _headers:
            pass
        elif not cookie == None:
            _headers['Cookie'] = cookie
        if 'Accept-Encoding' in _headers:
            pass
        elif compression and limit is None:
            _headers['Accept-Encoding'] = 'gzip'


        if redirect == False:

            class NoRedirection(urllib2.HTTPErrorProcessor):
                def http_response(self, request, response): return response

            opener = urllib2.build_opener(NoRedirection)
            urllib2.install_opener(opener)

            try: del _headers['Referer']
            except: pass

        if isinstance(post, dict):
            post = utils.byteify(post)
            post = urllib.urlencode(post)

        url = utils.byteify(url)

        request = urllib2.Request(url, data=post)
        _add_request_header(request, _headers)


        try:
            response = urllib2.urlopen(request, timeout=int(timeout))
        except urllib2.HTTPError as response:

            if response.code == 503:
                cf_result = response.read(5242880)
                try: encoding = response.info().getheader('Content-Encoding')
                except: encoding = None
                if encoding == 'gzip':
                    cf_result = gzip.GzipFile(fileobj=StringIO.StringIO(cf_result)).read()

                if 'cf-browser-verification' in cf_result:

                    netloc = '%s://%s' % (urlparse.urlparse(url).scheme, urlparse.urlparse(url).netloc)

                    if not netloc.endswith('/'):
                        netloc += '/'
                    ua = _headers['User-Agent']

                    cf = cache.get(cfcookie().get, 168, netloc, ua, timeout)

                    _headers['Cookie'] = cf

                    request = urllib2.Request(url, data=post)
                    _add_request_header(request, _headers)

                    response = urllib2.urlopen(request, timeout=int(timeout))
                else:
                    log_utils.log('Request-Error (%s): %s' % (str(response.code), url), log_utils.LOGDEBUG)
                    if error == False: return
            else:
                log_utils.log('Request-Error (%s): %s' % (str(response.code), url), log_utils.LOGDEBUG)
                if error == False: return


        if output == 'cookie':
            try: result = '; '.join(['%s=%s' % (i.name, i.value) for i in cookies])
            except: pass
            try: result = cf
            except: pass
            if close == True: response.close()
            return result

        elif output == 'geturl':
            result = response.geturl()
            if close == True: response.close()
            return result

        elif output == 'headers':
            result = response.headers
            if close == True: response.close()
            return result

        elif output == 'chunk':
            try: content = int(response.headers['Content-Length'])
            except: content = (2049 * 1024)
            if content < (2048 * 1024): return
            result = response.read(16 * 1024)
            if close == True: response.close()
            return result


        if limit == '0':
            result = response.read(224 * 1024)
        elif not limit == None:
            result = response.read(int(limit) * 1024)
        else:
            result = response.read(5242880)

        try: encoding = response.info().getheader('Content-Encoding')
        except: encoding = None
        if encoding == 'gzip':
            result = gzip.GzipFile(fileobj=StringIO.StringIO(result)).read()


        if 'sucuri_cloudproxy_js' in result:
            su = sucuri().get(result)

            _headers['Cookie'] = su

            request = urllib2.Request(url, data=post)
            _add_request_header(request, _headers)

            response = urllib2.urlopen(request, timeout=int(timeout))

            if limit == '0':
                result = response.read(224 * 1024)
            elif not limit == None:
                result = response.read(int(limit) * 1024)
            else:
                result = response.read(5242880)

            try: encoding = response.info().getheader('Content-Encoding')
            except: encoding = None
            if encoding == 'gzip':
                result = gzip.GzipFile(fileobj=StringIO.StringIO(result)).read()

        if 'Blazingfast.io' in result and 'xhr.open' in result:
            netloc = '%s://%s' % (urlparse.urlparse(url).scheme, urlparse.urlparse(url).netloc)
            ua = _headers['User-Agent']
            _headers['Cookie'] = cache.get(bfcookie().get, 168, netloc, ua, timeout)

            result = _basic_request(url, headers=_headers, post=post, timeout=timeout, limit=limit)

        if output == 'extended':
            try: response_headers = dict([(item[0].title(), item[1]) for item in response.info().items()])
            except: response_headers = response.headers
            response_code = str(response.code)
            try: cookie = '; '.join(['%s=%s' % (i.name, i.value) for i in cookies])
            except: pass
            try: cookie = cf
            except: pass
            if close == True: response.close()
            return (result, response_code, response_headers, _headers, cookie)
        else:
            if close == True: response.close()
            return result
    except Exception as e:
        log_utils.log('Request-Error: (%s) => %s' % (str(e), url), log_utils.LOGDEBUG)
        return


class getUrl(object):

    def __init__(self, url, close = True, proxy = None, post = None, headers = None, mobile = False, referer = None, cookie = None, output = '', timeout = '10'):
        if output == 'cookie' or output == 'kukili' or not close == True:
            cookie_handler = HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = build_opener(cookie_handler, HTTPBasicAuthHandler(), HTTPHandler())
            opener = install_opener(opener)
        if not post == None:
            post = Urlencode(post)
            request = Request(url, post)
        else:
            request = Request(url, None)
        if '720pizle' in url or 'bolumd' in url:
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
            request.add_header('Accept', '*/*')
            request.add_header('Accept-Language', 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3')
            request.add_header('Connection', 'keep-alive')
            request.add_header('X-Requested-With', 'XMLHttpRequest')
        else:
            request.add_header('User-Agent', UA)
        if not referer == None:
            request.add_header('Referer', referer)
        if not cookie == None:
            request.add_header('cookie', cookie)
        response = urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'kukili':
            if PY3:
                result = to_utf8(response.read()) + 'kuki :' + str(response.headers.get('Set-Cookie'))
            else:
                result = response.read() + 'kuki :' + str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        elif output == 'lenght':
            result = str(response.headers.get('Content-Length'))
        else:
            result = response.read()
        if PY3:
            result = to_utf8(result)
        if close == True:
            response.close()
        self.result = result


import base64
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    if PY3:    
        data = base64.b64decode(data)
        data = to_utf8(data)
        return data
    else:    
        return base64.decodestring(data)
        
def solveMediaRedirect(url, headers):
    # Use (streamed, headers-only) GET requests to fulfill possible 3xx redirections.
    # Returns the (headers-only) final response, or None.
    while True:
        try:
            mediaHead = requests.get(
                url, stream=True, headers=headers, allow_redirects=False, verify=False, timeout=10
            )
            if 'Location' in mediaHead.headers:
                url = mediaHead.headers['Location'] # Change the URL to the redirected location.
            else:
                mediaHead.raise_for_status()
                return mediaHead # Return the response.
        except:
            return None # Return nothing on failure.

HTML_ENTITY_RE = re.compile(r"&#?\w{0,8};")

def getColor(n):
        if n == '0': n = 'blue'
        elif n == '1': n = 'red'
        elif n == '2': n = 'yellow'
        elif n == '3': n = 'deeppink'
        elif n == '4': n = 'cyan'
        elif n == '5': n = 'lawngreen'
        elif n == '6': n = 'gold'
        elif n == '7': n = 'magenta'
        elif n == '8': n = 'yellowgreen'
        elif n == '9': n = 'white'
        elif n == '10': n = 'black'
        elif n == '11': n = 'crimson'
        elif n == '12': n = 'goldenrod'
        elif n == '13': n = 'powderblue'
        elif n == '14': n = 'deepskyblue'
        elif n == '15': n = 'springgreen'
        elif n == '16': n = 'darkcyan'
        elif n == '17': n = 'aquamarine'
        elif n == '18': n = 'mediumturquoise'
        elif n == '19': n = 'khaki'
        elif n == '20': n = 'darkorange'
        elif n == '21': n = 'none'
        else: n = 'gold'
        return n


def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace('&#8236;','')
    txt = HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    return txt

def OTVDecode(string):
    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+2)] == '\\x':
            c = chr(int(string[(i+2):(i+4)],16))
            i+=3
        if string[i:(i+2)] == '\\u':
            c = chr(int(string[(i+2):(i+6)],16))
            i+=5     
        ret = ret + c
        i += 1

    return ret

def oOTVDecode(string):
    i = 0                                       
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+4)] == '\\x':
            c = chr(int(string[(i+2):(i+4)],16))
            i+=3
        if string[i:(i+2)] == '\\u':
            c = chr(int(string[(i+2):(i+6)],16))
            i+=5     
        ret = ret + c
        i += 1

    return ret.replace("\xdc",'').replace("\xc7",'')
def select(kaynaklar, linkler, tip = 2):
    name = 'Kalite'
    if tip == 1:
        name = 'Kaynak'
    dialog = xbmcgui.Dialog()
    ret = dialog.select('LÃ¼tfen ' + name + ' SeÃ§iniz...',kaynaklar)
    if ret > -1:
        return linkler[ret]
    else:
        return 'selection cancelled'
def bolumdvideos( url,name):
        
            page = getHtml(url)
            
            html = re.findall('<iframe id="video_embed_code" src="([^"]+)"', page, re.IGNORECASE)[0]            
            logger.info("get_bolumd_videos -html: %s" %html)
            pag =getHtml(html) 
            pag=pag.replace("\t",'').replace("\n",'')
            data= re.search('<source src="(.*?)"', pag).group(1)
            logger.info("data: %s" %data)
            name='[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name
               
            addLink(name,  data, '')
  
def addLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 

def alfabekodla(text):
    if PY3:
        text =to_utf8(text)
    def fixup(m):
        text = m.group(0)
        
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('iso-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
import os, string                      

def nalfabekodla(text):
    
    rege = oOTVDecode(text)
    return rege
    logger.info("==text_: %s" %   rege)  

def malfabekodla(text):
    
    rege = OTVDecode(text)
    return rege
    logger.info("==text_: %s" %   rege)  
def xmalfabekodla(text):
   return text if isinstance(text, unicode) else text.decode('utf8')                            # -*- coding:cp1254 -*-
                          
videolist = []
qualitylist = []
linkler = []
kaynaklar = []
def malfabekodlamalfabekodla(string):
    try:
        import chardet
        string = string.decode(chardet.detect(string)["encoding"]).encode("utf-8")
    except:
        pass
    return string
m_id = 0
def omalfabekodla( s ) :
 kem = [ s [ HEM : HEM + 3 ] for HEM in range ( 0 , len ( s ) , 3 ) ]
 return '' . join ( chr ( int ( val ) ) for val in kem )
ver = 18
def kok():
    return settings.getSetting('root')
def m3uCategory(url,Logo=True):
    from resources.lib import comon
    if not comon.check_url(url):
        list = comon.m3u2list(os.path.join(chanDir, url)) 
    else :
        list = comon.cachelist(url,cdir)
    
    playheaders = ""
    
    try:
        surl,playheaders=url.split('|')
    except:
        playheaders = ""
    
    for channel in list:
        name = channel["display_name"]

        if channel.get("tvg_logo", ""): 
            logo = channel.get("tvg_logo", "")
            iconname = "https://kodilive.eu/logo/" + logo
        else :
            iconname = TVICO
        
        if Logo == False:
            if channel.get("tvg_logo", "") and comon.check_url(channel.get("tvg_logo", "")):
                iconname = channel.get("tvg_logo", "")
            else:
                iconname = TVICO
        
        channel["url"] = channel["url"].strip()
        if not playheaders == "":
            channel["url"] = channel["url"] + "|" + playheaders
        
        ext = "." + channel["url"].split(".")[-1]
        EXT = EXTV + EXTA
        if bool(ext in EXT):
            (name,channel["url"],iconname)
        else:
            return (name,channel["url"],iconname)

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
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

           
def oynat(name,url):
    ok = True
    xbmcPlayer = MyPlayer()
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmcPlayer.newplay(url,liz)
    sys.exit()
#'#EXTM3U#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=663283,RESOLUTION=852x480,FRAME-RATE=24.000,CODECS="avc1.4d481f,mp4a.40.2"
#https://cdngate.moly.cloud/579/index/xqx2oaruivokjiqbtfbcp6qoxswwijcmaikrke4hqvxsh4ckcemtpsrk54sa/index-v1-a1.m3u8
def gitm3u8(url):
    if  'moly' in url:
       url = url.replace('/hls/,','/index/').replace(',.urlset/master.m3u8','/index-v1-a1.m3u8')+'|Referer=https://vidmoly.to/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' 
       return url
    Content=getHtml(url)                                                                            
    logger.info("Content: %s" %    Content)
    sHtmlContent = re.findall('#EXT-X-STREAM-.*?BANDWIDTH=.*?,RESOLUTION=.*?x(.*?),.*?\n(.*?)\n', Content, re.S)
    for sTitle,Url  in sHtmlContent:          
            logger.info("Url: %s" % Url)
            qualitylist.append(sTitle)
            videolist.append(Url)
    return select(qualitylist,videolist)
      
 
def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace('&#8236;','')
    txt = HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    return txt
 
 
import json

import xbmcgui


def uppercase(value):
        return ''.join(['[UPPERCASE]', value, '[/UPPERCASE]'])


def color(color, value):
        return ''.join(['[COLOR=', color.lower(), ']', value, '[/COLOR]'])
     