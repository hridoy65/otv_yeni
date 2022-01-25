#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
import re
from resources.lib.gui.guiElement import cGuiElement 
SITE_IDENTIFIER = 'hdfilmcehennemi_com'
SITE_NAME = 'HDfilmcehennemi'

 
URL_MAIN = 'https://www.hdfilmcehennemi1.com/'
from resources.lib.comaddon import dialog, VSlog, xbmc					

TURK_SINEMA = (True, 'showGenre')
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
 
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.hdfilmcehennemi1.com/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    dialog = cConfig().createDialog(SITE_NAME)
    
    for i in range(0,27) :
        cConfig().updateDialog(dialog, 36)
        
        if (i > 0):
            sTitle = chr(64+i)
        else:
            sTitle = '09'
            
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl + sTitle.upper() )
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal] Lettre [COLOR red]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
def sEcho(s):
    if not 'page/' in s:
        s = s +'page/1'
    if 'page/1' in s:
        s = s.replace('page/1', 'page/2')
        return s
    if 'page/2' in s:
        s = s.replace('page/2', 'page/3')
        return s
    if 'page/3' in s:
        s = s.replace('page/3', 'page/4')
        return s
    if 'page/4' in s:
        s = s.replace('page/4', 'page/5')
        return s
    if 'page/5' in s:
        s = s.replace('page/5', 'page/6')
        return s
    if 'page/6' in s:
        s = s.replace('page/6', 'page/7')
        return s
    if 'page/7' in s:
        s = s.replace('page/7', 'page/8')
        return s
    if 'page/8' in s:
        s = s.replace('page/8', 'page/9')
        return s
    if 'page/9' in s:
        s = s.replace('page/9', 'page/10')
        return s
    if 'page/10' in s:
        s = s.replace('page/10', 'page/11')
        return s
    if 'page/11' in s:
        s = s.replace('page/11', 'page/12')
        return s
    if 'page/12' in s:
        s = s.replace('page/12', 'page/13')
        return s
    if 'page/13' in s:
        s = s.replace('page/13', 'page/14')
        return s
    if 'page/14' in s:
        s = s.replace('page/14', 'page/15')
        return s
    if 'page/15' in s:
        s = s.replace('page/15', 'page/16')
        return s
    if 'page/16' in s:
        s = s.replace('page/16', 'page/17')
        return s
    if 'page/17' in s:
        s = s.replace('page/17', 'page/18')
        return s
    if 'page/18' in s:
        s = s.replace('page/18', 'page/19')
        return s
    if 'page/19' in s:
        s = s.replace('page/19', 'page/20')
        return s
    if 'page/20' in s:
        s = s.replace('page/20', 'page/21')
        return s
    if 'page/21' in s:
        s = s.replace('page/21', 'page/22')
        return s
    if 'page/22' in s:
        s = s.replace('page/22', 'page/23')
        return s
    if 'page/23' in s:
        s = s.replace('page/23', 'page/24')
        return s
    if 'page/24' in s:
        s = s.replace('page/24', 'page/25')
        return s
    if 'page/25' in s:
        s = s.replace('page/25', 'page/26')
        return s
    if 'page/26' in s:
        s = s.replace('page/26', 'page/27')
        return s
    if 'page/27' in s:
        s = s.replace('page/27', 'page/28')
        return s
    if 'page/28' in s:
        s = s.replace('page/28', 'page/29')
        return s
    if 'page/29' in s:
        s = s.replace('page/29', 'page/30')
        return s
    if 'page/30' in s:
        s = s.replace('page/30', 'page/31')
        return s
    if 'page/31' in s:
        s = s.replace('page/31', 'page/32')
        return s
    if 'page/32' in s:
        s = s.replace('page/32', 'page/33')
        return s
    if 'page/33' in s:
        s = s.replace('page/33', 'page/34')
        return s
    if 'page/34' in s:
        s = s.replace('page/34', 'page/35')
        return s
    if 'page/35' in s:
        s = s.replace('page/35', 'page/36')
        return s
    if 'page/36' in s:
        s = s.replace('page/36', 'page/37')
        return s
    if 'page/37' in s:
        s = s.replace('page/37', 'page/38')
        return s
    if 'page/38' in s:
        s = s.replace('page/38', 'page/39')
        return s
    if 'page/39' in s:
        s = s.replace('page/39', 'page/40')
        return s
    if 'page/40' in s:
        s = s.replace('page/40', 'page/41')
        return s
    if 'page/41' in s:
        s = s.replace('page/41', 'page/42')
        return s
    if 'page/42' in s:
        s = s.replace('page/42', 'page/43')
        return s
    if 'page/43' in s:
        s = s.replace('page/43', 'page/44')
        return s
    if 'page/44' in s:
        s = s.replace('page/44', 'page/45')
        return s
    if 'page/45' in s:
        s = s.replace('page/45', 'page/46')
        return s
    if 'page/46' in s:
        s = s.replace('page/46', 'page/47')
        return s
    if 'page/47' in s:
        s = s.replace('page/47', 'page/48')
        return s
    if 'page/48' in s:
        s = s.replace('page/48', 'page/49')
        return s
    if 'page/49' in s:
        s = s.replace('page/49', 'page/50')
        return s 
    return False   
