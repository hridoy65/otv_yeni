# -*- coding: utf-8 -*-
import sys, os, re, codecs, xbmcplugin, xbmcgui, xbmcaddon, xbmc, xbmcvfs, threading, webbrowser
import json, hashlib, os.path, time, inspect, codecs
from contextlib import closing
from xbmcvfs import File
from resources.scripts import parsers
#from resources.lib.logger import logger   
from resources.sites.LIVETV2 import *
try:
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import quote_plus as Quote_plus
    from urllib.parse import unquote as Unquote
    from urllib.parse import quote as Quote
    from urllib.parse import unquote_plus as Unquote_plus
    isPy3 = True
except:
    from urllib import urlencode as Urlencode
    from urllib import quote_plus as Quote_plus
    from urllib import unquote as Unquote
    from urllib import quote as Quote
    from urllib import unquote_plus as Unquote_plus
    isPy3= False
    
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')

try:
    info = xbmc.getInfoLabel('System.BuildVersion')
    ver =int( re.findall('(^\d+).*?', info)[0])
except:
    ver = 18
    
class MyPlayer(xbmc.Player):
    def __init__( self, *args, **kwargs ):
        xbmc.Player.__init__( self )
        self.s = 0
        self.isfirst = 1
        self.curPos = 0
        self.audiostream =[]    
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
            
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname.encode('UTF-8').decode('utf-8'), "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def kok():
    return settings.getSetting('root')

tokens=kok().split('/')
root2= '/'.join(tokens[:-2])
logger.info('root2)>%s' % root2)
m_id = 0
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
IMAGES_PATH = xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'media'))
ADDON_PATH =  xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path')))
__addonuserdata__    = xbmc.translatePath(settings.getAddonInfo('profile'))
osInfo = xbmc.getInfoLabel('System.OSVersionInfo')
i = 1
temp = xbmc.translatePath("special://temp")

while osInfo == xbmc.getLocalizedString(503).encode("utf8"):
    i = i+1
    osInfo = xbmc.getInfoLabel('System.OSVersionInfo') 
    time.sleep(1)
    if i == 10:
        break
sysInfo = xbmc.getInfoLabel('System.FriendlyName')
if not settings.getSetting( "recorded_date") or settings.getSetting('recorded_date') == "01-01-2020":
    settings.setSetting('recorded_date', xbmc.getInfoLabel('System.Date(dd-mm-yyyy)'))
    
vidName = 'seyirTURK'
#vidName = xbmcaddon.Addon(vidName).getAddonInfo('name')
logger.info('vidName>%s' % vidName)
dialog = xbmcgui.Dialog()
if settings.getSetting('uclugorunum') == "true":
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
tc = hashlib.md5(vidName.encode()).hexdigest()
logger.info('tc>%s' % tc)
#tc ='b106dc966238b027c5fc2af0327f6280'
#      5ecc2a90d157b2f5a9391ff42106ac69
def macaddress():
    try:
        if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/KodiLite"):
            try:
                from Components.Network import iNetwork
                ifaces = iNetwork.getConfiguredAdapters()
                mac_id = iNetwork.getAdapterAttribute(ifaces[0], 'mac')
                settings.setSetting('mac_add', mac_id)
            except:
                pass
        else:
            mac_id = xbmc.getInfoLabel('Network.MacAddress')
            i = 1
            while mac_id == xbmc.getLocalizedString(503).encode("utf8"):
                i = i+1
                mac_id = xbmc.getInfoLabel('Network.MacAddress') 
                time.sleep(1)
                if i == 10:
                    break
            if  not ('gul' in mac_id or 'usy' in mac_id or mac_id == "" or mac_id == " " or "Occup" in mac_id or "Zaj" in mac_id or 'Besch' in mac_id or 'Bezig' in mac_id):
                settings.setSetting('mac_add', mac_id)
            else:
                settings.setSetting('mac_add', '00:00:00:00:00:00')
    except:
        settings.setSetting('mac_add', '00:00:00:00:00:00')

if not settings.getSetting('mac_add') or settings.getSetting('mac_add')=="" or settings.getSetting('mac_add')==" " or "Occup" in  settings.getSetting('mac_add') or "Zaj" in settings.getSetting('mac_add') or 'gul' in  settings.getSetting('mac_add') or 'usy' in  settings.getSetting('mac_add') or '00:00:00:00:00' in  settings.getSetting('mac_add') or 'Besch' in  settings.getSetting('mac_add') or 'Bezig' in  settings.getSetting('mac_add'):
        macaddress()

def message():        
    try:
        surum = settings.getAddonInfo('version')
        if settings.getSetting("surum_kontrol") == "-1":
            settings.setSetting('surum_kontrol', surum)
        surum = settings.getSetting("surum_kontrol")
        mesaj_page = parsers.fetch(root2 + '/mesaj.php?surum=' + surum)
        mesaj_json = json.loads(mesaj_page)
        mesaj = mesaj_json["message"][0]["mesaj"]
        u_mesaj = mesaj_json["message"][0]["u_mesaj"]
        flag = mesaj_json["message"][0]["flag"]
        u_flag = mesaj_json["message"][0]["u_flag"]
        is_user_active = mesaj_json["message"][0]["isUserActive"]
        if is_user_active == 0:
            settings.setSetting('mail', '')
            settings.setSetting('sifre', '')
            settings.setSetting('e_mail', '')
            settings.setSetting('user_id', '')
        if settings.getSetting("message") != flag:
            ok1 = dialog.ok("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR] Mesajınız var !", mesaj)
            settings.setSetting('message', flag)
        if settings.getSetting("u_message") != u_flag and u_flag != '' and u_mesaj != '':
            ok1 = dialog.ok("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]", u_mesaj)
            settings.setSetting('u_message', u_flag)
        cache_key = mesaj_json["message"][0]["cache_key"]
        if  cache_key != settings.getSetting("cache_key_local"):
            parsers.cache_clear()
            settings.setSetting("temp_watched","mids")
        settings.setSetting("cache_key_local",cache_key)
        update_text = mesaj_json["message"][0]["surum"]
        if 'eski_surum' in update_text:
            update(update_text,surum)
    except:
        pass
    
