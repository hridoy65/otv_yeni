# -*- coding: utf-8 -*-
import sys,xbmcaddon,parsers,xbmc

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
userdata = xbmc.translatePath('special://userdata')
user_id = settings.getSetting('user_id')
root = settings.getSetting('root')
temp_watched = settings.getSetting('temp_watched')
if user_id != "":
    m_id = sys.argv[1]
    delete = parsers.fetch(root + 'markWatched.php?u_id=' + settings.getSetting( "user_id" ) + '&m_id=' + m_id)
    if str(m_id) not in temp_watched:
        temp_watched += "," + str(m_id)
    settings.setSetting("temp_watched",temp_watched)
    if int(delete) == 1 or int(delete) == 2:
        parsers.showMessage('seyirTURK','[COLOR orange][B]İzlendi olarak işaretlendi.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/plus.png'))
    else:
        parsers.showMessage('seyirTURK','[COLOR orange][B]İşlem başarısız oldu.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
else:
    parsers.showMessage('seyirTURK','[COLOR orange][B]Giriş yapmamışsınız.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))
xbmc.executebuiltin("Container.Refresh")