def hdfilmcehennemi(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi1.com/category/diziler/page/1/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Diziler', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi1.com/')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)

    sUrl = 'https://www.hdfilmcehennemi1.com'

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
                
    sPattern = '<li id="menu-item-.*?" class="menu-item menu-item-type-.*? menu-item-object-.*? menu-item-.*?"><a href="(.*?)">([^<]+)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sGenre = alfabekodla(aEntry[1])
            ssUrl = aEntry[0]+ 'page/1/'
            if not 'http' in ssUrl:
                ssUrl = sUrl + ssUrl
            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  ssUrl)
                        
            if '/fragmanlar/' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'fragmanlar', sGenre, '', '', '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showMovies', sGenre, '', '', '', oOutputParameterHandler)

        
        
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
def fragmanlar(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.voirfilms.org/rechercher'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()

        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<a href="(.*?)">(.*?)</a>'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.decode('utf-8',"replace")
        sHtmlContent = unicodedata.normalize('NFD', sHtmlContent).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
        sHtmlContent = sHtmlContent.encode('utf-8')#On remet en utf-8
                                                                                  
                                                                 
        sPattern = '</div><div class="col-xs-.*? col-sm-.*? poster-container">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
    
    sHtmlContent = sHtmlContent.replace('.html','.html/6')
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
           
            sPicture = str(aEntry[1])
            
                
            sUrl = str(aEntry[0])
            
           
            
            sTitle =alfabekodla(aEntry[2])           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'fragmanHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
 
def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    data = resp.content                   
                                
    sHtmlContent = re.findall('<div class="col-xs-6 col-sm-4 poster-container">.*?<a href="(.*?)">.*?<img class="lazy-wide" src="data:.*?" data-flickity-lazyload=".*?" data-src="(.*?)" alt="(.*?)"', data, re.S)
         
    for sUrl,sPicture,sTitle in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
def sshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.voirfilms.org/rechercher'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()

        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<a href="(.*?)">(.*?)</a>'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.decode('utf-8',"replace")
        sHtmlContent = unicodedata.normalize('NFD', sHtmlContent).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
        sHtmlContent = sHtmlContent.encode('utf-8')#On remet en utf-8
                                                                                  

                                                                     
        sPattern = 'data-content="<p>(.*?)</p>.*?<a href="(.*?)">.*?data-src="(.*?)" alt="(.*?)".*?</i>(.*?)</span>'
    
    sHtmlContent = sHtmlContent.replace('-izle/','-izle/6').replace('</i><i','')
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)                                                            	
    #fh.close()                                                                                              
                                 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
           
            sPicture = str(aEntry[2])
            
                
            sUrl = str(aEntry[1])
            
            desc = str(aEntry[0])
            
            sTitle =aEntry[3] + ' [COLOR limegreen]' + aEntry[4] +'[/COLOR]'
          
            sTitle = alfabekodla(sTitle)          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)

 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory() 
def showMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.voirfilms.org/rechercher'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()

        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<a href="(.*?)">(.*?)</a>'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(ssUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.decode('utf-8',"replace")
        sHtmlContent = unicodedata.normalize('NFD', sHtmlContent).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
        sHtmlContent = sHtmlContent.encode('utf-8')#On remet en utf-8
                                                                                  

                                                                     
        sPattern = '<div class="col-xs-6 col-sm-4 poster-container">.*?data-content="<p>(.*?)</p>.*?<a href="(.*?)">.*?data-src="(.*?)" alt="(.*?)".*?<span class="poster-lang">(.*?)</span>'
    
    sHtmlContent = sHtmlContent.replace('-izle/','-izle/6').replace('<i class="tr-flag"></i>','').replace('<i class="fa fa-cc" style="color:#ffbe71;"></i>','')
                                                                                        
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)                                                            	
    #fh.close()                                                                                              
                                
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
           
            sPicture = str(aEntry[2])
            
                
            sUrl = aEntry[1]
            
            desc = str(aEntry[0])
            
            sTitle =aEntry[3] + ' [COLOR limegreen]' + aEntry[4]+ '[/COLOR]'
          
         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            if 'sezon' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'diziHosters', sTitle, '', '', '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)

            
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = sEcho(str(ssUrl))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
           
def __checkForNextPage(sHtmlContent):
    sPattern = '</span><a class="nextpostslink" rel="next" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False
def diziHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl = alfabekodla(sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sPattern = '<ul class="episode-list">(.+?)</ul>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)"><span class="text">(.*?)</span>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[1]
            
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            if 'Fragman' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', '', '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'DiziHosters', sTitle, '', '', '', oOutputParameterHandler)

            
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
         
def DiziHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace("'",'"')
    sPattern = '<font color=".*?">(.*?)</font>.*?<iframe src="(.*?)"'
    oParser = cParser()                    
    aResult = oParser.parse(sHtmlContent, sPattern)


    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[0]
            ssUrl = str(aEntry[1])
            if not 'http' in ssUrl:
                ssUrl = 'https:' + ssUrl

            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(ssUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showDIZIHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
UA = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    link =  cRequestHandler(sUrl).request()         
    reti =re.findall('<ul class="hdc-parts" style="padding-right:130px">.*?<li class="selected"><a href="(.*?)"><span class="text">(.*?)</span>',link,re.DOTALL)
    (url,ret)=reti[0]
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', url)
    oOutputParameterHandler.addParameter('sMovieTitle', str(ret) )
    oGui.addDir(SITE_IDENTIFIER, 'showHosters', ret, 'genres.png', oOutputParameterHandler)
           
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('User-Agent', UA)
    
    sHtmlContent = oRequest.request()
    sHtmlContent = sHtmlContent.replace("\n", "")
    sHtmlContent = sHtmlContent.replace('<span class="fa fa-check check-mark">', "")
#    sPattern = '<ul class="hdc-parts" style="padding-right:130px">(.*?)</ul>'
#    oParser = cParser()
#    aResult = oParser.parse(sHtmlContent, sPattern)
#    sHtmlContent = aResult
    ilk_pattern = '<li class="selected"><a href="[^"]+"><span class="text">([^<]+)</span>'
    parts_pattern = '<li><a href="([^"]+)"><span class="text">([^<]+)</span></a></li>'
 
    sPattern = '><a href="(.*?)"><span class="text">(.*?)</span>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent,parts_pattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[1] 
            
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    data = cRequestHandler(sUrl).request()
   
     
#    urll= re.findall('<div id="player" class="(.*?)">', data)[0]            
                             
    Url = re.findall("<div id=\"player\"[\s\S]*?<script>[\s\S]*?'([^']+)'", data)
    sHoster = base64.b64decode(Url[0])                       
    sHosterUrl = re.findall('src="(.*?)"', sHoster)[0]   
    if sHosterUrl:
       sHosterUrl =sHosterUrl
    else:
                 
       sHosterUrl= re.findall('<div id="player">.*?<iframe width=".*?" height=".*?" src="(.*?)"',data, re.S)[0]                         
   
           
    if not 'http' in sHosterUrl:
        sHosterUrl = 'http:' + sHosterUrl
    
    if "rapidrame.com" in sHosterUrl:
                 
                
                 oOutputParameterHandler = cOutputParameterHandler()
                 oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
                 oGui.addTV(SITE_IDENTIFIER, 'raptu', sMovieTitle, '', '', '', oOutputParameterHandler)   

    if "vanlongstream" in sHosterUrl:
                 
                 oOutputParameterHandler = cOutputParameterHandler()
                 oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
                 oGui.addTV(SITE_IDENTIFIER, 'yplayer', sMovieTitle, '', '', '', oOutputParameterHandler)   


    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if (oHoster != False):
                
                
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
#
        

    oGui.setEndOfDirectory()
def raptu():                    
    oGui = cGui()	
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    data = cRequestHandler(sUrl).request()
#    data=data.replace('\/',"/").replace('"file":"https://www.raptu.com',"")
      
    stream_url = re.findall('"file":"(.*?)","label":"(.*?)"',data, re.S)
    for sUrl,sTitle in stream_url:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
   

       


def yplayer():
#    oGui = cGui()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent=requests.get(sUrl,headers={'Referer':sUrl}).text
               
         


    sPattern = '<li class="(.*?)">(.*?)</li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[1]
            
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sitUrl', sUrl)
	    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
	    oGui.addDir(SITE_IDENTIFIER, 'tplayervideo', sTitle, 'genres.png', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
   

def  tplayervideo():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        p = oInputParameterHandler.getValue('siteUrl')
        Url = oInputParameterHandler.getValue('sitUrl')
	sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        sThumbnail = oInputParameterHandler.getValue('sThumbnail')
        key = re.findall('key=(.*?)$', Url, re.IGNORECASE)[0]
        

	url = 'https://tplayer.vanlongstream.com/getDataPlayer/' + p + '/' + key	
	req = urllib2.Request(url)
       
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        req.add_header('Referer',Url)
        req.add_header('X-Requested-With',' XMLHttpRequest')
        post={url: p}

        post = urllib.urlencode(post)
        sJson=_get(req,post)
             
        
	if not 'http' in sJson:
	           dialog().VSinfo('Stream Yok', p, 5)
		   return 
	rUrl =re.findall('"data":"(.*?)"', sJson)[0]
	if  'film.hdfilmcehennemi1.com/embedplay/' in  rUrl:
	       playgoogl(rUrl)
	if  'tmaster.vanlongstream' in  rUrl:
            sUrl ='https://tslave1.vanlongstream.com/hls/%s/%s.playlist.m3u8'%(key,key)
            p2pdrive(sUrl,rUrl)
	else:   
	    fragmanHosters(rUrl)
#	name = 'sMovieTitle'
#	addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name,rUrl, '')


def playgoogl(sUrl):                    
    oGui = cGui()	
    
    data = cRequestHandler(sUrl).request()
#    data=data.replace('\/',"/").replace('"file":"https://www.raptu.com',"")
      
    stream_url = re.findall('"file":"(.*?)","label":"(.*?)"',data, re.S)
    for sUrl,sTitle in stream_url:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'PLAYPLAY', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
 
def p2pdrive(sUrl,rUrl):                    
    oGui = cGui()	
    key=rUrl.replace('https://tmaster.vanlongstream.com/play/',"")  
    vUrl ='https://tslave1.vanlongstream.com/hls/%s/%s.playlist.m3u8'%(key,key)
#    https://tplayer.vanlongstream.com/initPlayer/be1d0eccb1646deaa85b96dd4b920a0e be1d0eccb1646deaa85b96dd4b920a0e
#    hUrl ='https://tslave1.vanlongstream.com/hls/be1d0eccb1646deaa85b96dd4b920a0e/be1d0eccb1646deaa85b96dd4b920a0e.playlist.m3u8'
   
    page =  getUrl(vUrl, output='cookie').result 
    req = urllib2.Request(vUrl)
       
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    req.add_header('Referer',rUrl)
    req.add_header('Cookie', page)
        

  
    data=_get(req)  


    stream_url = re.findall('RESOLUTION=.*?x(.*?)\n(.*?)\n',data, re.S)
    for sTitle,rrUrl in stream_url:
                                              
         
        Url ='https://tslave1.vanlongstream.com'+rrUrl 
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(Url))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'PLAYPLAY', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  


def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok


def fragmanHosters(sUrl):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
#    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
   


    sPattern = '<ifram.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def PLAYPLAY():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = sUrl+"|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  


def showDIZIHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
  

    sMovieTitle = alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        
        
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()