def save_m3u_link():
    if 'http' in settings.getSetting('m3u'):
        try:
            v = parsers.fetch(settings.getSetting('m3u'))
            if '#EXTINF' in v:
                with codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"gecici.m3u")), "w+", "utf-8-sig") as out:
                    out.write(parsers.to_utf8(v))
        except:
            pass

def Baslat(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    maina(Url)
def Basla(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    listele(Url)
def ayarlar():
    __settings__ = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
    __settings__.openSettings()


def maina(url):
  #  url = root2 + '/kodi/main.php?ct=' + tc
                logger.info('url>%s' % url)
                f = parsers.fetch(url)
                logger.info('f>%s' % f)
                jr = json.loads(f)
                for js in jr["movies"]:
                    idx = js["ID"]
                    baslik = js["Name"]
                    sign = '?'
                    logger.info('baslik>%s' % baslik)
                    try:
                        resim = js["Image"]
                    except:
                        resim = ""
                    link = js["Link"] + sign + 'ct=' + tc
                    desc = None
                    addDir('[COLOR blue]>>> [/COLOR]'+ baslik +'[/B][/COLOR]',Quote_plus(link),302,resim,idx, desc, None)
                

                

def main():
    url = root2 + '/kodi/main.php?ct=' + tc
    page = parsers.cache(url)
    if page != "":
        jr = json.loads(page)
        for rj in jr["main"]:
            link = rj["link"]
            resim = rj["icon"]
            isim = rj["title"]
            try:
                fanart ="https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/fanart.jpg"#.replace(' hd','https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/icon.png')
            except:
                fanart = resim
            try:
                desc = rj["Summary"]
            except:
                desc=""
            sign ='?'
            if '?' in link:
                sign = '&'
            link = link   + sign + 'ct=' + tc
            if '&id=' in link:
                link = link.replace('&id=','') + '&id='
            if '/iptv.php' in link: 
                link = link 
            if settings.getSetting('isAdult') == "Rabbit" and settings.getSetting( "user_id" ) :
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]'+isim+'[/B][/COLOR]',Quote_plus(link),2,resim, 0, desc, None,fanart)
            else:
                if not 'Adult' in isim:
                    addDir('[COLOR orange][B][COLOR blue]> [/COLOR]'+isim+'[/B][/COLOR]',Quote_plus(link),2,resim, 0, desc,None,fanart)

        if settings.getSetting('m3u'):
            if 'type=m3u'in settings.getSetting('m3u') or '.m3u'in settings.getSetting('m3u') :
                linkos = Quote(settings.getSetting('m3u'))
                desc = '[COLOR orange][B]seyirTURK[/B][/COLOR] te kendi kendi IPTV lerinizi bu alanda bulabilirsiniz.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Benim Iptv[/B][/COLOR]',linkos,2,os.path.join(IMAGES_PATH, 'myiptv.png'),0, desc,None,fanart)
                
        desc = '[COLOR orange][B]seyirTURK[/B][/COLOR] hakkımızdaki bilgileri görebileceğiniz alan.'
        addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Bilgiler[/B][/COLOR]','bilgiler.php',5,os.path.join(IMAGES_PATH, 'info2.png'),0, desc, None, fanart, "0", "bilgiler")

        desc = '[COLOR orange][B]seyirTURK[/B][/COLOR] ayarlarını yapabileceğiniz alan.'
        addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Ayarlar[/B][/COLOR]','main.php',5,os.path.join(IMAGES_PATH, 'settings.png'),0, desc, None, fanart,"0","ayarlar")



    
def listele(url):
        
