# -*- coding: utf-8 -*-
import sys,xbmcaddon,re,parsers,xbmc

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
userdata = xbmc.translatePath('special://userdata')
user_id = settings.getSetting('user_id')
root = settings.getSetting('root')
if user_id != "":
    try:
        link = re.findall('link=(.*?)$',sys.argv[1])[0]
    except:
        link = ""
    delete = parsers.fetch(root + 'user.php?type=faviptv' + '&do=1&link=' + link)
    if int(delete) == 0:
        parsers.showMessage('seyirTURK','[COLOR orange][B]IPTV çıkarıldı.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/minus.png'))
    else:
        parsers.showMessage('seyirTURK','[COLOR orange][B]İşlem başarısız oldu.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
else:
    parsers.showMessage('seyirTURK','[COLOR orange][B]Giriş yapmamışsınız.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
xbmc.executebuiltin("Container.Refresh")
