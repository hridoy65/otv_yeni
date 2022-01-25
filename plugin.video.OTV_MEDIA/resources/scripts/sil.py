# -*- coding: utf-8 -*-
import sys,xbmcaddon,parsers,xbmc

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
userdata = xbmc.translatePath('special://userdata')
user_id = settings.getSetting('user_id')
root = settings.getSetting('root')
if user_id != "":
    m_id = sys.argv[1]
    delete = parsers.fetch(root + 'user.php?type=fav&do=44' + '&f_id=' + m_id)
    if int(delete) == 0:
        parsers.showMessage('seyirTURK','[COLOR orange][B]Film çıkarıldı.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/minus.png'))
    else:
        parsers.showMessage('seyirTURK','[COLOR orange][B]İşlem başarısız oldu.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
else:
    parsers.showMessage('seyirTURK','[COLOR orange][B]Giriş yapmamışsınız.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
xbmc.executebuiltin("Container.Refresh")