#        url='http://cekke.tk/sey/kodi/iptv/bluetv/online.php?ct=75401a547f0f5c34c1e2597ef10fd2c6'
        logger.info('url>%s' % url)
        kokd = kok()
        isSearchNegative = 0
        searchstring=""


        if ("?name" in url or '&name' in url) and not ('isAdult=1&name=' in url or 'iptv/search.php?name=' in url):
                key = dialog.select('', ['[B]Dublaj yada Altyazı Önemsiz[/B]', '[B]Türkçe Dublaj[/B]', '[B]Türkçe Altyazı[/B]', '[B]Almanca Dublaj[/B]', '[B]Kişi Arama[/B]'])
                if key != -1:
                    keyboard = xbmc.Keyboard( '', "Arama", False )
                    keyboard.doModal()
                    if ( keyboard.isConfirmed() ):
                            searchstring = keyboard.getText().strip()
                            if key== 0:
                                substring = ''
                            elif key == 1:
                                substring = '&lang=DUB'
                            elif key == 2:
                                substring = '&lang=SUB'
                            elif key == 3:
                                substring = '&lang=GER'
                            else:
                                substring = ''
                                url = url.replace("p_type=Movie","p_type=person").replace("p_type=TV","p_type=person")
                            url = url.replace('name=', 'name=' + Quote(searchstring) + substring)
                    else:
                        isSearchNegative = 1

                else:
                    isSearchNegative = 1
        elif 'isAdult=1&name=' in url or 'iptv/search.php?name=' in url:
            keyboard = xbmc.Keyboard( '', "Arama", False )
            keyboard.doModal()
            if ( keyboard.isConfirmed() ):
                searchstring = keyboard.getText().strip().replace(" ", "%20")
                url = url.replace('name=', 'name=' + searchstring)
            else:
                isSearchNegative = 1
            
            
        if 'type=user' in url or 'type=history' in url:
            if settings.getSetting( "user_id" ):
                url = url + settings.getSetting( "user_id" )
            else :
                ok = dialog.ok("","Girmek istediğiniz yer için lütfen ayarlardan kullanıcı girişi yapınız.")
                url = "bos"

        else :
            pass
        if "seyirturkelkitabi" in url:
            try:
                webbrowser.open("https://seyirturk.tk/kullanici-el-kitabi/")
            except:
                parsers.showMessage("","[COLOR orange][B]Cihazınızda herhangi bir internet tarayıcısı yok![/B][/COLOR]")
            url = "bos"
        
        if url!="bos" :
            if "adult" in url or "%2b18" in url or "erotik" in url or "yetiskin" in url or "Erotik" in url or "Yetiskin" in url:
                if settings.getSetting( "isAdult" ) == "Rabbit":			
                    k = xbmc.Keyboard('', 'Yetişkin Şifresini Giriniz') ; k.doModal()
                    pin = k.getText()
                    if k.isConfirmed():
                        if pin != settings.getSetting( "isAdultkey" ):
                            isSearchNegative = -1
                            url='/'.join(kokd.split('/')[:-2]) + '/kodi/main.php'
                    else:
                        isSearchNegative = 1
                        url='/'.join(kokd.split('/')[:-2]) + '/kodi/main.php'
            else:
                pass
            if url.startswith('http'):
                if settings.getSetting('m3u') == url:
                    try:
                        url11 = os.path.join(__addonuserdata__,'gecici.m3u' )
                        cc = open(url11,'r')
                        data1 = cc.read()
                        cc.close()
                        f = data1
                    except:
                        parsers.showMessage("","[COLOR orange][B]Girdiğiniz linkte m3u bulunamadı![/B][/COLOR]")
                        f = ''
                else:
                    f = parsers.cache(url)
                    logger.info('ffff>%s' % f)
            else:
                if "bilgiler.php" not in url:
                    url1 = os.path.join(__addonuserdata__, settings.getSetting('m3u') )
                    c = open(url1,'r')
                    data = c.read()
                    c.close()
                    f = data
                else:
                    f=''


            if "movies" in f and not 'm3u' in url:
                    js = json.loads(f)
                    idx = '0'
                    if 'miptv.php' in url and not 'Adultkodiiptv.php' in url:
                        link = url 
                        addDir('[COLOR blue]> [/COLOR] IPTV [/B][/COLOR]',Quote_plus(link),302,os.path.join(IMAGES_PATH, 'ara.png'),'0', 'desc', None)
                    for rs in js['movies']:
                            language = ''
                            son_ek = ''
                            try:
                                hw = int(rs['hasWatched'])
                            except:
                                hw = 0
                            if str(rs['ID']) in settings.getSetting("temp_watched") or hw > 0:
                                son_ek = "[COLOR white] - İzlendi[/COLOR]"
                            try:
                                language_int = rs['Language']
                                if language_int == "6":
                                    language = "[COLOR grey] TA - TD - GE[/COLOR]" + son_ek
                                elif language_int == "5":
                                    language = "[COLOR yellow] TD - GE[/COLOR]" + son_ek
                                elif language_int == "4":
                                    language = "[COLOR purple] TA - GE[/COLOR]" + son_ek
                                elif language_int == "3":
                                    language = "[COLOR orange] GE[/COLOR]" + son_ek
                                elif language_int == "2":
                                    language = "[COLOR blue] TA - TD[/COLOR]" + son_ek
                                elif language_int == "1":
                                    language = "[COLOR green] TD[/COLOR]" + son_ek
                                elif language_int == "0":
                                    language = "[COLOR red] TA[/COLOR]" + son_ek
                            except:
                                pass
                            baslik = rs['Name'] + language
                            try:
                                if 'Erotik' in rs["Genres"]:
                                    baslik = rs['Name']
                            except:
                                pass
                            resim = rs['Image']
                            try:
                                fanart ="https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/fanart.jpg"#.replace(' hd','https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/icon.png')
                            except:
                                fanart = resim
                            try:
                                imdbscore = rs["IMDBScore"]
                            except:
                                imdbscore = 'NA'
                            try:
                                releasedate = rs["ReleaseDate"]
                            except:
                                releasedate = 'NA'
                            try:
                                genres = rs["Genres"]
                            except:
                                genres = 'NA'
                            try:
                                try:
                                    if settings.getSetting('uclugorunum') == "true":
                                        desc = '[COLOR green][B]IMDb: ' + imdbscore +'[/COLOR][COLOR blue] Tarih: ' + releasedate.replace(' 00:00:00','') + '[/COLOR][/B]\n[COLOR yellow]Türler: ' + genres + '[/COLOR]\n' + rs['Summary']
                                        if   'turler.php' in url or 'turlerdizi.php' in url or 'diziler.php' in url or 'filmler.php' in url :
                                            desc = rs['Summary'] 
                                    else:
                                        desc =  baslik.replace(' TD','').replace(' TA','').replace(' TA - TD',''.replace(" GE","") ).replace("-","") +  '\n' +'[COLOR green][B]IMDb: ' + imdbscore +'[/COLOR][COLOR blue] Tarih: ' + releasedate.replace(' 00:00:00','') + '[/COLOR][/B]\n[COLOR yellow]Türler: ' + genres + '[/COLOR]\n' + rs['Summary']
                                        if   'turler.php' in url or 'turlerdizi.php' in url or 'diziler.php' in url or 'filmler.php' in url :
                                            desc =  baslik.replace(' TD','').replace(' TA','').replace(' TA - TD',''.replace(" GE","") ).replace("-","") + '\n' + rs['Summary']  
                                            
                                except:
                                    desc = None
                                try:
                                    idx = str(rs['ID'])
                                except:
                                    pass
                                try :
                                    tip = rs["Type"]
                                except:
                                    tip ='Yok'
                                try:
                                    sign ='?'
                                    if '?' in rs['Link']:
                                        sign = '&'
                                    link = rs['Link']  + sign + 'ct=' + tc
                                except:
                                    if tip == 'Movie' or tip == 'yok':
                                        link = kokd + 'streams.php?id=' + idx
                                    else:
                                        link = kokd + 'episodes.php?id=' + idx
                                if 'show.php?type=user' in url:
                                    addDir(''+ baslik +'',Quote_plus(link),302,resim, idx, desc, None)

                                else:
                                    if not 'type=random' in url:
                                        isAdult = 0
                                        try:
                                            if rs["isAdult"] == "1":
                                                isAdult = 1
                                        except:
                                            pass
                                        if isAdult != 1 and 'Adult' not in url:
                                            addDir('[COLOR blue]* [/COLOR]'+ baslik +'',Quote_plus(link),302,resim,idx, desc, None, fanart)
                                        if settings.getSetting('isAdult') == "Rabbit" and settings.getSetting( "user_id" ) and 'Adult' in url:
                                            if "mainprovider" in url:
                                                addDir('[COLOR blue]{f} [/COLOR]'+ baslik + son_ek +'',Quote_plus(link),302,resim,idx, desc, None, fanart)
                                            elif "Adultfilmler.php" in url:
                                                addDir('[COLOR blue]{} [/COLOR]'+ baslik +'',Quote_plus(link),302,resim,idx, desc, None, fanart)
                                            elif "iptvmain_adult.png" in f:
                                                addDir('[COLOR blue]{tv} [/COLOR]'+ baslik +'',Quote_plus(link),302,resim,idx, desc, None, fanart)
                                            else:
                                                addDir('[COLOR blue]{c} [/COLOR]'+ baslik +'',Quote_plus(link),302,resim,idx, desc, None, fanart)
                                    else:
                                        listele(link)
                            except:
                                pass 
            elif "links" in f:
                try:
                    m_id = re.findall('id=([0-9]+)',url)[0]
                except:
                    m_id = None
                try:
                    ee_id = re.findall('&e_id=([0-9]+)',url)[0]
                except:
                    ee_id = 'yok'
                try:
                    if ee_id == 'yok':
                        timestamp = parsers.fetch(kokd + 'save.php?type=g&m_id=' + m_id )
                    else:
                        timestamp = parsers.fetch(kokd + 'save.php?type=g&isTv=1&m_id=' + ee_id)
                except:
                    timestamp = 0
                logger.info('f>%s' % f)
                jr = json.loads(f)
                logger.info('jr)>%s' % jr)
                for rj in jr["links"]:
                    link = Quote(rj["Link"].encode('UTF-8'))
                    try:
                        e_id = rj["E_ID"]
                    except:
                        e_id = "0"
                    releasedate = 'NA'
                    name_from_labelinfo = (xbmc.getInfoLabel('ListItem.Title').replace("*","").replace(' TD','').replace(' TA','').replace(' TA - TD','').replace(" GE","").replace("-","").replace("(4K)","") ).encode('utf-8').decode('utf-8')
                    if "rastgele" in name_from_labelinfo.lower():
                        name_from_labelinfo = '' + rj["name"] 
                    if name_from_labelinfo != "":
                        settings.setSetting("gecici_isim", name_from_labelinfo)
                    if name_from_labelinfo == "":
                        name_from_labelinfo = settings.getSetting("gecici_isim")
                    try:
                        provider = rj["Provider"]
                        desc = rj["Summary"]
                        turkish = int(rj["isTurkish"])
                        try:
                            imdbscore = rj["IMDBScore"]
                        except:
                            imdbscore = 'NA'
                        try:
                            releasedate = rj["ReleaseDate"]
                        except:
                            pass
                        if turkish == 0 :
                            dil = '[COLOR red] TA[/COLOR]'.encode('UTF-8').decode("utf-8")
                        elif turkish == 1 :
                            dil = '[COLOR green] TD[/COLOR]'.encode('UTF-8').decode("utf-8")
                        elif turkish == 2 :
                            dil = '[COLOR blue] TA - TD[/COLOR]'.encode('UTF-8').decode("utf-8")
                        elif turkish == 3 :
                            dil = '[COLOR orange] AD[/COLOR]'.encode('UTF-8').decode("utf-8")
                        elif turkish == 4 :
                            dil = ''
                        if 'yourt' in url :
                            baslik =  '[COLOR blue][B][COLOR red]> [/COLOR]' + rj['Name']  +''
                        elif rj["MainProvider"] == "streamingporn" or rj["MainProvider"] == "sex-empire"or rj["MainProvider"] == "freomovie"or rj["MainProvider"] == "pandamovie":
                            baslik = name_from_labelinfo + '[COLOR white][B]- ' + ' ' + provider  +''
                        else:
                            baslik = name_from_labelinfo + ' - ' + provider + dil

                    except :
                        provider = rj['Name']
                        desc = '' + provider +''
                        try:
                            page = codecs.open(xbmc.translatePath(os.path.join(__addonuserdata__,"day")),'r',"utf-8-sig").read()
                            js = json.loads(page)
                            desc = ""
                            for i, j in enumerate(js["content"]):
                                channel =  j["channel"].lower().replace(' hd','').replace(' tv','')
                                name = j["name"]
                                start = j["start"]
                                finish = j["finish"]
                                type = j["type"]
                                if type == '':
                                    type = parsers.to_utf8('Diğer')
                                if provider.lower().replace(' hd','').replace(' tv','') in channel:
                                    desc = desc + '[COLOR orange]' + start + '-' + finish + '[/COLOR] ' + name[0:21] + '\n'
                        except:
                            pass
                        dil = ""
                        if 'Adult' not in url:
                            if 'faviptv.php' in url:
                                baslik =  '[COLOR blue][B][COLOR red]« [/COLOR]' + rj['Name']  +''
                            else:
                                baslik =  '[COLOR blue][B][COLOR red]» [/COLOR]' + rj['Name']  +''
                        else:
                            baslik =  '[COLOR blue][B][COLOR red]> [/COLOR]' + rj['Name']  +''
                    resim = rj["Image"]
                    try:
                        genres = rj["Genres"]
                    except:
                        genres = 'NA'
                    try:
                        film_adi ='' + rj["name"] 
                    except:
                        film_adi = ""
                        pass
                    if releasedate == 'NA':
                        desc1 = desc
                    else:
                        desc1 = '[COLOR green][B]IMDb: ' + imdbscore +'[/COLOR][COLOR blue] Tarih: ' + releasedate.replace(' 00:00:00','') + '[/COLOR][/B]\n[COLOR yellow]Türler: ' + genres + '[/COLOR]\n'  + desc
                    if e_id != "0":
                        isTv = "1"
                        m_id = rj["E_ID"]
                    else :
                        isTv = "0"
                    addDir(baslik, link, 303, resim, m_id, desc1, timestamp, resim, isTv)
            elif "bilgiler.php" in url:
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] istatistiklerini görebileceğiniz alan.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]İstatistik[/B][/COLOR]','istatistik.php',5,os.path.join(IMAGES_PATH, 'stat.png'),0, desc, None, os.path.join(IMAGES_PATH, 'stat.png'),"0",'istatistik')
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] sürüm notlarını görebileceğiniz alan.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Sürüm Notları[/B][/COLOR]','surum.php',5,os.path.join(IMAGES_PATH, 'vers.png'),0, desc, None, os.path.join(IMAGES_PATH, 'vers.png'),"0", "surum")
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] hakkımızdaki bilgileri görebileceğiniz alan.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Hakkında[/B][/COLOR]','hakkinda.php',5,os.path.join(IMAGES_PATH, 'info.png'),0, desc, None, os.path.join(IMAGES_PATH, 'info.png'),"0","hakkında")
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] VIP üyelik hakkında bilgi alabileceğiniz alan.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]VIP bilgi[/B][/COLOR]','vip_uyelik.php',5,os.path.join(IMAGES_PATH, 'vip.png'),0, desc, None, os.path.join(IMAGES_PATH, 'vip.png'),"0","vip")
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] Yasal bilgi alabileceğiniz alan.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]Yasal bilgi[/B][/COLOR]','yasal.php',5,os.path.join(IMAGES_PATH, 'yasal.png'),0, desc, None, os.path.join(IMAGES_PATH, 'yasal.png'),"0","yasal")
                desc = '[COLOR orange][B]OTV_MEDIA[/B][/COLOR] OTV_MEDIA kullanımı hakkında bilgi alabileceğiniz alan. Bu kısmı seçtiğinizde sisteminizde yüklü bulunan internet tarayıcısı açılacaktır.'
                addDir('[COLOR orange][B][COLOR blue]> [/COLOR]OTV_MEDIA Kullanıcı Elkitabı[/B][/COLOR]','OTV_MEDIAelkitabi.php',302,os.path.join(IMAGES_PATH, 'handbook.png'),0, desc, None, os.path.join(IMAGES_PATH, 'yasal.png'),"0","yasal")
            elif ".m3u" in url or "type=m3u" in url:
                channels = m3uarray(f)
                tip = re.findall('.*?#(.*?)$',url)
                kategoriler =sorted(Remove(channels[0]))
                if not tip and len(channels[0]) > 0 and len(kategoriler) > 1:
                    for a in kategoriler:
                        baslik = a
                        if a == "":
                            baslik = "Kategorisiz"
                        desc = "[COLOR orange][B]OTV_MEDIA[/B][/COLOR] IPTV nizin kategorisi."
                        addDir('[COLOR blue][B]~ ' + parsers.to_utf8(baslik) + '',Quote(parsers.to_utf8(url) + '#' + parsers.to_utf8(a)),302,os.path.join(IMAGES_PATH, 'kategori.png'),None, desc,None)
                else:
                    x = 0
                    for channel in channels[3]:
                        isim = channels[2][x].encode('UTF-8').decode("utf8").replace('\n','').replace('\r','')
                        link = channel.strip()
                        resim = channels[1][x]
                        desc = "IPTV Kanalı"
                        if len(resim) == 0:
                            resim = os.path.join(IMAGES_PATH, 'iptv.png')
                        try:
                            if tip[0] in channels[0][x]:
                                addDir('[COLOR blue][B]> '+isim+'[/B][/COLOR]', Quote(link), 303, resim, None, desc, None)
                        except:
                            addDir('[COLOR blue][B]> '+isim+'[/B][/COLOR]', Quote(link), 303, resim, None, desc, None)
                        x=x+1
            elif 'episodes.php' in url: 
                f = parsers.cache(url)
                logger.info('ffff>%s' % f)
                jr = json.loads(f)
                for js in jr["episodes"]:
                    idx = js["ID"]
                    baslik = js["Name"]
                    resim = js["Image"]
                    e_id = js["E_ID"]
                    season = js["Season"]
                    episode = js["Episode"]
                    try:
                        imdbscore = js["IMDBScore"]
                    except:
                        imdbscore = 'NA'
                    try:
                        releasedate = js["ReleaseDate"]
                    except:
                        releasedate = 'NA'
                    try:
                        genres = js["Genres"]
                    except:
                        genres = 'NA'
                    try:
                        language_int = rs['Language']
                        if language_int == "6":
                            language = "[COLOR grey] TA - TD - GE[/COLOR]"
                        elif language_int == "5":
                            language = "[COLOR yellow] TD - GE[/COLOR]"
                        elif language_int == "4":
                            language = "[COLOR purple] TA - GE[/COLOR]"
                        elif language_int == "3":
                            language = "[COLOR orange] GE[/COLOR]"
                        elif language_int == "2":
                            language = "[COLOR blue] TA - TD[/COLOR]"
                        elif language_int == "1":
                            language = "[COLOR green] TD[/COLOR]"
                        elif language_int == "0":
                            language = "[COLOR red] TA[/COLOR]"
                    except:
                        language = ''
                    kaldigim_bolum = str(js["isLeft"])
                    baslik1 = js['Name']
                    baslik = js['Name'] + '  S' + str(season) + 'B' + str(episode)
                    baslik = baslik + language
                    if  kaldigim_bolum == '1':
                        baslik = baslik + '[COLOR red][B] ►[/COLOR]'.encode('UTF-8').decode('utf-8')
                    link = kokd + 'streams.php?id=' + str(idx) +'&isTv=1&e=' + str(episode) + '&s=' + str(season) + '&e_id=' + str(e_id)
                    try:
                        if settings.getSetting('uclugorunum') == "true":
                            desc = '[COLOR green][B]IMDb: ' + imdbscore +'[/COLOR][COLOR blue] Tarih: ' + releasedate.replace(' 00:00:00','') + '[/COLOR][/B]\n[COLOR yellow]Türler: ' + genres + '[/COLOR]\n'  + js['Summary']
                        else:
                            desc = '' + baslik1 + '' + '\n' + '[COLOR green][B]IMDb: ' + imdbscore +'[/COLOR][COLOR blue] Tarih: ' + releasedate.replace(' 00:00:00','') + '[/COLOR][/B]\nCOLOR yellow]Türler: ' + genres + '[/COLOR]\n'  +  + js['Summary']
                    except:
                        desc = None

                    addDir(''+ baslik +'',Quote_plus(link),302,resim,idx, desc, None)

            elif '"person":' in f:
                jr = json.loads(f)
                for js in jr["person"]:
                    idx = js["ID"]
                    baslik = js["Name"]
                    try:
                        resim = js["Image"]
                    except:
                        resim = ""
                    link = js["Link"]
                    desc = None
                    addDir('[COLOR blue]>>> [/COLOR]'+ baslik +'[/B][/COLOR]',Quote_plus(link),302,resim,idx, desc, None)
                    
            else:
                    xbmc.executebuiltin('Action(back)')
                    if isSearchNegative == 0:
                        if 'name=' not in url and "0 Games" not in f:
                            parsers.showMessage("[COLOR orange][B]OTV_MEDIA KODI[/B][/COLOR]", "Link Bulunamadı!")
                        elif "0 Games" not in f:
                            parsers.showMessage("[COLOR orange][B]OTV_MEDIA KODI[/B][/COLOR]","Arama sayfası boş döndü.")
                        elif "0 Games" in f and "istory" in url:
                            parsers.showMessage("[COLOR orange][B]OTV_MEDIA KODI[/B][/COLOR]","İzlemeye Başladıklarım bölümü boş!.")
                    if isSearchNegative == -1:
                        parsers.showMessage("[COLOR orange][B]OTV_MEDIA KODI[/B][/COLOR]","Şifreniz yanlış. Kod: -1")

        else:
            mania()
