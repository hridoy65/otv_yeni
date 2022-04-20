# -*- coding: utf-8 -*-
import base64
import re
import sys
import six
from six.moves.urllib.parse import urljoin, unquote_plus, quote_plus, quote, unquote
from six.moves import zip
import json
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
from resources.modules import control, client
from resources.sites.LIVETV2 import *
ADDON = xbmcaddon.Addon()
ADDON_DATA = ADDON.getAddonInfo('profile')
ADDON_PATH = ADDON.getAddonInfo('path')
DESCRIPTION = ADDON.getAddonInfo('description')
FANART = ADDON.getAddonInfo('fanart')
ICON = ADDON.getAddonInfo('icon')
ID = ADDON.getAddonInfo('id')
NAME = ADDON.getAddonInfo('name')
VERSION = ADDON.getAddonInfo('version')
Lang = ADDON.getLocalizedString
Dialog = xbmcgui.Dialog()
vers = VERSION
ART = ADDON_PATH + "/resources/icons/"

BASEURL = 'https://sporthd.live/'
Live_url = 'https://1.vecdn.pw/program.php'
headers = {'User-Agent': client.agent(),
           'Referer': BASEURL}

from dateutil.parser import parse
from dateutil.tz import gettz
from dateutil.tz import tzlocal
SITE_IDENTIFIER = 'ssport365'
# reload(sys)
# sys.setdefaultencoding("utf-8")
iconimage = ICON

fanart = FANART
description = DESCRIPTION
query = None
def ASCII(js):                    
              js =  js.replace('65','A')  
              js =  js.replace('66','B') 
              js =  js.replace('67','C') 
              js =  js.replace('68','D') 
              js =  js.replace('69','E') 
              js =  js.replace('70','F')                                                                                                                                                                                                              
              js =  js.replace('71','G') 
              js =  js.replace('72','H')  
              js =  js.replace('73','I')  
              js =  js.replace('74','J')  
              js =  js.replace('75','K')  
              js =  js.replace('76','L')  
              js =  js.replace('77','M')  
              js =  js.replace('78','N') 
              js =  js.replace('79','O') 
              js =  js.replace('80','P') 
              js =  js.replace('81','Q') 
              js =  js.replace('82','R') 
              js =  js.replace('83','S')  
              js =  js.replace('84','T')  
              js =  js.replace('85','U')  
              js =  js.replace('86','V')  
              js =  js.replace('87','W')  
              js =  js.replace('88','X')  
              js =  js.replace('89','Y')  
              js =  js.replace('90','Z') 
              js =  js.replace('91','[')                              
              js =  js.replace('92','\\')
              js =  js.replace('93',']')    
              js =  js.replace('94','^')  
              js =  js.replace('95','_')   
              js =  js.replace('96','`') 
              js =  js.replace('97','a')
              js =  js.replace('98','b') 
              js =  js.replace('99','c')                              
              js =  js.replace('100','d')
              js =  js.replace('101','e')
              js =  js.replace('102','f')
              js =  js.replace('103','g')
              js =  js.replace('104','h')    
              js =  js.replace('105','i') 
              js =  js.replace('106','j')  
              js =  js.replace('107','k')   
              js =  js.replace('108','l')
              js =  js.replace('109','m') 
              js =  js.replace('110','n')
              js =  js.replace('111','o') 
              js =  js.replace('112','p') 
              js =  js.replace('113','q') 
              js =  js.replace('114','r') 
              js =  js.replace('115','s') 
              js =  js.replace('116','t') 
              js =  js.replace('117','u') 
              js =  js.replace('118','v')
              js =  js.replace('119','w')               
              js =  js.replace('120','x')          
              js =  js.replace('121','y')          
              js =  js.replace('122','z')             
              js =  js.replace('123','{')
              js =  js.replace('124','|')
              js =  js.replace('125','}')
              js =  js.replace('126','~')
              js =  js.replace('33','!')
              js =  js.replace('34','"')
              js =  js.replace('35','#')
              js =  js.replace('36','$')
              js =  js.replace('37','%')
              js =  js.replace('38','&')
              js =  js.replace('39',"'")
              js =  js.replace('40','(')
              js =  js.replace('41',')')
              js =  js.replace('42','*')
              js =  js.replace('43','+')
              js =  js.replace('44',',')
              js =  js.replace('45','-')
              js =  js.replace('46','.')
              js =  js.replace('47','/') 
              js =  js.replace('48','0')                
              js =  js.replace('49','1')  
              js =  js.replace('50','2')  
              js =  js.replace('51','3') 
              js =  js.replace('52','4')  
              js =  js.replace('53','5') 
              js =  js.replace('54','6')  
              js =  js.replace('55','7')  
              js =  js.replace('56','8') 
              js =  js.replace('57',"9")   
              js =  js.replace('58',':')    
              js =  js.replace('59',';')   
              js =  js.replace('60','<') 
              js =  js.replace('61','=') 
              js =  js.replace('62','>')               
              js =  js.replace('63','?')   
              js =  js.replace('64','@')
              js =js.replace('[', '').replace(']', '').replace(',', '')
              return js                                                                     

#######################################
# Time and Date Helpers
#######################################
try:
    local_tzinfo = tzlocal()
    locale_timezone = json.loads(xbmc.executeJSONRPC(
        '{"jsonrpc": "2.0", "method": "Settings.GetSettingValue", "params": {"setting": "locale.timezone"}, "id": 1}'))
    if locale_timezone['result']['value']:
        local_tzinfo = gettz(locale_timezone['result']['value'])
except:
    pass


def convDateUtil(timestring, newfrmt='default', in_zone='UTC'):
    if newfrmt == 'default':
        newfrmt = xbmc.getRegion('time').replace(':%S', '')
    try:
        in_time = parse(timestring)
        in_time_with_timezone = in_time.replace(tzinfo=gettz(in_zone))
        local_time = in_time_with_timezone.astimezone(local_tzinfo)
        return local_time.strftime(newfrmt)
    except:
        return timestring
           
              
