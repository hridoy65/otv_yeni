# -*- coding: cp1254 -*-
import parsers,xbmcgui,xbmcvfs,os,xbmc
dialog = xbmcgui.Dialog()
key = dialog.yesno('[COLOR orange][B]seyirTURK Kodi[/B][/COLOR]', '\nseyirTURK �nbelle�i temizlenecek!', yeslabel='Temizle', nolabel='Temizleme')
temp = xbmc.translatePath("special://temp")
if key ==1:
    path = xbmc.translatePath(os.path.join(temp,'86519'))
    paths, files = xbmcvfs.listdir(path)
    print(files)
    for file in files:
        xbmcvfs.delete(os.path.join(path, file))
    parsers.showMessage('[COLOR orange][B]seyirTURK Kodi[/B][/COLOR]', "[COLOR blue][B]�nbellek temizlendi.[/B][/COLOR]")
else:
    parsers.showMessage('[COLOR orange][B]seyirTURK Kodi[/B][/COLOR]', "[COLOR yellow][B]Vazge�ildi.[/B][/COLOR]")