def oynat(url,baslik,resim,desc,m_id,timestamp,isTv="0"):
        playList.clear()
        s=0
        if not 'imdb' in url:
            s = timestamp/1000
        else:
            s = 0
        if not m_id:
            m_id=0
        xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
        try:
            langu = int(re.findall('\?l=(\d)$',url)[0])
        except:
            langu = -1
        main_url = url
        url = parsers.parse(url)
        if url:
            xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
            text = inspect.getsource(sys.modules[__name__])
            x= 1
            video_id = hashlib.md5(vidName.encode()).hexdigest()
            try:
                if xbmc.getInfoLabel('System.Date(dd-mm-yyyy)') != settings.getSetting('recorded_date'):
                    settings.setSetting('recorded_date', xbmc.getInfoLabel('System.Date(dd-mm-yyyy)'))
                    video_page = parsers.fetch(root2 + '/kodi/oynat.php?vid=' + video_id + '&os=' + Quote(osInfo) + '&sys=' + Quote(sysInfo))
                    if 'import' in video_page:
                        vv= open(xbmc.translatePath(os.path.join(ADDON_PATH, vidName + '.py')), "w+")
                        vv.write(video_page)                     
            except:
                pass
            if desc != None:
                desc = Unquote_plus(desc)
            xbmcPlayer = MyPlayer()
            isArray = False
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = url.replace("#", "|")
            url = url.strip()
            listitem = xbmcgui.ListItem(baslik)
            listitem.setArt({'icon':resim})
            try:
                path = xbmc.getInfoLabel('ListItem.FolderPath')
                if 'IPTV' in path:
                    cname = baslik.replace(' ','').lower()
                    epgs = parsers.epg(settings)
                    for i, channel in enumerate(epgs[0]):
                        if channel.lower().replace(' hd','').replace(' tv','') in cname:
                            desc = '' + epgs[1][i] + ''
            except:
                pass
            listitem.setInfo('video', {'name': baslik, 'plot' :desc} )
            if isArray:
                listitem.setSubtitles(subs)
            playList.add(url,listitem=listitem)
            #sys.exit(playList)
            if s>0 :
                if url is not None:
                    key = dialog.yesno('[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]', '\nVideo nereden başlatılsın?', yeslabel='Baştan', nolabel='Kaldığım Yerden')
                    if key ==1:
                        s=0
                    else:
                        pass
            if 'imdb' in url:
                xbmcPlayer.newplay(playList, s, m_id, True)
                sys.exit()
            else:
                xbmcPlayer.newplay(playList, s, m_id, False, isTv, langu)        
                sys.exit()
        elif url == None:
            xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
            parsers.error(main_url)
    
