# -*- coding: utf-8 -*-
import sys,xbmcaddon,re,parsers,xbmc

settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
userdata = xbmc.translatePath('special://userdata')
user_id = settings.getSetting('user_id')
root = settings.getSetting('root')

if user_id != "":
    try:
        image = re.findall('image=(.*?)&',sys.argv[1])[0]
    except:
        image = ""
    try:
        link = re.findall('link=(.*?)&',sys.argv[1])[0]
    except:
        link = ""
    try:
        name = re.findall('name=(.*?)$',sys.argv[1])[0]
        name = name.replace('[COLOR blue][B][COLOR red]» [/COLOR]','').replace('[/B][/COLOR]','').replace(' ','%20')
    except:
        name ='noname'
    add = parsers.fetch(root + 'user.php?type=faviptv&u_id=' + user_id + '&do=0&link=' + link + '&name=' + name + '&image=' + image )
    if int(add) == 0:
        parsers.showMessage('seyirTURK','[COLOR orange][B]IPTV eklendi.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/plus.png'))
    else :
        parsers.showMessage('seyirTURK','[COLOR orange][B]IPTV zaten var.[/B][/COLOR]', 3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/unlem.png'))    
else:
    parsers.showMessage('seyirTURK','[COLOR orange][B]Giriş yapmamışsınız.[/B][/COLOR]',3000, xbmc.translatePath('special://home/addons/plugin.video.OTV_MEDIA/resources/media/x.png'))