def Main_menu():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'getevents', 'LIVE EVENTS', 'turkey-free-iptv.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'showGenres', 'SPORTS', 'turkey-free-iptv.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', Live_url)
    oGui.addDir(SITE_IDENTIFIER, 'leaguesmenu', 'BEST LEAGUES', 'turkey-free-iptv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def leaguesmenu():
    oGui = cGui()                           
    liste = []
    liste.append( ['Uefa Champions League','index.php?champ=uefa-champions-league','flags/uefa-champions-league.png'] )
    liste.append( ['Uefa Europa League','index.php?champ=uefa-europa-league','flags/uefa-europa-league.png'] )
    liste.append( ['Premier League','index.php?champ=premier-league','flags/premier-league.png'] )
    liste.append( ['Bundesliga','index.php?champ=bundesliga','flags/bundesliga.png'] )
    liste.append( ['Laliga','index.php?champ=laliga','flags/spanish-primera-division.png'] )
    liste.append( ['Serie A','index.php?champ=serie-a','flags/serie-a.png'] )
    liste.append( ['France Ligue 1','index.php?champ=france-ligue-1','flags/france-ligue-1.png'] )
    liste.append( ['Eredivisie','index.php?champ=eredivisie','flags/eredivisie.png'] )
    liste.append( ['Australian A League','index.php?champ=australian-a-league','flags/australian-a-league.png'] )
    liste.append( ['MLS','index.php?champ=mls','flags/mls.png'] )
    liste.append( ['Rugby Top 14','index.php?champ=rugby-top-14','flags/rugby-top-14.png'] )
    liste.append( ['Greece Super League','index.php?champ=greece-super-league','flags/greece-super-league.png'] )
    liste.append( ['Argentina Superliga','index.php?champ=argentina-superliga','flags/argentina-superliga.png'] )
    liste.append( ['Portuguese Primeira Liga','index.php?champ=portuguese-primeira-liga','flags/portuguese-primeira-liga.png'] )
    liste.append( ['Primera Division Apertura','index.php?champ=primera-division-apertura','flags/primera-division-apertura.png'] )
    liste.append( ['Bundesliga 2','index.php?champ=bundesliga-2','flags/bundesliga-2.png'] )
    liste.append( ['Greece Super League 2','index.php?champ=greece-super-league-2','flags/greece-super-league-2.png'] )
    liste.append( ['Belarus Vysheyshaya Liga','index.php?champ=belarus-vysheyshaya-liga','flags/belarus-vysheyshaya-liga.png'] )
    for sTitle,sUrl,Pic in liste:
        sUrl2= BASEURL +sUrl             
        sPicture= BASEURL + Pic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oGui.addTV(SITE_IDENTIFIER, 'getevents', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
                        
def sportsmenu():
    oGui = cGui()                           
    liste = []
    liste.append( ['Football', 'type=football','images/football.png'] )
    liste.append( ['Basketball','type=basketball', 'images/basketball.png'] )
    liste.append( ['MotorSport','type=motorsport', 'images/motorsport.png'] )
    liste.append( ['Handball','type=handball','images/handball.png'] )
    liste.append( ['Rugby','type=rugby','images/rugby.png'] )
    liste.append( ['NFL','type=nfl','images/nfl.png'] )
    liste.append( ['UFC','type=ufc','images/ufc.png'] )
    liste.append( ['Wrestling','type=wresling','images/wresling.png'] )
    liste.append( ['Hockey','type=hokey', 'images/hockey.png'] )
    liste.append( ['Volleyball','type=volleyball','images/volleyball.png'] )
    liste.append( ['Darts','type=darts','images/darts.png'] )
    liste.append( ['Tennis','type=tennis','images/tennis.png'] )
    liste.append( ['Boxing','type=boxing','images/boxing.png'] )
    liste.append( ['Cricket','type=cricket', 'images/cricket.png'] )
    liste.append( ['Baseball','type=baseball','images/baseball.png'] )
    liste.append( ['Snooker','type=snooker','images/snooker.png'] )
    liste.append( ['Chess','type=chess','images/chess.png'] )
    for sTitle,sUrl,Pic in liste:
        sUrl2= Live_url +sUrl             
        sPicture= BASEURL + Pic
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oGui.addTV(SITE_IDENTIFIER, 'getevents', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def getevents():  # 5
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')

    data = client.request(url)
    # xbmc.log('@#@EDATAAA: {}'.format(data))
    data = six.ensure_text(data, encoding='utf-8', errors='ignore')
    days = list(zip(client.parseDOM(data, 'button', attrs={'class': 'accordion'}),
                    client.parseDOM(data, 'div', attrs={'class': "panel"})))
    # data = client.parseDOM(str(data), 'div', attrs={'class': "panel"})
    # xbmc.log('@#@DAYSSS: {}'.format(str(days)))
    for day, events in days:
        dia = client.parseDOM(day, 'span')[0]
        events = six.ensure_text(events, encoding='utf-8', errors='ignore')
        events = list(zip(client.parseDOM(events, 'div', attrs={'class': "left.*?"}),
                          client.parseDOM(events, 'div', attrs={'class': "containe"})))
        # xbmc.log('@#@EVENTS: {}'.format(str(events)))
    # addDir('[COLORcyan]Time in GMT+2[/COLOR]', '', 'BUG', ICON, FANART, '')
       # addDir(dia, '', '', ICON, FANART, name)
        tevents = []
        for event, streams in events:
            if '\n' in event:
                ev = event.split('\n')
                for i in ev:
                    tevents.append((i, streams))
            else:
                tevents.append((event, streams))

        for event, streams in sorted(tevents):
            # links = re.findall(r'<a href="(.+?)".+?>( Link.+? )</a>', event, re.DOTALL)
            streams = str(quote(base64.b64encode(six.ensure_binary(streams))))

            event = event.encode('utf-8') if six.PY2 else event
            event = '[COLOR gold][B]{}[/COLOR][/B]'.format(event)


            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', str(event))
            oOutputParameterHandler.addParameter('siteUrl', streams)
            oGui.addDir(SITE_IDENTIFIER, 'get_stream', event, 'libretv.png', oOutputParameterHandler)
            #oGui.addMovie(SITE_IDENTIFIER, 'get_stream', event, icon, icon, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                            




def get_stream():  # 4
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    data = base64.b64decode(unquote(url))
    # xbmc.log('@#@DATAAAA:%s' % data, xbmc.LOGINFO)
    if b'info_outline' in data:
        control.infoDialog("[COLOR gold]No Links available ATM.\n [COLOR lime]Try Again Later![/COLOR]", NAME,
                           iconimage, 5000)
        return
    else:
        links = list(zip(client.parseDOM(str(data), 'a', ret='href'), client.parseDOM(str(data), 'a')))
        # xbmc.log('@#@STREAMMMMMSSSSSS:%s' % links, xbmc.LOGINFO)
        titles = []
        streams = []
        for link, title in links:
            streams.append(link)
            titles.append(title)

        if len(streams) > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select('[COLORgold][B]Choose Stream[/B][/COLOR]', titles)
            if ret == -1:
                return
            elif ret > -1:
                host = streams[ret]
                # xbmc.log('@#@STREAMMMMM:%s' % host, xbmc.LOGNOTICE)
                return resolve(host, name)
            else:
                return
        else:
            link = links[0][0]
            return resolve(link, name)


def idle():
    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
    else:
        xbmc.executebuiltin('Dialog.Close(busydialog)')


def busy():
    if float(xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')[:4]) > 17.6:
        xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    else:
        xbmc.executebuiltin('ActivateWindow(busydialog)')


def mresolve(url, name):
    # xbmc.log('RESOLVE-URL: %s' % url, xbmc.LOGNOTICE)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    # dialog.notification(AddonTitle, '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]', icon, 5000)
    if 'acestream' in url:
        url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
        liz = xbmcgui.ListItem(name)
        liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
        liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage,
                    'fanart': fanart})
        liz.setPath(url)
        xbmc.Player().play(url1, liz, False)
        quit()
    if '/live.cdnz' in url:
        r = six.ensure_str(client.request(url, referer=BASEURL)).replace('\t', '')
        # xbmc.log("[{}] - HTML: {}".format(ADDON.getAddonInfo('id'), str(r)))
        from resources.modules import jsunpack
        if 'script>eval' in r:
            unpack = re.findall(r'''<script>(eval.+?\{\}\)\))''', r, re.DOTALL)[0]
            r = jsunpack.unpack(unpack.strip())
            # xbmc.log('RESOLVE-UNPACK: %s' % str(r), xbmc.LOGNOTICE)
        else:
            r = r
        # xbmc.log("[{}] - HTML: {}".format(ADDON.getAddonInfo('id'), str(r)))
        if 'hfstream.js' in r:
            regex = '''<script type='text/javascript'> width=(.+?), height=(.+?), channel='(.+?)', g='(.+?)';</script>'''
            wid, heig, chan, ggg = re.findall(regex, r, re.DOTALL)[0]
            stream = 'https://www.playerfs.com/membedplayer/' + chan + '/' + ggg + '/' + wid + '/' + heig + ''
        else:
            if 'cbox.ws/box' in r:
                try:
                    stream = client.parseDOM(r, 'iframe', ret='src', attrs={'id': 'thatframe'})[0]
                except IndexError:
                    streams = client.parseDOM(r, 'iframe', ret='src')
                    stream = [i for i in streams if not 'adca.' in i][0]
                    # xbmc.log("[{}] - STREAM: {}".format(ADDON.getAddonInfo('id'), str(stream)))
            else:
                stream = client.parseDOM(r, 'iframe', ret='src')[-1]
                # xbmc.log("[{}] - STREAM-ELSE: {}".format(ADDON.getAddonInfo('id'), str(stream)))
        # xbmc.log("[{}] - STREAM: {}".format(ADDON.getAddonInfo('id'), str(stream)))
        rr = client.request(stream, referer=url)
        rr = six.ensure_text(rr, encoding='utf-8').replace('\t', '')
        if 'eval' in rr:
            unpack = re.findall(r'''script>(eval.+?\{\}\))\)''', rr, re.DOTALL)[0]
            # unpack = client.parseDOM(rr, 'script')
            # xbmc.log('UNPACK: %s' % str(unpack))
            # unpack = [i.rstrip() for i in unpack if 'eval' in i][0]
            rr = six.ensure_text(jsunpack.unpack(str(unpack) + ')'), encoding='utf-8')
        else:
            r = rr
        if 'youtube' in rr:
            try:
                flink = client.parseDOM(r, 'iframe', ret='src')[0]
                fid = flink.split('/')[-1]
            except IndexError:
                fid = re.findall(r'''/watch\?v=(.+?)['"]''', r, re.DOTALL)[0]
            # xbmc.log('@#@STREAMMMMM111: %s' % fid, xbmc.LOGNOTICE)

            flink = 'plugin://plugin.video.youtube/play/?video_id={}'.format(str(fid))
            # xbmc.log('@#@STREAMMMMM111: %s' % flink, xbmc.LOGNOTICE)

        else:
            if '<script>eval' in rr and not '.m3u8?':
                unpack = re.findall(r'''<script>(eval.+?\{\}\))\)''', rr, re.DOTALL)[0].strip()
                # xbmc.log("[{}] - STREAM-UNPACK: {}".format(ADDON.getAddonInfo('id'), str(unpack)))
                rr = jsunpack.unpack(str(unpack) + ')')
                # xbmc.log("[{}] - STREAM-UNPACK: {}".format(ADDON.getAddonInfo('id'), str(r)))
            # else:
            #     xbmc.log("[{}] - Error unpacking".format(ADDON.getAddonInfo('id')))
            if 'player.src({src:' in rr:
                flink = re.findall(r'''player.src\(\{src:\s*["'](.+?)['"]\,''', rr, re.DOTALL)[0]
                # xbmc.log('@#@STREAMMMMM: %s' % flink, xbmc.LOGNOTICE)
            elif 'hlsjsConfig' in rr:
                flink = re.findall(r'''src=\s*["'](.+?)['"]''', rr, re.DOTALL)[0]
            elif 'new Clappr' in rr:
                flink = re.findall(r'''source\s*:\s*["'](.+?)['"]\,''', str(rr), re.DOTALL)[0]
            elif 'player.setSrc' in rr:
                flink = re.findall(r'''player.setSrc\(["'](.+?)['"]\)''', rr, re.DOTALL)[0]

            else:
                try:
                    flink = re.findall(r'''source:\s*["'](.+?)['"]''', rr, re.DOTALL)[0]
                except IndexError:
                    ea = re.findall(r'''ajax\(\{url:\s*['"](.+?)['"],''', rr, re.DOTALL)[0]
                    ea = six.ensure_text(client.request(ea)).split('=')[1]
                    flink = re.findall('''videoplayer.src = "(.+?)";''', ea, re.DOTALL)[0]
                    flink = flink.replace('" + ea + "', ea)

            flink += '|Referer={}'.format(quote(stream)) #if not 'azcdn' in flink else ''
        # xbmc.log('@#@STREAMMMMM111: %s' % flink)
        stream_url = flink
    elif '//em.bedsport' in url or 'cdnz.one/ch' in url:
        xbmc.log('@#@STREAMMMMM111: %s' % url)
        referer = 'https://em.bedsport.live/'
        r = six.ensure_str(client.request(url, referer=referer))
        vid = re.findall(r'''fid=['"](.+?)['"]''', r, re.DOTALL)[0] #<script>fid='do4';
        #ragnaru.net/embed.php?player='+embedded+'&live='+fid+'" '+PlaySize+' width='+v_width+' height='+v_height+'
        host = 'https://ragnaru.net/embed.php?player=desktop&live={}'.format(str(vid))
        data = six.ensure_str(client.request(host, referer=referer))
        link = re.findall(r'''return\((\[.+?\])\.join''', data, re.DOTALL)[0]
        xbmc.log('@#@STREAMMMMM111: %s' % link)
        stream_url = link.replace('[', '').replace(']', '').replace('"', '').replace(',', '').replace('\/', '/')
        xbmc.log('@#@STREAMMMMM222: %s' % stream_url)
        stream_url += '|Referer=https://ragnaru.net/&User-Agent={}'.format(quote(ua))
    elif '//bedsport' in url:
        r = six.ensure_str(client.request(url))
        frame = client.parseDOM(r, 'iframe', ret='src')[0]
        r = six.ensure_str(client.request(frame))
        frame = client.parseDOM(r, 'iframe', ret='src')[0]
        data = six.ensure_str(client.request(frame))
        xbmc.log('@#@DATAAA: %s' % data)
        unpack = re.findall(r'''script>(eval.+?\{\}\))\)''', data, re.DOTALL)[0]
        # unpack = client.parseDOM(rr, 'script')
        # xbmc.log('UNPACK: %s' % str(unpack))
        # unpack = [i.rstrip() for i in unpack if 'eval' in i][0]
        from resources.modules import jsunpack
        data = six.ensure_text(jsunpack.unpack(str(unpack) + ')'), encoding='utf-8')
        xbmc.log('@#@DATAAA: %s' % data)
        stream_url = data
    else:
        stream_url = url
    
    liz = xbmcgui.ListItem(name)
    liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
    liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage, 'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("IsPlayable", "true")
    liz.setPath(str(stream_url))
    # if float(xbmc.getInfoLabel('System.BuildVersion')[0:4]) >= 17.5:
    #     liz.setMimeType('application/vnd.apple.mpegurl')
    #     liz.setProperty('inputstream.adaptive.manifest_type', 'hls')
    #     liz.setProperty('inputstream.adaptive.stream_headers', str(headers))
    # else:
    #     liz.setProperty('inputstreamaddon', None)
    #     liz.setContentLookup(True)
    xbmc.Player().play(stream_url, liz, False)
    quit()
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), False, liz)



def Open_settings():
    control.openSettings()

def showGenres():
    oGui = cGui()

    liste = []
    #liste.append(['News', URL_MAIN + 'non-classe/'])
    liste =sportsmenu().categories()
    logger.info("ret1: %s" %str(liste))
    oOutputParameterHandler = cOutputParameterHandler()
    for  sUrl, sTitle,png in liste:
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'shGenres', sTitle, png, oOutputParameterHandler)

    oGui.setEndOfDirectory()
def shGenres():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')

    liste = []
    #liste.append(['News', URL_MAIN + 'non-classe/'])
    liste =sportsmenu().events(url)
    logger.info("ret2: %s" %str(liste))
    oOutputParameterHandler = cOutputParameterHandler()
    for  sUrl, sTitle in liste:
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'howMovies', sTitle,'libretv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()           

def howMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = ''
    #liste.append(['News', URL_MAIN + 'non-classe/'])
    liste =sportsmenu()._links(url)
    if not 'http' in liste: 

        oOutputParameterHandler = cOutputParameterHandler()
        #logger.info("sUrlret3: %s" %str(sUrl))
       # oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
       # oOutputParameterHandler.addParameter('sThumb', sThumb)
        oGui.addDir('youtubecom_tr', 'Searchchannell', sTitle,'libretv.png', oOutputParameterHandler)


                  
           
   
    oOutputParameterHandler = cOutputParameterHandler()
    for  sUrl, sTitle in liste:
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oGui.addDir(SITE_IDENTIFIER, 'showHosters2', sTitle,'libretv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def zresolve():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    liste = oInputParameterHandler.getValue('siteUrl')
    name= oInputParameterHandler.getValue('sMovieTitle')
    urk =info(liste)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'  
		 # data =data.replace("\n",'').replace("\r",'')
    logger.info("ret-: %s" %str(	urk ))
    inf = getHtml(urk)
    flink = re.findall('<iframe src="(.+?)"', inf)[0]
    inffo = getHtml(flink )
    stream = client.parseDOM(inffo, 'iframe', ret='src')[0]
    logger.info("streams: %s" %str(stream))
    stream_url = infom(stream)
    stream_url =stream_url +'|Referer='+stream+'&User-Agent={}'.format(quote(ua))
    logger.info("ret: %s" %str(stream_url))
    liz = xbmcgui.ListItem(name)
    liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
    liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage, 'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("IsPlayable", "true")
    liz.setPath(str(stream_url))
    # if float(xbmc.getInfoLabel('System.BuildVersion')[0:4]) >= 17.5:
    #     liz.setMimeType('application/vnd.apple.mpegurl')
    #     liz.setProperty('inputstream.adaptive.manifest_type', 'hls')
    #     liz.setProperty('inputstream.adaptive.stream_headers', str(headers))
    # else:
    #     liz.setProperty('inputstreamaddon', None)
    #     liz.setContentLookup(True)
    xbmc.Player().play(stream_url, liz, False)
    quit()
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), False, liz)