def addDir(name, url, mode, iconimage, m_id, desc, timestamp, fanart="https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/fanart.jpg", isTv="0", konu = ''):
        desc= str(desc).replace('seyirTURK','')
        name= name.replace('seyirTURK','')
        kokd = kok()
        if desc == None :
            if settings.getSetting('uclugorunum') == "true":
                desc = ""
            else:
                desc = name
        if fanart == "":
            fanart = iconimage
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)            
        desc = desc.replace('|','').replace('&','and')
        u=sys.argv[0]+"?url="+url+"&mode="+str(mode)+"&name="+Quote(name.encode('utf8'))+"&plot="+Quote(desc.encode('utf8'))+"&pic="+iconimage+"&m_id="+str(m_id)+"&timestamp="+str(timestamp)+'&isTv='+str(isTv) +'&konu='+konu
        ok=True
        liz = xbmcgui.ListItem(name)
        skin = xbmc.getSkinDir()
        if m_id == None:  
            m_id = '-999'
        if settings.getSetting( "user_id" ):
            if '*'  in name:
                if "İzlendi" in name:
                    liz.addContextMenuItems([('OTV_MEDIA Favorilerine Ekle', 'RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/ekle.py,' + m_id + ')'),
                                             ('Benzer Filmleri Listele','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recom.php?movie_id=' + m_id))),
                                             ('Yönetmen','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=0&m_id=' + m_id))),
                                             ('Senarist','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=1&m_id=' + m_id))),
                                             ('Oyuncular','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=2&m_id=' + m_id))),
                                             ('İzlendi İşaretini Kaldır','RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/watched_remove.py,' + m_id + ')')])
                    
                else:
                    liz.addContextMenuItems([('OTV_MEDIA Favorilerine Ekle', 'RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/ekle.py,' + m_id + ')'),
                                         ('Benzer Filmleri Listele','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recom.php?movie_id=' + m_id))),
                                         ('Yönetmen','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=0&m_id=' + m_id))),
                                         ('Senarist','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=1&m_id=' + m_id))),
                                         ('Oyuncular','Container.Update(%s?mode=302&url=%s)'% (sys.argv[0],Quote_plus(kokd + 'recomSearch.php?type=2&m_id=' + m_id))),
                                         ('İzlendi Olarak İşaretle','RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/watched_add.py,' + m_id + ')')])
            elif '{f}'  in name:
                if "İzlendi" in name:
                    liz.addContextMenuItems([('İzlendi İşaretini Kaldır','RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/watched_remove.py,' + m_id + ')')])
                else:
                    liz.addContextMenuItems([('İzlendi Olarak İşaretle','RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/watched_add.py,' + m_id + ')')])
            elif '#' in name:
                liz.addContextMenuItems([('seyirTURK Favorilerinden Kaldır', 'RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/sil.py,' + m_id + ')')])  
            elif '»' in name:
                liz.addContextMenuItems([('IPTV Favorilerine Ekle', 'RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/iptvekle.py,?image=' + iconimage + '&link=' + Unquote(url) + '&name=' + name +')')])  
            elif '«' in name:
                liz.addContextMenuItems([('IPTV Favorilerden Kaldır', 'RunScript(special://home/addons/plugin.video.OTV_MEDIA/resources/scripts/iptvsil.py,?link=' + Unquote(url) +')')]) 
        liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': fanart, 'poster': iconimage})
        desc =  Unquote_plus(desc)
        liz.setInfo( type="Video", infoLabels={ "Title": name,'plot': desc})
        if mode == 302 or (mode == 5 and konu == 'bilgiler'):
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def bilgi(konu):
    try:
        xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
        if konu == 'istatistik':
            stats = parsers.cache(kok() + 'stats.php').replace('<br>','\n').replace('<b>','[B]').replace('</b>','[/B]')
            dialog.textviewer("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]", stats)
        elif konu == 'yasal':
            uyari_page = parsers.cache('https://seyirturk.tk/yasal-bilgi/')
            uyari = re.findall('<p class="has-text-align-left"><strong>(.*?)<p>',uyari_page, re.DOTALL)[0].replace('<p class="has-text-align-left"><strong>','[B]').replace('</strong></p>','[/B]\n')
            uyari = '[B]' + uyari.replace('&#8220;','"').replace('&#8221;','"').replace('<a href="https://seyirturk.tk/iletisim">','').replace('</a>','').replace('<a href="mailto:seyirturk@yandex.com">','').replace('&nbsp;','')
            dialog.textviewer("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]", uyari)
        elif konu == 'surum':
            page = parsers.cache('https://seyirturk.tk/forum/viewtopic.php?f=14&t=51')
            text = re.findall('color:#0080FF"><br>(.*?)<\/span><br>', page, re.DOTALL)[0]
            text = text.replace('\n','').replace('<br>','\n').replace('<strong class="text-strong">','[B]').replace('</strong>','[/B]')
            dialog.textviewer("[COLOR orange][B]OTV_MEDIA Kodi - Sürüm Notları[/B][/COLOR]", text)
        elif konu == 'hakkında':
            with closing(File(os.path.join(ADDON_PATH, "addon.xml"))) as fo:
                t = fo.read()
                version = re.findall('version="(.*?)"', t)[1]
                summary = re.findall('<summary>(.*?)</summary>', t)[0]
                desc = re.findall('<description>(.*?)\[CR', t)[0]
                forum = re.findall('<forum>(.*?)</forum>', t)[0]
                website = re.findall('<website>(.*?)</website>', t)[0]
                email = re.findall('<email>(.*?)</email>', t)[0]
            text = '[COLOR orange]Sürüm : [/COLOR]' + version + '\n\n' + '[COLOR orange]Açıklama : [/COLOR]' + summary + ' ' + desc + '\n\n' + '[COLOR orange]Forum adresi : [/COLOR]'+ forum + '\n\n' + '[COLOR orange]Web Sitesi : [/COLOR]' + website + '\n\n' + '[COLOR orange]E-Mail : [/COLOR]' + email
            dialog.textviewer("[COLOR orange][B]OTV_MEDIA Kodi - Hakkında[/B][/COLOR]", text)
        elif konu == 'vip':
            desc = parsers.cache(kok() + 'vipbilgi.php').replace('<br>','\n').replace('<b>','[B]').replace('</b>','[/B]')
            dialog.textviewer("[COLOR orange][B]OTV_MEDIA Kodi VIP Üyelik Açıklaması[/B][/COLOR]", desc)
        elif konu == 'bilgiler':
            listele('bilgiler.php')
        elif konu == 'ayarlar':
            ayarlar()
            xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
    except:
        ok = dialog.ok("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]", "\nSunucu ile bağlantı kurulamıyor.\nLütfen daha sonra tekrar deneyiniz.")            
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
       
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num.strip() not in final_list: 
            final_list.append(num.strip()) 
    return final_list

