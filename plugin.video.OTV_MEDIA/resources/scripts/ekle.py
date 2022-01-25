# -*- coding: utf-8 -*-
import sys,xbmcaddon,parsers,xbmc

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
userdata = xbmc.translatePath('special://userdata')
root = settings.getSetting('root')
user_id = settings.getSetting('user_id')
if user_id != "":
    m_id = sys.argv[1]
    check =  parsers.fetch(root + 'user.php?type=check' + '&f_id=' + m_id)
    if int(check) == 0:
        add = parsers.fetch(root + 'user.php?type=fav&do=0' + '&f_id=' + m_id)
        if int(add) == 0:
            parsers.showMessage('seyirTURK','[COLOR orange][B]Film eklendi.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/plus.png'))
        else :
            parsers.showMessage('seyirTURK','[COLOR orange][B]İşlem başarısız oldu.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
    else :
        parsers.showMessage('seyirTURK','[COLOR orange][B]Film zaten var.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/unlem.png'))
else:
    parsers.showMessage('seyirTURK','[COLOR orange][B]Giriş yapmamışsınız.[/B][/COLOR]',3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))