from resources.modules import webutils, control, cache, linkSearch, constants

# python 2 doesn't support date.datetime.timestamp()
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    # python version < 3.3
    import time
    def timestamp(date):
        return time.mktime(date.timetuple())
else:
    def timestamp(date):
        return date.timestamp()
def livetvHtml(sUrl, data=None):  
        
        oRequestHandler = cRequestHandler(sUrl)
        oRequestHandler.addHeaderEntry('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
        oRequestHandler.addHeaderEntry('Referer','http://livetv.sx/')
        oRequestHandler.addHeaderEntry('Cookie','__utmc=32281891')
        data = oRequestHandler.request()
        return to_utf8(data )
                                          # Cookie: __utmc=32281891;

def info(url):
              
    
    data =getHtml(url)
    sPattern = '<iframe  allowFullScreen="true" scrolling=no frameborder="0 "width="700" height="480" src="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(data, sPattern)
    if (aResult[0] == True):
         return  aResult[1][0]
def infom(url):
              
    
    data =getHtml(url)
    sPattern = "source:'(.+?)'.+?source"
    oParser = cParser()
    aResult = oParser.parse(data, sPattern)
    if (aResult[0] == True):
         return  aResult[1][0]

class sportsmenu():
	def __init__(self, url = ''):
		self.base = 'http://livetv.sx'
		self.search_url = 'http://livetv.sx/enx/megasearch/?msq={}'

	def categories(self):
		import requests
		self.html = requests.get(self.base + '/en/allupcoming').text
		
		cats = re.findall('<tr>\s*<[^<]*<a class="main" href="([^"]*allupcomingsports/(\d+)/)"><img[^>]*src="([^"]+)"></a></td>\s*<td align="left">[^<]*<a[^<]*<b>([^<]*)</b></a>\s*</td>\s*<td width=\d+ align="center">\s*<a [^<]*<b>\+(\d+)</b></a>\s*</td>\s*</tr>', self.html)
		cats = self.__prepare_cats(cats)
		return cats

	def events(self,url):
		import requests
		html = requests.get(url).text
		soup = webutils.bs(html)
		soup = soup.find('table',{'class':'main'})

		events = soup.findAll('td',{'colspan':'2', 'height':'38'})
		events = self.__prepare_events(events)
		return events

	def links(self, url, timeout=int(control.setting('cache_timeout'))):
		#return self._links(url)
		return cache.get(self._links, timeout, url)

	def _links(self,url):
		import requests
		html = requests.get(url).text
		links = re.findall('title\s*=\s*[\"\']([^\"\']*)[^$]+linkflag.+?Kbps.+?>([^<]*).+?\&nbsp;(\d*).+?href\s*=\s*[\"\']([^\"\']+).+?(?:&nbsp.+?>([^<]+))?', html, re.DOTALL)
		links = self.__prepare_links(links)
		if len(links) == 0:
			return []
		titles = {}
		for l in links:
			titles[l[0]] = l[1]

		links = [u[0] for u in links]

		ret = linkSearch.getLinks(links)

		out2 = []
		for u in ret:
			out2.append((u, titles[u]))

		return out2


	@staticmethod
	def convert_time(time,month, day):
		def month_converter(month):
			months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
			return months.index(month) + 1
		li = time.split(':')
		hour,minute=li[0],li[1]
		month = month_converter(month)
		import datetime
		import pytz
		d = pytz.timezone('Europe/London').localize(datetime.datetime(2021 , int(month), int(day), hour=int(hour), minute=int(minute)))
		timezona = control.setting('timezone_new')
		my_location = pytz.timezone(constants.get_zone(int(timezona)))
		convertido=d.astimezone(my_location)
		fmt = "%m/%d %H:%M"
		time=convertido.strftime(fmt)
		return time, timestamp(convertido)
		

	def __prepare_links(self,links):
		new = []
		for link in links:
			streamer_tmp = 'Web'
			url = 'http:' + link[3]
			if 'acestream' in url:
				continue
			health = link[2]
			lang = link[0]
			if u'ð' in lang:
				lang = 'unknown'
			if 'aliez' in url:
				streamer_tmp = 'Aliez'
			if lang == '':
				lang = 'unknown'
			
			bitrate = link[1]
			title = "%s | %s | %s"%(streamer_tmp,lang, bitrate)
			new.append((url,title.replace('ifr','flash')))
			
		return new




	def __prepare_cats(self,cats):
		new = []
		for cat in cats:
			url = self.base + cat[0]
			title = cat[3] + ' (%s)'%cat[4]
			id = self.get_id(cat[3])
			img = 'icons/%s.png'%id
			new.append((url,title,img))

		return new

	def get_id(self,id):
		id = id.lower().replace(' ','_')
		id = id.replace('ice_hockey','hockey').replace('football','soccer').replace('american_soccer','football').replace('rugby_union','rugby').replace('combat_sport','fighting').replace('winter_sport','skiing').replace('water_sports','waterpolo').replace('billiard','snooker')
		return id

	def __prepare_events(self,events):
		new=[]
		for ev in events:
			url = self.base + ev.find('a')['href']
			event = ev.find('a').getText()
			info = ev.find('span', {'class':'evdesc'}).getText()
			try:
				league = re.findall('\((.+?)\)', info)[0]
			except:
				league = ''

			time = re.findall('(\d+:\d+)',info)[0]
			day,month = re.findall('(\d+) (\w+) at',info)[0]
			time, timestamp = self.convert_time(time,month, day)
			color = 'orange'
			if 'live.gif' in str(ev):
				time = '[COLOR red]LIVE[/COLOR]'
			title = u'(%s) [B]%s[/B] - (%s)'%(time, event, league)        
			new.append(((url,title), timestamp))

		new = list(set(new))
		new.sort(key=lambda x: x[1])	
		new = [x[0] for x in new]
		return new

	def resolve(self,url):
		  urk =info(url)
		  
		 # data =data.replace("\n",'').replace("\r",'')
		  logger.info("ret-: %s" %str(	urk ))
		  inf = getHtml(urk)
		  flink = re.findall('<iframe src="(.+?)"', inf)[0]
		  inffo = getHtml(flink )
		  stream = client.parseDOM(inffo, 'iframe', ret='src')[0]
		  logger.info("streams: %s" %str(stream))
		  inff = infom(stream)
		 # flin =  re.findall("source:'(.+?)'.+?source", inff)[0]
		  logger.info("retu: %s" %str(inff))
		  return inff
	
	       
	def search(self, query):
		query = quote_plus(query)
		search_url = self.search_url.format(query)
		import requests
		html = requests.get(search_url).text
		tables = webutils.bs(html).findAll('table')
		table = None
		for i in range(len(tables)):
			if tables[i].getText().strip() == 'Broadcast Schedules':
				table = tables[i+1]
				break
		tds = table.findAll('td')
		league = ''
		out = []
		for i in range(len(tds)):
			if (i%2 == 0):
				league = tds[i].find('img')['title']
			else:
				a = tds[i].find('a')
				url = self.base + a['href']
				ev = a.getText().strip()
				ev_time = tds[i].find('span', {'class': 'date'}).getText()
				t1, t2 = ev_time.split('at')
				day = t1.split(' ')[0].strip()
				month = t1.split(' ')[1].strip()
				t = t2.strip()
				tm, stamp = self.convert_time(t, month, day)
				title = u'(%s) [B]%s[/B] - (%s)'%(tm, ev, league)        
				out.append((url, title))

		return out
def yaz64(e):
    _keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    t = ''
    f = 0
    e = re.sub('[^A-Za-z0-9\\+\\/\\=]', '', e)
    while f < len(e):
        s = _keyStr.find(e[f])
        f += 1
        o = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        u = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        a = _keyStr.find(e[f]) if f < len(e) else 0
        f += 1
        n = s << 2 | o >> 4
        r = (o & 15) << 4 | u >> 2
        i = (u & 3) << 6 | a
        t = t + chr(n)
        if u != 64:
            t = t + chr(r)
        if a != 64:
            t = t + chr(i)

    return t       


def mRealUrl(sHtmlContent): 
    sPattern = '<link rel="alternate" type="application/json+oembed" href="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:

        return  aResult[1][0]        


def RealUrl(url):
   
           
             
    data =getHtml(url)
    data =data.replace('+', '').replace('&#8243;', '"')
    logger.info("urlla----: %s" %data)
    sPattern = '<link rel="canonical" href="(.+?)" />'
    oParser = cParser()
    aResult = oParser.parse(data, sPattern)
    if (aResult[0] == True):
         return RealUrl2( aResult[1][0])
def RealUrl2(url):  # Recupere les liens des regex
    data =getHtml(url)
    r = re.search('<iframe.+?src="(.+?)"', data)
    if (r):
        url = r.group(1)
        return url


def RetRealUrl(chain):  # Recupere les liens des regex
    r = re.search('<iframe src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('<iframe width=".+?" height=".+?" src="(.+?)"', chain)
    if (r):        
        url = r.group(1)
        return url
    r = re.search('<iframe allowFullScreen frameborder=0 marginheight=0 marginwidth=0 scrolling=.+?src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url     
    r = re.search('<iframe frameborder="no" height=".+?" src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url

    r = re.search('<p><iframe frameborder="0" marginheight="0" marginwidth="0" src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('<iframe.+?src="(.+?)"', chain)
    if (r):        
        url = r.group(1)
        return url

    r = re.search('"0;URL=(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('bradmax_video url="(.+?)" autoplay="true"', chain)
    if (r):
        url = r.group(1)
        return url

             

def showHosters1(sUrl4,name):  # affiche les videos disponible du live
    oGui = cGui()
    UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    url = RealUrl(sUrl4)               
#    logger.info("chain---: %s" %str(chain))
#    chain =chain.replace('&#8221;', '"').replace('&#8243;', '"')
#    url = RealUrl(chain)
   


    
#    logger.info("chain---: %s" %str(chain))
#    url = RetRealUrl(chain)
    logger.info("urlmmm---: %s" %str(url))
    url =str(url).replace('https://href.li/?', '').replace('https://daddylive.fun/livetv/stream-', 'https://poscitech.click/tv/ch')
#    if  '.m3u8' in url:
    
#       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')
    if not (url.startswith("http")):                       
          url = "http:" + url
    logger.info("url---: %s" %str(url))
    resolve(url,name)
    return
def showHosters2():  # affiche les videos disponible du live
    oGui = cGui()
    UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    oInputParameterHandler = cInputParameterHandler()
    sUrl4 = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle2 = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    logger.info("sUrl4: %s" %str(sUrl4))
    sHtmlContent =  getHtml(sUrl4)
    logger.info("sHtmlContent: %s" %str(sHtmlContent))
    oParser = cParser()
    if '<iframe width=' in  sHtmlContent:
        sPattern = '<iframe width=".+?" height=".+?" src="(.+?)".+?</iframe>'
    else:
        sPattern = '<ifram.+?allowFullScreen.+?src="(.+?)".+?</iframe>'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:

        sHosterUrl = ''
        Referer = ''
        url = aResult[1][0]
        if not (url.startswith("http")):
            url = "http:" + url                                                              
        url =str(url).replace('https://href.li/?', '').replace('https://daddylive.fun/livetv/stream-', 'https://poscitech.click/tv/ch')
        resolve(url,sMovieTitle2)
        return
      # https://pelotero.net/tntsports.php

def showHosters():  # affiche les videos disponible du live
    oGui = cGui()
    UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    oInputParameterHandler = cInputParameterHandler()
    sUrl4 = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    from resources.lib.handler.requestHandler import cRequestHandler
   # oRequestHandler = cRequestHandler(sUrl4)        
    chain = getHtml(sUrl4)               
    logger.info("chain: %s" %str(chain))
    url = RetRealUrl(chain)
    url =str(url).replace('https://href.li/?', '').replace('https://daddylive.fun/livetv/stream-', 'https://poscitech.click/tv/ch').replace('https://daddylive.me/livetv/stream-', 'https://poscitech.click/tv/ch')
    if not (url.startswith("http")):                        
          url = "http:" + url
    logger.info("url: %s" %str(url))
    resolve(url,name)
def ccookie2( Url ):
    oGui = cGui()
   
    
  

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Url, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
       print(e.read())
       print(e.reason)

    sHtmlContent = to_utf8(response.read())
    head = response.headers
    return  head
def resolve(urlk,name):                                                       #  f693b5c4cec828b0cbbd1682483b197ce8b3e35d1bfe888a83231661381359bc5
    oGui = cGui()
    UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    sHosterUrl = ''
    sThumb = ''
    Referer = ''
    sMovieTitle2= name
    #name= 'PLAY'
    #from resources.lib.handler.requestHandler import cRequestHandler
    if urlk:

        sHosterUrl = ''
        Referer = ''
        url = urlk             
        if not (url.startswith("http")):
            url = "http:" + url
        logger.info("url: %s" %str(url))

        if 'sawlive.tv' in url:                                                         
       
            cf=getHtml(url)
            rUrl = re.findall(r'''src=\s*["'](.+?)['"]''', cf, re.DOTALL)[0]
            cfe=getHtml(rUrl)
            from OTVJSfuckdec import OTVJSfuck  
            cfe=cfe.replace("var ", "").replace('split(";";', 'split(";");')     
            r= OTVJSfuck(cfe).decode()
            urll = client.parseDOM(r, 'iframe', ret='src')[0]                                    
            data1= re.findall("(.+?)'stre'/'(.+?)'",urll)
            (bir,iki)=data1[0]
            urllk = iki+r
            dat= re.findall('= "(.+?)"',urllk)[0]
           
            dat =str(dat).split(';')
            urllan =bir.replace("'", "")+ '/stream/'+ dat[1]+ '/'+ dat[0]
            logger.info("urlla----: %s" %urllan)
            cfem=getHtml(urllan)
            
            unpack = re.findall(r'''(eval.+?\{\}\))\)''', cfem, re.DOTALL)[0]
            from resources.modules import jsunpack                     
            data = six.ensure_text(jsunpack.unpack(str(unpack) + ')'),encoding='utf-8')
            data=data.replace("var jameiei=", "").replace(";", "")#.replace("[", "'").replace(",", "',").replace("]", "'")    
            U=ASCII(data)
            U = U+'|Host=198.144.159.40&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'#+ urll
            logger.info("U----: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')

        if  'soccer24hd.com' in url:
            url =str(url).replace('ww.', '')          
            r=gegetHtml(url)                  
            logger.info("r-: %s" %str(r))            
            urll = client.parseDOM(r, 'iframe', ret='src')[0]
            logger.info("urll-: %s" %str(urll)) 
           # referer = url
           # urlla =gegetHtml(urll)
            urlla = six.ensure_str(client.request(urll, referer=url))                               
            logger.info("urlla----: %s" %str(urlla))
            U =getHosterIframe(urll,url)
            U = U+'|Referer=https://soccer24hd.com/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'#+ urll
            logger.info("U----: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if  'ustreamix.to' in url:
            url = url.split('&')
            url = url[0]
            logger.info("urlurlurl----: %s" %str(url)) 
            r=gegetHtml(url)
            logger.info("r----: %s" %str(r))            
            urll = client.parseDOM(r, 'iframe', ret='src')[0]+ r
            logger.info("urll-: %s" %str(urll)) 
           # referer = url
           # urlla =gegetHtml(urll)
            urlla = six.ensure_str(client.request(urll, referer=url))                               
            logger.info("urlla-ll---: %s" %str(urlla))
            U =getHosterIframe2(urlla)
            U = U+'|Referer=https://starlive.xyz/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'#+ urll
            logger.info("U-ll---: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if  'xestreams.com' in url:
            r=gegetHtml(url)
            U =getHosterIframe2(r)
            U = U+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'#+ urll
            logger.info("U-ll---: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')

          
        if  'starlive.xyz' in url:
            
            r=gegetHtml(url)
            logger.info("r-: %s" %str(r))            
            urll = client.parseDOM(r, 'iframe', ret='src')[0]
            if not (urll.startswith("http")):                       
               urll = "http:" + urll

            logger.info("urll-: %s" %str(urll)) 
           # referer = url
           # urlla =gegetHtml(urll)
            urlla = six.ensure_str(client.request(urll, referer=url))                               
            logger.info("urlla----: %s" %str(urlla))
            U =getHosterIframe(urll,url)
            U = U+'|Referer=https://wigistream.to/&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'#+ urll
            logger.info("U----: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
             
        if 'tutele.sx' in url :
            if  'pelotero.net' in url:
              chain = getHtml(url)
              url = RetRealUrl(chain)
            referer='https://www.tutele.sx/'
            r= six.ensure_str(client.request(url, referer=referer))
            logger.info("r-: %s" %str(r))            
            urll = client.parseDOM(r, 'iframe', ret='src')[0]
            urll = urll.replace("'+encodeURIComponent(document.referrer)+'", '')+ url
            logger.info("urll----: %s" %str(urll))
            urla =ccookie2(urll)
            logger.info("ret-: %s" %str(urla))                   

            referer = url
           # r = six.ensure_str(client.request(url, referer=referer))
            urlla = six.ensure_str(client.request(urll, referer=referer))                               
            urlla = urlla.replace('\/', '/') 
            logger.info("urlla----: %s" %str(urlla))
            Xauth = re.search('"auth":"(.+?)"', urlla).group(1)
            
            data1= re.findall(r'''value=\s*["'](.+?)['"]''', urlla, re.DOTALL)[0]
            U = base64.b64decode(data1)
           # U = gegetHtml(U) 
            logger.info("U----: %s" %str(U))
           # U =ccookie2(U)
           # logger.info("U2----: %s" %str(U))
            Xauth= to_utf8(Xauth)
            
            timestamp = time.time()
            host = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',to_utf8(U))
            Modi =time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(timestamp))
            U= to_utf8(U)+'|redirect_uri=https://www.tutele.sx/redirect_image.php' #+ url #+  '&Xauth='+Xauth
            U = U.replace('.m3u8', '.m3u8') 
#Host: chupachichi10.site
#Connection: keep-alive
#sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
#Xauth: 5jnX9+oBu6TjHHZNOB5FK4yfN0o1zNR+cvP4YNmItKGvvJJAFxpaBsDaO0z51F3Uqc7iOKwuwobmfNe3epleNGhBuJuC1r9x5znS4YOaxpZFpG9T1l74dmsXvtiC3RTqouWwuuzqQUbNHhYxHP3iEq/QatXaWU3jK/oYYZqfG+RRfN3JwONppIzCEEcMsjKluq5stSj2zwq02oFHDZP1Ushq3pFBG+EMu1KzvCfPCuUftIL/FePtrdqehC/KM45eV6IyUBmfF+eeYLhT9VuUPKXMGv8jArnLRoJMxhLgow4B3CHGcQrPnK9Z2XWHywokr35vrc326U6FfUEg7VyWInof03F9sWE6QV5gETXWreCHLlxKR+Va6igJTDid0EOp
#sec-ch-ua-mobile: ?0
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36
#sec-ch-ua-platform: "Windows"
#Accept: */*
#Origin: https://www.tutele.sx
#Sec-Fetch-Site: cross-site
#Sec-Fetch-Mode: cors
#Sec-Fetch-Dest: empty
#Referer: https://www.tutele.sx/embed.php?&a=149&s=vsdr6rnese2aj0nu8e23g4isbv&ip=95.90.195.237&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F99.0.4844.84+Safari%2F537.36&referer=https%3A%2F%2Fpelotero.net%2F
#Accept-Language: en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,tr;q=0.6
#Accept-Encoding: gzip, deflate

           # U = U+'|Referer='               Origin: https://www.tutele.sx
                #&If-Modified-Since='+Modi+'             #                If-None-Match: "62325361-3f9"
            logger.info("U----: %s" %str(U))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'wikisport.click' in url or 'freestreams-live1.com' in url or 'pelotero' in url:
                   referer = 'http://wikisport.click/'
                   U = getHosterIframe(url, referer)

                  
                   U = U.replace("https://tr4e.herokuapp.com/", '')+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0&Host=stream2.grandma.fit'#.replace("http://134.19.182.131:8080/edg1_2.m3u8", "http://212.224.98.205:2200/NL/mlcampeonhd-esp/index.m3u8?token=") +'|Referer=http://wikisport.click/'
                   logger.info("U----: %s" %str(U))
                   addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'fb.freestreams' in url or 'cf.freestreams-live1.com' in url:
                   referer = 'http://fb.freestreams-live1.com/'
                   U = getHosterIframe(url, referer)
                                                              
                  
                   U = U.replace("https://tr4e.herokuapp.com/", '')+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0&Host=stream2.grandma.fit'#.replace("http://134.19.182.131:8080/edg1_2.m3u8", "http://212.224.98.205:2200/NL/mlcampeonhd-esp/index.m3u8?token=") +'|Referer=http://wikisport.click/'
                   logger.info("U----: %s" %str(U))
                   addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')


        if 'weakstreams' in url:
                    sHtmlContent=getHtml(url) 
                    fid ='http://weakstreams.com/gethls?idgstream='+re.search('vidgstream = "(.+?)"', sHtmlContent).group(1) +'&serverid=&cid=' 
                    Content=getHtml(fid)
                    Content = Content.replace("\/", '/')
                    logger.info("Conten: %s" %Content)
               #logger.info("sUrl : %s" % urll)
                    U = re.search('"rawUrl":"(.+?)"', Content).group(1)
                    U = U+'|Referer='+ fid
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'sportsonline' in url or 'sportzonline' in url:
        #urll='https://bedsport.live/ch6.php'
            referer = url
            r = six.ensure_str(client.request(url, referer=referer))
            logger.info("--r: %s" %str(r))                                
            frame = client.parseDOM(r, 'iframe', ret='src')[0]
            referer = 'https://sportsonline.to/'
            sHtmlContent = six.ensure_str(client.request(frame, referer=referer))
           # sHtmlContent = getHtml(frame)
            logger.info("sHtmlContent--r: %s" %str(sHtmlContent)) 
            sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
            aResult = re.findall(sPattern, sHtmlContent)

            if aResult:
               sstr = aResult[0]
               if not sstr.endswith(';'):
                 sstr = sstr + ';'
               sUnpack = cPacker().unpack(sstr)
               logger.info("sUnpack--r: %s" %str(sUnpack)) 
               sPattern = 'src="(.+?)"'
               aResult = re.findall(sPattern, sUnpack)
               U = aResult[0]+'|Referer=https://streamservice443.net&User-Agent={}'.format(quote(ua))
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')  
                        

        if 'poscitech' in url:
            
            url = url.replace('https://poscitech.click/tv/ch', '').replace('.php', '').replace('https://eplayer.click/premiumtv/poscitech.php?id=', '')
            Url3 ='https://poscitech.click/'
            Url2 ='https://poscitech.click/tv/ch%s.php' %(url)
            ssHtmlContent=getHtml(Url2)
#            logger.info("ssHtmlContent: %s" % ssHtmlContent)
            Url4 = re.search('<iframe src="(.+?)"', ssHtmlContent).group(1)
#            logger.info("Url4: %s" % Url4) 
            sHtmlContent = requests.session().get(Url4, headers={'Content-Type': 'text/html',
                'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
                'Referer':Url3,
                'Accept': 'text/html, */*'}).text 
#            logger.info("sHtmlConten: %s" % sHtmlContent) 
            Url5 = re.search('<iframe src="(.+?)"', sHtmlContent).group(1)     # Url5 = re.search('<iframe src="(.+?)"', sHtmlContent).group(1)
            lsHtmlContent=getHtml(Url5) 
#            logger.info("sHtmlConten: %s" % lsHtmlContent)                        # Origin=https://player.licenses4.me&
            if 'source' in   sHtmlContent:
               U = re.search("//source:'(.+?)/chunks.m3u8.+?'", lsHtmlContent).group(1)
               U = U+'/chunks.m3u8|Accept-Language=tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3&Host=www.mireasa-live.com&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0&Referer=https://player.licenses4.me/'
               addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')        
        if 'cdn.crichd.pro' in url:
                    sHtmlContent=getHtml(url) 
                    fid ='https://123zcast.com/embed.php?player=desktop&v='+re.search('fid="(.+?)"', sHtmlContent).group(1)
                    Content=getHtml(fid)
                    logger.info("Conten: %s" %Content)
               #logger.info("sUrl : %s" % urll)
                    U = re.search("source: '(.+?)'", Content).group(1)
                    U = U+'|Referer='+ fid
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'futbolcafem' in url:
                    sHtmlContent=getHtml(url) 
                    #logger.info("sHtmlConten: %s" % sHtmlContent)
               #logger.info("sUrl : %s" % urll)
                    U =re.search('<video.+?src="(.+?)"', sHtmlContent).group(1)
                    U = U.replace('.m3u8', '.m3u8')       
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'sbautumn.net' in url:
                    sHtmlContent=getHtml(url) 
                    #logger.info("sHtmlConten: %s" % sHtmlContent)
               #logger.info("sUrl : %s" % urll)
                    U ='https://sbautumn.net'+ re.search("var videoLink = '(.+?)'", sHtmlContent).group(1)
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')


        if 'key.licenses4.me' in url:
                    logger.info("UrUrl4: %s" % url)
                   
                    sHtml=getHtml(url)
                    sHtml = sHtml.replace("'", '"')
                    logger.info("sHtml : %s" % sHtml)
                    Url = re.search('<iframe allow="encrypted-media".+?src="(.+?)"', sHtml).group(1)
                    eferer=[('Referer', url)]
                    sHtmlContent=gegetUrl(Url,headers=eferer)
                    sHtmlContent = sHtmlContent.replace("'", '"')
                    logger.info("sHtmlContent : %s" % sHtmlContent)
                    U =re.search('dash:  "(.+?)"', sHtmlContent).group(1)
                    
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
        if 'sport365hd.com' in url:
                    U = url.replace("https://sport365hd.com/channel", "https://5-61-37-22.livesports24.online") + ".m3u8"
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')
            #logger.info("urll----: %s" %str(urll+r))
           


        if 'popofthestream' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
            sPattern = 'src="([^"]+)'
            aResult = re.findall(sPattern, sHtmlContent)
            if aResult:
                url2 = url.replace('-', '/')
                urlChannel = url2.replace('html', 'json')
                oRequestHandler = cRequestHandler(urlChannel)
                sHtmlContent = oRequestHandler.request();
                result = json.loads(sHtmlContent)
                if 'id' in result:
                    idChannel = result['id']
                    oRequestHandler = cRequestHandler(url2)
                    sHtmlContent2 = oRequestHandler.request();
                    sPattern = '<iframe.+?src="([^\']+)'
                    aResult = re.findall(sPattern, sHtmlContent2)
                    if aResult:
                        url = aResult[0] + idChannel
                    

        if 'sportlevel' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = "manifestUrl: '(.+?)',"
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = 'http://d.sportlevel.com' + aResult[0]
            else:
                sPattern2 = '(http:\/\/embedded.+?)"'
                aResult = oParser.parse(sHtmlContent2, sPattern2)
                if (aResult[0] == True):
                    url2 = aResult[1][0]
                    oRequestHandler = cRequestHandler(url2)
                    sHtmlContent3 = oRequestHandler.request()
                    sPattern = "RESOLUTION=(\w+)\s*(http.+?)(#|$)"
                    aResult2 = oParser.parse(sHtmlContent3, sPattern)
                    if (aResult2[0] == True):
                        for aResult in aResult2[1]:
                            q = aResult[0]
                            sHosterUrl = aResult[1]
                            sDisplayTitle = sMovieTitle2 + ' [' + q + '] '

                            oHoster = cHosterGui().checkHoster(sHosterUrl)
                            if (oHoster != False):
                                oHoster.setDisplayName(sDisplayTitle)
                                oHoster.setFileName(sMovieTitle2)
                                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
                        oGui.setEndOfDirectory()
                        return

        if 'tv.rushandball' in url:
            sPattern = '\/(\d+)'
            aResult = re.findall(sPattern, url)
            if aResult:
                id = aResult[0]
                url2 = 'https://tv.rushandball.ru/api/v2/content/' + id + '/access'

                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.setRequestType(1)
                oRequestHandler.addHeaderEntry('Referer', url)
                sHtmlContent = oRequestHandler.request()
                sPattern = 'stream.+?"(https.+?)"'
                aResult = oParser.parse(sHtmlContent, sPattern)
                if (aResult[0] == True):
                    sHosterUrl = aResult[1][0]
            sHosterUrl = sHosterUrl
        if 'seenow.tv' in url:
            sPattern = 'api.(.+?)$'
            aResult = re.findall(sPattern, url)
            if aResult:
                data = 'url=' + aResult[0] + '&type=tv'  # url=itv-4&type=tv]
                oRequestHandler = cRequestHandler(url)
                oRequestHandler.addHeaderEntry('Referer', url)
                oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
                sHtmlContent = oRequestHandler.request()
                cook = oRequestHandler.GetCookies()
                xbmc.sleep(200)
                oRequestHandler = cRequestHandler(url)
                oRequestHandler.setRequestType(1)
                oRequestHandler.addHeaderEntry('Content-Length', len(data))
                oRequestHandler.addHeaderEntry('Referer', url)
                oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
                oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
                # oRequestHandler.addHeaderEntry('Content-Type', 'application/json; charset=utf-8')
                oRequestHandler.addHeaderEntry('Cookie', cook)
                # oRequestHandler.addHeaderEntry('Connection', 'keep-alive')
                oRequestHandler.addParametersLine(data)
                sHtmlContent2 = oRequestHandler.request()  # json

                sPattern = 'stream_id.+?(\d+)'
                aResult = re.findall(sPattern, sHtmlContent2)
                if aResult:
                    stream_id = aResult[0]
                    url2 = 'https://www.filmon.com/api-v2/channel/' + stream_id + '?protocol=hls'
                    oRequestHandler = cRequestHandler(url2)
                    oRequestHandler.addHeaderEntry('Referer', url)
                    oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
                    sHtmlContent2 = oRequestHandler.request()
                    sPattern = 'quality"."(\w+)".*?url.*?"(https.+?)"'
                    aResult = re.findall(sPattern, sHtmlContent2)
                    if aResult:
                        for Result in aResult:
                            q = Result[0]
                            sHosterUrl = Result[1]
                            sDisplayTitle = sMovieTitle2 + ' [' + q + '] '

                            oHoster = cHosterGui().checkHoster(sHosterUrl)
                            if (oHoster != False):
                                oHoster.setDisplayName(sDisplayTitle)
                                oHoster.setFileName(sMovieTitle2)
                                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

                        oGui.setEndOfDirectory()
                        return

        if 'faraoni1' in url:
            # type de chaine : eurosport
            # plusieurs suivi  de liens  possibles 5 max vus
            # ex :
            # http://faraoni1.ru/1/10.html ,20.html 5 requetes
            # LiveTV/live2/1.html 3 requetes
            # etc

            nextlink = url
            for x in range(0, 6):  # 6 reqs max pour trouver lhost (normalement 5 )
                oRequestHandler = cRequestHandler(nextlink)
                sHtmlContent = oRequestHandler.request()
                sPattern = 'url.+?(http.+?m3u8)'
                aResult = re.findall(sPattern, sHtmlContent)
                if aResult:
                    sHosterUrl = str(aResult[0])
                    break
                else:
                    sPattern = '<iframe.+?src="([^"]+)'
                    aResult = re.findall(sPattern, sHtmlContent)
                    if aResult:
                        nextlink = 'http://faraoni1.ru' + aResult[0]

        if 'embed.tvcom.cz' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
            sPattern = "source.+?hls.+?'(https.+?m3u8)"
            aResult = re.findall(sPattern, sHtmlContent)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'allsports.icu' in url:
            sPattern = 'ch(\d+).php'
            aResult = re.findall(sPattern, url)
            if aResult:
                id = aResult[0]
                url2 = 'http://allsports.icu/stream/ch' + id + '.html'
                sHosterUrl = getHosterIframe(url2, url2)
            sHosterUrl = sHosterUrl
        # old host
        if 'espn-live.stream' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            aResult = re.findall(sPattern, sHtmlContent2)
            if aResult:
                url = aResult[0]  # redirection vers un autre site ci-dessous

        if 'footballreal.xyz' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern1 = '<iframe src="(.+?)"'
            aResult = re.findall(sPattern1, sHtmlContent2)
            if aResult:
                url = aResult[0]  # redirection vers un autre site ci-dessous

        if 'dailydeports.pw' in url:
            oRequestHandler = cRequestHandler(url)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            oRequestHandler.addHeaderEntry('Referer', sUrl4)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src="([^"]+)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                if 'cdnz.one' in aResult[0]:
                    url = aResult[0]  # redirection vers un autre site
            else:
                sPattern2 = "str='([^']+)'"
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    for aEntry in aResult:
                        aEntry = aEntry.replace('@', '')
                        data = bytearray.fromhex(aEntry).decode()
                        sPattern3 = '<iframe src="([^"]+)"'
                        aResult1 = re.findall(sPattern3, data)
                        if aResult1:
                            url = aResult1[0]  # redirection vers un autre site
                            break

        if 'emb.apl' in url:  # Terminé - Supporte emb.aplayer et emb.apl3
            Referer = url
            oRequestHandler = cRequestHandler(url)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'source: *\'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0] + '|User-Agent=' + UA + '&referer=' + Referer
            else:
                sPattern2 = "pl\.init\('([^']+)'\);"
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0] + '|User-Agent=' + UA + '&referer=' + Referer
            sHosterUrl = sHosterUrl
        if 'cemdnz.one' in url:
            logger.info("url1: %s" %str(url))
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern1 = '<iframe src=["\'](.+?)["\']'
            aResult = re.findall(sPattern1, sHtmlContent2)
            if aResult:
                Referer = url
                url = aResult[0]  # redirection vers un autre site

        if 'sport7.pw' in url or 'vip7stream' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'videoLink = \'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0] + '|User-Agent=' + UA + '&referer=' + url
            sHosterUrl = sHosterUrl
        if 'totalsport.me' in url or 'airhdx' in url or 'givemenbastreams' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            if Referer:
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', Referer)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'source: ["\'](.+?)["\']'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'sportsbar.pw' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'videoLink = \'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'livesoccers.pw' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src=\'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = aResult[0]
                oRequestHandler = cRequestHandler(sHosterUrl2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', sHosterUrl2)
                sHtmlContent3 = oRequestHandler.request()
                sPattern3 = '<source src="([^"]+)"'
                aResult1 = re.findall(sPattern3, sHtmlContent3)
                if aResult1:
                    sHosterUrl = aResult1[0]
            sHosterUrl = sHosterUrl
        if 'assia' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'file:"([^"]+)"|source: \'([^\']+)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0][1] + '|User-Agent=' + UA + '&referer=' + url
            else:
                sPattern2 = '<source src=\'([^\']+)\''
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0] + '|User-Agent=' + UA + '&referer=' + url
            sHosterUrl = sHosterUrl
        if 'sawlive' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'src="([^"]+)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl3 = aResult[0]
                oRequestHandler = cRequestHandler(sHosterUrl3)
                sHtmlContent3 = oRequestHandler.request()
                sPattern3 = 'var .+? = "([^;]+);([^\"]+)";'
                aResult = re.findall(sPattern3, sHtmlContent3)
                if aResult:
                    sHosterUrl3 = "http://www.sawlive.tv/embedm/stream/" + aResult[0][1] + '/' + aResult[0][0]
                    oRequestHandler = cRequestHandler(sHosterUrl3)
                    sHtmlContent4 = oRequestHandler.request()

                    sPattern4 = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
                    aResult = re.findall(sPattern4, sHtmlContent4)
                    if aResult:
                        str2 = aResult[0]
                        if not str2.endswith(';'):
                            str2 = str2 + ';'
    
                        strs = cPacker().unpack(str2)
                        sPattern5 = 'var .+?=([^;]+);'
                        aResult1 = re.findall(sPattern5, strs)
                        if aResult1:
                            jameiei = eval(aResult1[0])
                            data = ''
                            for c in jameiei:
                                data += chr(c)
                            sHosterUrl = data

            sHosterUrl = sHosterUrl
        if 'sportlive.site' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src="(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = aResult[0]
                oRequestHandler = cRequestHandler(sHosterUrl2)
                sHtmlContent3 = oRequestHandler.request()
                sPattern3 = '<script type=\'text/javascript\'>id=\'(.+?)\''
                aResult2 = re.findall(sPattern3, sHtmlContent3)
                if aResult2:
                    sHosterUrl3 = aResult2[0]
                    sHosterUrl3 = "http://hdcast.pw/stream_jw2.php?id=" + sHosterUrl3
                    oRequestHandler = cRequestHandler(sHosterUrl3)
                    sHtmlContent4 = oRequestHandler.request()
                    sPattern4 = 'curl = "([^"]+)";'
                    aResult3 = re.findall(sPattern4, sHtmlContent4)
                    if aResult3:
                        sHosterUrl = aResult3[0]
                        sHosterUrl = base64.b64decode(sHosterUrl)
            sHosterUrl = sHosterUrl
        if 'stream365' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'var a[ 0-9]+="(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                gameId = int(aResult[2]) + int(aResult[0]) - int(aResult[1]) - int(aResult[2])
                sHosterUrl = 'http://91.192.80.210/edge0/xrecord/' + str(gameId) + '/prog_index.m3u8'
            sHosterUrl = sHosterUrl
        if 'youtube' in url:  # Je sais pas
            logger.info("url----: %s" %str(url))
            patterns = [r'(?P<video_id>[\w-]{11})',
                r'(?:http)*s*:*[/]{0,2}(?:w{3}\.|m\.)*youtu(?:\.be/|be\.com/'
                r'(?:embed/|watch/|v/|.*?[?&/]v=))(?P<video_id>[\w-]{11}).*']

            for pattern in patterns:
                       #  http://www.youtube.com/embed/dOjwpCzYoAw?rel=0&autoplay=1
                v_id = re.search(pattern, url)
                if v_id:
                    video_id = v_id.group('video_id')
                logger.info("video_id: %s" % video_id)
                import youtubecom_tr
                youtubecom_tr.YouTubeplay2(video_id)

        if 'streamup.me' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src="([^"]+)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = aResult[0]
                oRequestHandler = cRequestHandler(sHosterUrl2)
                sHtmlContent3 = oRequestHandler.request()
                sHtmlContent3 = Unquote(sHtmlContent3)
                sPattern3 = 'src: "\/\/(.+?)"'
                aResult = re.findall(sPattern3, sHtmlContent3)
                if aResult:
                    sHosterUrl = 'http://' + aResult[0]
            sHosterUrl = sHosterUrl
        if 'livestream' in url:  # fixé
            sPattern2 = '<td bgcolor=".+?" *align="center".+?\s*<iframe.+?src="https://([^"]+)/player?.+?</iframe>'
            aResult = re.findall(sPattern2, sHtmlContent)
            if aResult:
                accountid = aResult[0]
                jsonUrl = 'https://player-api.new.' + accountid + '?format=short'
                oRequestHandler = cRequestHandler(jsonUrl)
                sHtmlContent = oRequestHandler.request()
                sPattern3 = '"m3u8_url":"(.+?)"'
                aResult = re.findall(sPattern3, sHtmlContent)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'forbet.tv' in url:  # Probleme ssl
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'file: "([^"]+)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'p.hd24.watch' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'data-channel="([^"]+)">'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                Host = '190-2-146-56.livesports24.online'
                sHosterUrl = 'https://' + Host + '/' + aResult[0] + '.m3u8'
            sHosterUrl = sHosterUrl
        if 'hdsoccerstreams.net' in url:  # Pas terminer
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<script>fid="(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                fid = aResult[0]
                url2 = 'http://webtv.ws/embed.php?live=spstream' + fid + '&vw=700&vh=440'
                Referer = url
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', Referer)
                sHtmlContent3 = oRequestHandler.request()                         

        if 'thesports4u.net' in url or 'soccerstreams' in url or 'all.ive' in url or 'cdnz.one' in url or '1.vecdn' in url:  # Fini
            if 'all.ive' in url or 'cdnz.one' in url or '1.vecdn' in url:
                logger.info("url1: %s" %str(url))
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = oRequestHandler.request()
                logger.info("sHtmlContent2: %s" %str(sHtmlContent2))
                sPattern2 = "<script>fid='(.+?)'"
                aResult = re.findall(sPattern2, sHtmlContent2)

                if aResult:
                    Referer = 'https://ragnaru.net/'
                    url2 = 'https://ragnaru.net/embed.php?player=desktop&live=' + aResult[0]
                    logger.info("url2: %s" %str(url2))
                    oRequestHandler = cRequestHandler(url2)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', 'https://all.ive.zone/')
                    sHtmlContent3 = oRequestHandler.request()

            if 'thesports4u' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = oRequestHandler.request()
                sPattern2 = '<script>fid="(.+?)"'
                aResult = re.findall(sPattern2, sHtmlContent2)

                if aResult:
                    url2 = 'http://wlive.tv/embed.php?player=desktop&live=' + aResult[0] + '&vw=700&vh=440'
                    oRequestHandler = cRequestHandler(url2)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', 'http://thesports4u.net/')
                    oRequestHandler.addHeaderEntry('Host', 'www.wlive.tv')
                    sHtmlContent3 = oRequestHandler.request()

            if 'soccerstreams' in url:
                url = url.replace('/hds', '/hdss/ch')

                oRequestHandler = cRequestHandler(url)
                sHtmlContent1 = oRequestHandler.request()
                sPattern2 = '<script>fid="(.+?)"'
                aResult = re.findall(sPattern2, sHtmlContent1)

                if aResult:
                    url2 = 'http://wlive.tv/embedra.php?player=desktop&live=' + aResult[0] + '&vw=700&vh=440'
                    oRequestHandler = cRequestHandler(url2)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', url)
                    oRequestHandler.addHeaderEntry('Host', 'www.wlive.tv')
                    sHtmlContent3 = oRequestHandler.request()

            if sHtmlContent3:
                m = re.search('return.*?\[(.*?)\].*?\+\s+(.*)\.join.*document.*?"(.*?)"', sHtmlContent3)
                if m:
                    timeVar = m.group(2)
                    hashVar = m.group(3)
    
                    # http://tv.wlive.tv/tv/lu2mIWw6KZ20180321/playlist.m3u8?hlsendtime=1542297480&hlsstarttime=0&hlshash=jhTrgemr-kGm9E01YIVfqkZ9VPobibqbDRiov2psf_A=
                    url3 = ''.join(m.group(1).split(','))
                    url3 = url3.replace('"', '').replace('\/', '/')
                    if not url3.startswith('http'):
                        url3 = 'http:' + url3 
    
                    m = re.search(timeVar + '.*?\[(.*?)\]', sHtmlContent3)
                    if m:
                        timeStr = ''.join(m.group(1).split(',')).replace('"', '')
                        url3 += timeStr
    
                    m = re.search(hashVar + '>(.*?)<', sHtmlContent3)
                    if m:
                        hashStr = ''.join(m.group(1).split(',')).replace('"', '')
                        url3 += hashStr
                        sHosterUrl = url3
                        logger.info("sHosterUrl: %s" %str(sHosterUrl))
                        if Referer:
                            sHosterUrl += '|referer=' + Referer
            sHosterUrl = sHosterUrl
        if 'sports-stream.net' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'sports-stream.+?ch=(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                fid = aResult[0]
                url2 = 'http://webtv.ws/embeds.php?live=spstream' + fid + '&vw=700&vh=440'
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', 'http://www.sports-stream.net/chtv/sps.php?ch=' + fid)
                sHtmlContent2 = oRequestHandler.request()

                sPattern3 = 'source src="(.+?)".+?">'
                aResult = re.findall(sPattern3, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'sports-stream.link' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'sports-stream.+?ch=(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                fid = aResult[0]
                url2 = 'https://www.airhdx.com/embedd.php?live=spstream' + fid + '&vw=700&vh=440'
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', 'http://www.sports-stream.link/chtv/sps.php?ch=' + fid)
                sHtmlContent2 = oRequestHandler.request()

                sPattern3 = 'source: "(.+?)",'
                aResult = re.findall(sPattern3, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0] + '|referer=' + url2
            sHosterUrl = sHosterUrl
        if 'foot.futbol' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src=\'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = aResult[0]
                Referer = sHosterUrl2
                oRequestHandler = cRequestHandler(sHosterUrl2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', Referer)
                sHtmlContent3 = oRequestHandler.request()
                sPattern3 = '<source src="([^"]+)"'
                aResult2 = re.findall(sPattern3, sHtmlContent3)
                if aResult2:
                    sHosterUrl = aResult2[0]
            sHosterUrl = sHosterUrl
        if 'viewhd.me' in url:  # Pas terminer je sais pas comment on trouve le m3u dans hdstream
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<script>fid="([^"]+)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = 'http://www.hdstream.live/embed.php?player=desktop&live=' + aResult[0] + '&vw=620&vh=490'
                Referer = sHosterUrl2
                oRequestHandler = cRequestHandler(sHosterUrl2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', Referer)
                sHtmlContent3 = oRequestHandler.request()
                          #  new.socolive.pro
        if 'socolive.pro' in url or 'new.socolive.pro' in url: # OK
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'channel=\'(.+?)\', g=\'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                for aEntry in aResult:
                    channel = aEntry[0]
                    g = aEntry[1]

            url2 = 'https://live.uctnew.com/hembedplayer/' + channel + '/' + g + '/700/480'
            logger.info("url2: %s" %str(url2))
            oRequestHandler = cRequestHandler(url2)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            oRequestHandler.addHeaderEntry('Referer', 'http://new.socolive.pro/')
            sHtmlContent2 = oRequestHandler.request()
            logger.info("sHtmlContent2: %s" %str(sHtmlContent2))
            sPatternUrl = 'hlsUrl = "https:\/\/" \+ ea \+ "([^"]+)"'
            sPatternPK = 'enableVideo."([^"]+)"'
            sPatternEA = 'ea = "([^"]+)";'
            aResultUrl = re.findall(sPatternUrl, sHtmlContent2)
            aResultEA = re.findall(sPatternEA, sHtmlContent2)
            aResultPK = re.findall(sPatternPK, sHtmlContent2)
            if aResultUrl and aResultPK and aResultEA:
                aResultPK = aResultPK[0][:53] + aResultPK[0][54:]   # une lettre s'est glissé dans le code :D
                url3 = aResultEA[0] + aResultUrl[0]+ aResultPK
                sHosterUrl = 'https://' + url3
                logger.info("sHosterUrl: %s" %str(sHosterUrl))
            sHosterUrl = sHosterUrl

        if 'socolive.xyz' in url or 'sportsfix' in url or 'bartsim' in url or 'buzztv.futbol' in url or 'leet365.cc' in url:# Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'iframe src="(.+?)"'                                    
            aResult = re.findall(sPattern2, sHtmlContent2)
                                                                                               
            if aResult:
                url2 = aResult[0]
                if not url.startswith('http'):
                    url2 = "http:" + url2
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                sHtmlContent2 = oRequestHandler.request()

                sPattern2 = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
                aResult = re.findall(sPattern2, sHtmlContent2)

                if aResult:
                    str2 = aResult[0]
                    if not str2.endswith(';'):
                        str2 = str2 + ';'

                    strs = cPacker().unpack(str2)
                    logger.info("strs--r: %s" %str(strs))
                    sPattern3 = '{source:"([^"]+)"'
                    aResult1 = re.findall(sPattern3, strs)
                    if aResult1:
                        U = aResult1[0] + '|User-Agent=' + UA + '&referer=' + url2
                    else:
                        sPattern3 = 'src="([^"]+)"'
                        aResult1 = re.findall(sPattern3, strs)
                        if aResult1:
                            U = aResult1[0] + '|User-Agent=' + UA + '&referer=' + url2
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, U, '')

        if '1me.club' in url or 'sportz' in url or 'streamhd' in url or 'hdsportslive' in url or 'cricfree' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()

            if 'hdsportslive' in url or 'cricfree' in url:
                sPattern2 = 'document.write\(unescape\(\'(.+?)\'\)\)'
                aResult = re.findall(sPattern2, sHtmlContent2)
                unQuote = Unquote(aResult[0])

                sPattern2 = '<iframe.+?src="(.+?)"'
                aResult = re.findall(sPattern2, unQuote)

                url = aResult[0]
                if not url.startswith('http'):
                    url = 'https:' + url

                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = oRequestHandler.request()

                sPattern2 = '<iframe.+?src=\'(.+?)\''
                aResult = re.findall(sPattern2, sHtmlContent2)

            else:
                sPattern2 = '<iframe src="(.+?)"'
                aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:

                if 'wstream.to'  in aResult[0] or 'streamcdn' in aResult[0]:  # Terminé
                    embedUrl = aResult[0]

                    if embedUrl.startswith('//'):
                        embedUrl = 'https:' + embedUrl

                    if 'sportz' in url or 'hdsportslive' in url or 'cricfree' in url:
                        Referer = url
                    else:
                        Referer = 'http://1me.club'

                    oRequestHandler = cRequestHandler(embedUrl)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', Referer)
                    sHtmlContent3 = oRequestHandler.request()

                    sPattern2 = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
                    aResult = re.findall(sPattern2, sHtmlContent3)

                    if aResult:
                        str2 = aResult[0]
                        if not str2.endswith(';'):
                            str2 = str2 + ';'

                    strs = cPacker().unpack(str2)
                    sPattern3 = '{source:"([^"]+)"'
                    aResult1 = re.findall(sPattern3, strs)
                    if aResult1:
                        sHosterUrl = aResult1[0]

                if 'widestream.io' in aResult[0]:  # Terminé
                    oRequestHandler = cRequestHandler(aResult[0])
                    sHtmlContent3 = oRequestHandler.request()
                    sPattern3 = 'file:"([^"]+)"'
                    aResult1 = re.findall(sPattern3, sHtmlContent3)
                    if aResult1:
                        sHosterUrl = aResult1[0]
            sHosterUrl = sHosterUrl
        
        if ('shd' in url) or ('hd' in url and 'streamhd' not in url and 'hdsportslive' not in url and 'airhdx'
                              not in url and 'wizhd' not in url):
                       
            urlApi = 'https://api.livesports24.online/gethost'
            sHtmlContent2 = ''
            channel = url.split('/')[4]
            try:
                oRequestHandler = cRequestHandler(urlApi)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                oRequestHandler.addHeaderEntry('Origin', 'https://' + url.split('/')[2])
                sHtmlContent2 = oRequestHandler.request()
            except:
                pass
            if sHtmlContent2:

                sPattern1 = '([^"]+)'
                aResult = re.findall(sPattern1, sHtmlContent2)
                if aResult:
                    host = aResult[0]
            else:
                urlApi = 'https://api.livesports24.online:8443/gethost'
                channel = url.split('/')[4]
                oRequestHandler = cRequestHandler(urlApi)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                oRequestHandler.addHeaderEntry('Origin', 'https://' + url.split('/')[2])
                sHtmlContent2 = oRequestHandler.request()

                sPattern1 = '([^"]+)'
                aResult = re.findall(sPattern1, sHtmlContent2)
                if aResult:
                    host = aResult[0]

            sHosterUrl = 'https://' + host + '/' + channel + '.m3u8'

        if 'sportgol7' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern1 = '<source src="(.+?)"'
            aResult = re.findall(sPattern1, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'nowlive.pro' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent3 = oRequestHandler.request()
            sPattern3 = 'src%3A%20%22//([^"]+)%3A([^"]+)m3u8'
            aResult1 = re.findall(sPattern3, sHtmlContent3)
            if aResult1:
                ip = aResult1[0][0]
                name = aResult1[0][1]
                sHosterUrl = 'http://' + ip + ':' + name + 'm3u8'
            sHosterUrl = sHosterUrl
        if 'harleyquinn' in url or 'joker' in url :  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'fid="(.+?)"; v_width=(.+?); v_height=(.+?);'
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                fid = aResult[0][0]
                vw = aResult[0][1]
                vh = aResult[0][2]

                url2 = 'http://www.jokersplayer.xyz/embed.php?u=' + fid + '&vw=' + vw + '&vh=' + vh
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                sHtmlContent2 = oRequestHandler.request()
                sPattern3 = 'src=http://(.+?)/(.+?) '
                aResult = re.findall(sPattern3, sHtmlContent2)
                if aResult:
                    ip = aResult[0][0]
                    url3 = 'http://' + ip + '/' + aResult[0][1]
                    oRequestHandler = cRequestHandler(url3)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', url2)
                    oRequestHandler.addHeaderEntry('Connection', 'keep-alive')
                    sHtmlContent2 = oRequestHandler.request()
                    sPattern3 = 'src=.+?e=(.+?)&st=(.+?)&'
                    aResult = re.findall(sPattern3, sHtmlContent2)
                    if aResult:
                        e = aResult[0][0]
                        st = aResult[0][1]
                        sHosterUrl = 'http://' + ip + '/live/' + fid + '.m3u8'+'?e=' + e + '&st=' + st
#            sHosterUrl = sHosterUrl
                if sHosterUrl == '':
                    url2 = 'http://player.jokehd.com/one.php?u=' + fid + '&vw=' + vw + '&vh=' + vh
                    oRequestHandler = cRequestHandler(url2)
                    oRequestHandler.addHeaderEntry('User-Agent', UA)
                    oRequestHandler.addHeaderEntry('Referer', url)
                    sHtmlContent2 = oRequestHandler.request()
                    sPattern3 = 'source: \'(.+?)\''
                    aResult = re.findall(sPattern3, sHtmlContent2)
                    if aResult:
                        sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'baltak.biz' in url: # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src="\/blok.php\?id=(.+?)"'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                url2 = aResult[0]
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', 'http://baltak.biz/blok.php?id=' + url2)
                sHtmlContent2 = oRequestHandler.request()

                sPattern2 = 'source: \'(.+?)\''
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0]
            #sHosterUrl = sHosterUrl
            else:
                sPattern2 = 'source: \"(.+?)\"'
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'footballstream' in url:  # Terminé
            url = url.replace('/streams', '/hdstreams')
            oRequestHandler = cRequestHandler(url)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            oRequestHandler.addHeaderEntry('Referer', url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'fid="(.+?)"; v_width=(.+?); v_height=(.+?);'
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                fid = aResult[0][0]
                vw = aResult[0][1]
                vh = aResult[0][2]

                embedded = "mobile"  # "desktop"

                url2 = 'http://www.b4ucast.me/embedra.php?player=' + embedded + '&live=' + fid + '&vw=' + vw + '&vh=' + vh
                oRequestHandler = cRequestHandler(url2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                sHtmlContent2 = oRequestHandler.request()

                sPattern3 = 'source: *["\'](.+?)["\']'
                aResult = re.findall(sPattern3, sHtmlContent2)
                if aResult:
                    sHosterUrl = 'http:' + aResult[0]
            sHosterUrl = sHosterUrl
        if 'tennistvgroup' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()

            sPattern2 = 'source: *["\'](.+?)["\']'
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'box-live.stream' in url:  # Terminé
            oRequestHandler = cRequestHandler(url)
            oRequestHandler.addHeaderEntry('User-Agent', UA)
            oRequestHandler.addHeaderEntry('Referer', sUrl4)

            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = 'source: \'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0] + '|User-Agent=' + UA + '&referer=' + url
            else:
                sPattern2 = 'var source = \"(.+?)\"'
                aResult = re.findall(sPattern2, sHtmlContent2)
                if aResult:
                    sHosterUrl = aResult[0]
                else:
                    sPattern2 = '<iframe.+?src="(http.+?)".+?</iframe>'
                    aResult = re.findall(sPattern2, sHtmlContent2)
                    if aResult:
                        Referer = url
                        url = aResult[0]  # decryptage plus bas (telerium)

        if 'telerium.tv' in url:  # WIP
            oRequestHandler = cRequestHandler(url)
            if Referer:
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', Referer)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
            aResult = re.findall(sPattern2, sHtmlContent2)

            if aResult:
                str2 = aResult[0]
                if not str2.endswith(';'):
                    str2 = str2 + ';'

                strs = cPacker().unpack(str2)

                sPattern3 = '{url:window\.atob\((.+?)\)\.slice.+?\+window\.atob\((.+?)\)'
                aResult1 = re.findall(sPattern3, strs)
                if aResult1:
                    m3u = aResult1[0][0]
                    sPatternM3u = m3u + '="(.+?)"'
                    m3u = re.findall(sPatternM3u, strs)
                    m3u = base64.b64decode(m3u[0])[14:]

                    token = aResult1[0][1]
                    sPatterntoken = token + '="(.+?)"'
                    token = re.findall(sPatterntoken, strs)
                    token = base64.b64decode(token[0])

                    sHosterUrl = 'https://telerium.tv/' + m3u + token + '|referer=' + url
            sHosterUrl = sHosterUrl
        # TODO A TESTER
        if 'usasports.live' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern1 = 'var sou = "  (.+?)"'
            aResult = re.findall(sPattern1, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        # TODO A TESTER
        if 'wiz1' in url:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern1 = '"iframe" src="(.+?)"'
            aResult = re.findall(sPattern1, sHtmlContent2)
            if aResult:
                sHosterUrl = aResult[0]
            sHosterUrl = sHosterUrl
        if 'var16.ru' in url:
            sHosterUrl = getHosterVar16(url, url)

        # TODO A TESTER
        if 'livesportone' in url:
            url = url.replace('livesportone.com', 'sportes.pw')

            oRequestHandler = cRequestHandler(url)
            sHtmlContent2 = oRequestHandler.request()
            sPattern2 = '<iframe src=\'(.+?)\''
            aResult = re.findall(sPattern2, sHtmlContent2)
            if aResult:
                sHosterUrl2 = aResult[0] + '|User-Agent=' + UA + '&referer=' + url
                oRequestHandler = cRequestHandler(sHosterUrl2)
                oRequestHandler.addHeaderEntry('User-Agent', UA)
                oRequestHandler.addHeaderEntry('Referer', url)
                sHtmlContent3 = oRequestHandler.request()
                sPattern3 = 'source: "([^"]+)"'
                aResult1 = re.findall(sPattern3, sHtmlContent3)
                if aResult1:
                    sHosterUrl = aResult1[0] + '|User-Agent=' + UA + '&referer=' + url
            sHosterUrl = sHosterUrl
        if 'acestream' in url:
            url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
            liz = xbmcgui.ListItem(name)
            liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
            liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage,
                    'fanart': fanart})
            liz.setPath(url)
            xbmc.Player().play(url1, liz, False)
            quit()
        if '/live.cdnz' in url:
            r = six.ensure_str(client.request(url, referer=BASEURL)).replace('\t', '')
        # xbmc.log("[{}] - HTML: {}".format(ADDON.getAddonInfo('id'), str(r)))
            from resources.modules import jsunpack
            if 'script>eval' in r:
                unpack = re.findall(r'''<script>(eval.+?\{\}\)\))''', r, re.DOTALL)[0]
                r = jsunpack.unpack(unpack.strip())
            # xbmc.log('RESOLVE-UNPACK: %s' % str(r), xbmc.LOGNOTICE)
            else:
                 r = r
        # xbmc.log("[{}] - HTML: {}".format(ADDON.getAddonInfo('id'), str(r)))
            if 'hfstream.js' in r:
                regex = '''<script type='text/javascript'> width=(.+?), height=(.+?), channel='(.+?)', g='(.+?)';</script>'''
                wid, heig, chan, ggg = re.findall(regex, r, re.DOTALL)[0]
                stream = 'https://www.playerfs.com/membedplayer/' + chan + '/' + ggg + '/' + wid + '/' + heig + ''
            else:
                if 'cbox.ws/box' in r:
                    try:
                       stream = client.parseDOM(r, 'iframe', ret='src', attrs={'id': 'thatframe'})[0]
                    except IndexError:
                       streams = client.parseDOM(r, 'iframe', ret='src')
                       stream = [i for i in streams if not 'adca.' in i][0]
                    # xbmc.log("[{}] - STREAM: {}".format(ADDON.getAddonInfo('id'), str(stream)))
                else:
                    stream = client.parseDOM(r, 'iframe', ret='src')[-1]
                # xbmc.log("[{}] - STREAM-ELSE: {}".format(ADDON.getAddonInfo('id'), str(stream)))
        # xbmc.log("[{}] - STREAM: {}".format(ADDON.getAddonInfo('id'), str(stream)))
            rr = client.request(stream, referer=url)
            rr = six.ensure_text(rr, encoding='utf-8').replace('\t', '')
            if 'eval' in rr:
                unpack = re.findall(r'''script>(eval.+?\{\}\))\)''', rr, re.DOTALL)[0]
            # unpack = client.parseDOM(rr, 'script')
            # xbmc.log('UNPACK: %s' % str(unpack))
            # unpack = [i.rstrip() for i in unpack if 'eval' in i][0]
                rr = six.ensure_text(jsunpack.unpack(str(unpack) + ')'), encoding='utf-8')
            else:
                r = rr
            if 'youtube' in rr:
                try:
                    flink = client.parseDOM(r, 'iframe', ret='src')[0]
                    fid = flink.split('/')[-1]
                except IndexError:
                    fid = re.findall(r'''/watch\?v=(.+?)['"]''', r, re.DOTALL)[0]
            # xbmc.log('@#@STREAMMMMM111: %s' % fid, xbmc.LOGNOTICE)

                flink = 'plugin://plugin.video.youtube/play/?video_id={}'.format(str(fid))
            # xbmc.log('@#@STREAMMMMM111: %s' % flink, xbmc.LOGNOTICE)

            else:
                if '<script>eval' in rr and not '.m3u8?':
                    unpack = re.findall(r'''<script>(eval.+?\{\}\))\)''', rr, re.DOTALL)[0].strip()
                # xbmc.log("[{}] - STREAM-UNPACK: {}".format(ADDON.getAddonInfo('id'), str(unpack)))
                    rr = jsunpack.unpack(str(unpack) + ')')
                # xbmc.log("[{}] - STREAM-UNPACK: {}".format(ADDON.getAddonInfo('id'), str(r)))
            # else:
            #     xbmc.log("[{}] - Error unpacking".format(ADDON.getAddonInfo('id')))
                if 'player.src({src:' in rr:
                    flink = re.findall(r'''player.src\(\{src:\s*["'](.+?)['"]\,''', rr, re.DOTALL)[0]
                # xbmc.log('@#@STREAMMMMM: %s' % flink, xbmc.LOGNOTICE)
                elif 'hlsjsConfig' in rr:
                    flink = re.findall(r'''src=\s*["'](.+?)['"]''', rr, re.DOTALL)[0]
                elif 'new Clappr' in rr:
                    flink = re.findall(r'''source\s*:\s*["'](.+?)['"]\,''', str(rr), re.DOTALL)[0]
                elif 'player.setSrc' in rr:
                    flink = re.findall(r'''player.setSrc\(["'](.+?)['"]\)''', rr, re.DOTALL)[0]

                else:
                    try:
                        flink = re.findall(r'''source:\s*["'](.+?)['"]''', rr, re.DOTALL)[0]
                    except IndexError:
                        ea = re.findall(r'''ajax\(\{url:\s*['"](.+?)['"],''', rr, re.DOTALL)[0]
                        ea = six.ensure_text(client.request(ea)).split('=')[1]
                        flink = re.findall('''videoplayer.src = "(.+?)";''', ea, re.DOTALL)[0]
                        flink = flink.replace('" + ea + "', ea)

                flink += '|Referer={}'.format(quote(stream)) #if not 'azcdn' in flink else ''
        # xbmc.log('@#@STREAMMMMM111: %s' % flink)
            sHosterUrl = flink
        if'//em.bedsport' in url or 'cdnz.one/ch' in url:
            referer = 'https://em.bedsport.live/'
            r = six.ensure_str(client.request(url, referer=referer))
            vid = re.findall(r'''fid=['"](.+?)['"]''', r, re.DOTALL)[0] #<script>fid='do4';
        #ragnaru.net/embed.php?player='+embedded+'&live='+fid+'" '+PlaySize+' width='+v_width+' height='+v_height+'
            host = 'https://ragnaru.net/embed.php?player=desktop&live={}'.format(str(vid))
            data = six.ensure_str(client.request(host, referer=referer))
            link = re.findall(r'''return\((\[.+?\])\.join''', data, re.DOTALL)[0]
            stream_url = link.replace('[', '').replace(']', '').replace('"', '').replace(',', '').replace('\/', '/')
            sHosterUrl += '|Referer=https://ragnaru.net/&User-Agent={}'.format(quote(ua))
        if 'nonameco' in url:
        #urll='https://bedsport.live/ch6.php'
            referer = '"https://wigistream.to/'
            r = six.ensure_str(client.request(url, referer=referer))
            logger.info("--r: %s" %str(r))
            frame = client.parseDOM(r, 'iframe', ret='src')[0]
            referer = '"https://wigistream.to/'
            data2 = six.ensure_str(client.request(frame, referer=referer))


            logger.info("data--r: %s" %str(data2))
            unpack = re.findall(r'''script>(eval.+?\{\}\))\)''', data2, re.DOTALL)[0]
            from resources.modules import jsunpack
            data1 = six.ensure_text(jsunpack.unpack(str(unpack) + ')'), encoding='utf-8')
            sHosterUrl = re.findall(r'''src=\s*["'](.+?)['"]''', data1, re.DOTALL)[0]+'|Referer=https://rallive.net/&User-Agent={}'.format(quote(ua))
            logger.info("data2 : %s" %str(data1))


        if '//bedsport' in url:
        #urll='https://bedsport.live/ch6.php'
            referer = 'https://bedsport.live/'
            r = six.ensure_str(client.request(url, referer=referer))
            logger.info("--r: %s" %str(r))
            frame = client.parseDOM(r, 'iframe', ret='src')[0]
            referer = 'https://bedsport.live/'
            data2 = six.ensure_str(client.request(frame, referer=referer))


            logger.info("data--r: %s" %str(data2))
            unpack = re.findall(r'''script>(eval.+?\{\}\))\)''', data2, re.DOTALL)[0]
            from resources.modules import jsunpack
            data1 = six.ensure_text(jsunpack.unpack(str(unpack) + ')'), encoding='utf-8')
            sHosterUrl = re.findall(r'''src=\s*["'](.+?)['"]''', data1, re.DOTALL)[0]+'|Referer=https://rallive.net/&User-Agent={}'.format(quote(ua))
            logger.info("data2 : %s" %str(data1))
       # refere = 'https:/sopertyvalua.com/'
       # data = six.ensure_str(client.request(flink, referer=refere))
       # logger.info("data: %s" %str(data))

        # xbmc.log('UNPACK: %s' % str(unpack))
        # unpack = [i.rstrip() for i in unpack if 'eval' in i][0]
        #logger.info("unpack: %s" %strunpack)


          
        # Tentative avec les pattern les plus répendus
        liz = xbmcgui.ListItem(name)
        liz.setArt({'poster': 'poster.png', 'banner': 'banner.png'})
        liz.setArt({'icon': iconimage, 'thumb': iconimage, 'poster': iconimage, 'fanart': fanart})
        liz.setInfo(type="Video", infoLabels={"Title": name})
        liz.setProperty("IsPlayable", "true")
        liz.setPath(str(sHosterUrl ))
    # if float(xbmc.getInfoLabel('System.BuildVersion')[0:4]) >= 17.5:
    #     liz.setMimeType('application/vnd.apple.mpegurl')
    #     liz.setProperty('inputstream.adaptive.manifest_type', 'hls')
    #     liz.setProperty('inputstream.adaptive.stream_headers', str(headers))
    # else:
    #     liz.setProperty('inputstreamaddon', None)
    #     liz.setContentLookup(True)
        xbmc.Player().play(sHosterUrl , liz, False)
        quit()
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), False, liz)



        oGui.setEndOfDirectory()

def getHosterVar16(url, referer):
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()

    sPattern = 'file:\"([^"]+)\"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] + '|referer=' + url
    
    sPattern = 'src=\"(.+?)\"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        referer = url
        url = 'http://var16.ru/' + aResult[0]
        return getHosterVar16(url, referer)
    

# Traitement générique
def getHosterIframe(url, referer):
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()
    logger.info("url--r: %s" %str(url))
    logger.info("sHtmlContent--r: %s" %str(sHtmlContent))
    sPattern = '[^/]sourc.+?["\'](http.+?)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] + '|referer=' + url
    
    sPattern = '<iframe.+?src=["\']([^"\']+)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        referer = url
        url = aResult[0]
        if not url.startswith("http"):
            if not url.startswith("//"):
                url = '//'+referer.split('/')[2] + url  # ajout du nom de domaine
            url = "https:" + url
        return getHosterIframe(url, referer)
    
    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
    aResult = re.findall(sPattern, sHtmlContent)

    if aResult:
        sstr = aResult[0]
        if not sstr.endswith(';'):
            sstr = sstr + ';'
        sUnpack = cPacker().unpack(sstr)
        sPattern = 'src="(.+?)"'
        aResult = re.findall(sPattern, sUnpack)
        if aResult:
            return aResult[0] #+ '|Referer=' + url
    if  "noob4cast.com"  in sHtmlContent:
       sHtmlContent = sHtmlContent.replace("'", '"')

    sPattern =  'fid="(.+?)"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
            code = aResult[0]
            Url='https://noob4cast.com/fsembed.php?player=desktop&live='+ code                                              
            sHtmlContent=gegetHtml(Url)
            sHtmlContent = sHtmlContent.replace('return(["h', 'return"h').replace('"].join("") ', '"').replace('\/', '/').replace('","', '')
            logger.info("sHtmlConten: %s" % sHtmlContent)
            U = re.search('return"(.+?)"', sHtmlContent).group(1)
            return U+'|Referer=https://noob4cast.com/'


    if  "atob('"  in sHtmlContent:
       sHtmlContent = sHtmlContent.replace("'", '"')

    sPattern =  '.atob\("(.+?)"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        import base64
        code = aResult[0]
        logger.info("code--r: %s" %str(code))
        try:
            if isMatrix():
                code = base64.b64decode(code).decode('ascii')
            else:
                code = base64.b64decode(code)
            return  code# + '|Referer=' + url
        except Exception as e:
            pass
        
def RetRealUrl(chain):  # Recupere les liens des regex
#    url =url.replace('https://href.li/?', '')
    r = re.search('<iframe src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('<iframe width=".+?" height=".+?" src="(.+?)"', chain)
    if (r):        
        url = r.group(1)
        return url
    r = re.search('<iframe allowFullScreen frameborder=0 marginheight=0 marginwidth=0 scrolling=.+?src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url     
    r = re.search('<iframe frameborder="no" height=".+?" src="(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    r = re.search('"0;URL=(.+?)"', chain)
    if (r):
        url = r.group(1)
        return url
    
    
def getHosterIframe2(sHtmlContent):
#    sHtmlContent = getHtml(url)
    if  "atob('"  in sHtmlContent:
       sHtmlContent = sHtmlContent.replace("'", '"')
    logger.info("sHtmlContent: %s" %str(sHtmlContent))
    sPattern =  '.atob\("(.+?)"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        import base64
        code = aResult[0]
        try:
            if isMatrix():
                code = base64.b64decode(code).decode('ascii')
            else:
                code = base64.b64decode(code)
            return  code 
        except Exception as e:
            pass
        