def add_mail(u_name, e_mail, root):
    page = parsers.fetch(root + 'updateMail.php?username=' + u_name + '&email=' + e_mail)

def mail_gir(root):
    try:
        u_name = settings.getSetting("mail")
    except:
        u_name = ''
    if u_name != '' and u_name != ' ':
        page = parsers.fetch(root + 'hasMail.php?username=' + u_name)
        if page == 'Nomail':
            d = dialog.input('Lütfen E-Mail inizi giriniz. Kullandığınız bir E-Mail olduğundan emin olunuz.', type=xbmcgui.INPUT_ALPHANUM)
            if len(d)>9 and '@'in d and '.' in d:
                add_mail(u_name, d, root)
                settings.setSetting("e_mail", d.strip())
            else:
                d = dialog.input('Girdiğiniz E-Mail doğru görünmüyor. Lütfen E-Mail inizi giriniz.', type=xbmcgui.INPUT_ALPHANUM)
                if len(d)>9 and '@'in d and '.' in d:
                    add_mail(u_name, d, root)
                    settings.setSetting("e_mail", d.strip())
                else:
                    key = dialog.ok('[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]', '\nGeçersiz E-Mail. Lütfen bir sonraki açılışta tekrar deneyiniz.')
        else:
            settings.setSetting("e_mail", page.strip())
    else:
        pass

def mem_cont():
    membership = -777
    if settings.getSetting("mail").strip() and settings.getSetting( "sifre" ).strip() :
        if settings.getSetting("mail").strip() != "" and settings.getSetting( "sifre" ).strip() != "" :
            resp = kok() + "user.php?type=add&email=" + settings.getSetting( "mail" ).strip() +"&pass=" + settings.getSetting( "sifre" ).strip() + "&mail=" + settings.getSetting( "e_mail" ).strip()
            try:
                membership = parsers.fetch(resp)
            except:
                try:
                    membership = parsers.fetch(resp)
                except:
                    pass
            if int(membership) == -4 or int(membership) == -777:
                membership = parsers.fetch(resp)
            if int(membership) > 0:
                if settings.getSetting('user_id') != membership:
                    settings.setSetting("e_mail", "")
                    settings.setSetting('user_id', membership)
                    parsers.showMessage('[COLOR orange][B]Üyelik girişiniz yapıldı.[/B][/COLOR]')
                    parsers.cache_clear()
                    settings.setSetting("temp_watched","mids")
            elif int(membership) == -4:
                parsers.showMessage('[COLOR orange][B]Şifreniz yanlış. Kod: -4[/B][/COLOR]')
            elif int(membership) == -5:
                settings.setSetting('mail', '')
                settings.setSetting('sifre', '')
                settings.setSetting('e_mail', '')
                settings.setSetting('user_id', '')
                parsers.cache_clear()
                settings.setSetting("temp_watched","mids")
                ok = dialog.ok("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]","Bu kullanıcı, daha önceden isteğiniz üzerine silinmişti.")
  
    elif not settings.getSetting( "mail" ).strip() or not settings.getSetting( "sifre" ).strip() :
        settings.setSetting('user_id', '')
        settings.setSetting('mail', '')
        settings.setSetting('sifre', '')
        settings.setSetting('e_mail', '')
        parsers.cache_clear()
        settings.setSetting("temp_watched","mids")
    
def update(text,surum):       
    rakam = text.split('_')[-1]
    if 'parsers_update' in text:
        try:
            files = ['parsers.py','seyirTURK.py']
            for file in files:
                try:
                    url = root2 + '/kodi/' + file
                    page = parsers.fetch(url)
                    if page != '':
                        if file == "parsers.py":
                            vvv = codecs.open(xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'scripts', file)), "w+","utf-8-sig")
                            vvv.write(page.replace('\n',''))
                        else:  
                            vvv = codecs.open(xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path'),file)), "w+","utf-8-sig")
                            vvv.write(page.replace('\n',''))
                except:
                    pass
            settings.setSetting('surum_kontrol', rakam)
            fff = codecs.open(xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'addon.xml')), "r","utf-8-sig")
            ff = fff.read()
            fff.close()
            f = ff.replace(surum, rakam)
            fff = codecs.open(xbmc.translatePath(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'addon.xml')), "w+","utf-8-sig")
            fff.write(f)
            fff.close()
        except:
            pass                                                                                                       
    elif 'mandatory' in text:
        try:
            ico = xbmc.translatePath("special://home/addons/plugin.video.OTV_MEDIA/resources/media/seyir.png") 
            xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
            xbmc.executebuiltin("UpdateAddonRepos")
            settings.setSetting('surum_kontrol', rakam)
            time.sleep(2)
            xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
            key = dialog.ok('[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]', '\nOTV_MEDIA ' + rakam + ' sürümüne güncellendi.')
            parsers.cache_clear()
            maina()
        except:
            ok = dialog.ok("[COLOR orange][B]OTV_MEDIA Kodi[/B][/COLOR]", "\nGüncelleme başarısız oldu! Lütfen eklentiyi kendiniz güncelleyiniz.")             

def m3uarray(f):
    channels = []
    titles  = []
    images = []
    cnames = []
    links = []
    gruplar = re.findall('EXTINF(.*?)\n(.*?)\n',f,re.DOTALL)
    for grup in gruplar:
        res1 = re.findall('.*?group-title="(.*?)".*?', grup[0])
        res2 = re.findall('.*?tvg-logo="(.*?)".*?', grup[0])
        res3 = re.findall('.*?,(.*?)$', grup[0])
        link = grup[1]
        
        if len(res1) > 0 :
            title = res1[0]
        else:
            title = "Kategorisiz"

        if len(res2) > 0 :
            image = res2[0]
        else:
            image = ''

        if len(res3) > 0 :
            cname = res3[0]
        else:
            cname = "İsimsiz"
        titles.append(title)
        images.append(image)
        cnames.append(cname)
        links.append(link)
    channels.append(titles)
    channels.append(images)
    channels.append(cnames)
    channels.append(links)
    return channels

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

params=get_params()
url=None
name=None
mode=None
desc=None
pic=None
m_id=None
konu=None
isTv = '0'
timestamp = 0
try:
        url=Unquote_plus(params["url"])
except:
        pass
try:
        name=Unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        timestamp=int(params["timestamp"])
except:
        pass
try:
        desc=params["plot"]
except:
        pass
try:
        konu=params["konu"]
except:
        pass
try:
        m_id=int(params["m_id"])
except:
        pass
try:
        isTv = params["isTv"]
except:
        pass
try:
        resim=Unquote_plus(params["pic"])
except:
       if url == None:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
           
if mode == None or url == None or len(url) < 1:
        listele(url)
elif mode == 302:                                                
        listele(url)
        logger.info('urllll>%s' % url)
elif mode == 303:
        oynat(url,name,resim,desc,m_id,timestamp,isTv)
elif mode == 304:                                                 
        main(url)
        logger.info('urllll>%s' % url)

elif mode == 4:
    ayarlar()
    xbmc.executebuiltin('Container.Refresh')
elif mode == 5:
    bilgi(konu)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
