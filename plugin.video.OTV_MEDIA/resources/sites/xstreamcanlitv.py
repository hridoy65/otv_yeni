#-*- coding: utf-8 -*-
from  LIVETV2 import * 
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
from resources.lib.player import cPlayer

SITE_NAME = 'streamcanlitv' 
SITE_IDENTIFIER = 'xstreamcanlitv'

MOVIE_VIEWS = (True, 'streamcanlitv')


def iostreamcanlitv():
    oGui = cGui()
    urlkk= "http://www.canlitv.stream/" 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://www.canlitv.today/kategoriler'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if re.match('.*?<a href="tum-kanallar">',sHtmlContent, re.S):
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
      sPattern = '<a href="(kategori/.*?)">(.*?)</a>'
                                                                 
      sHtmlContent = sHtmlContent
   
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
           
            sTitle = aEntry[1]
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(urlkk) + sUrl
           
            #sTitle = alfabekodla(sTitle)
            sPicture = "http://www.canlitv.stream/static/images/logo.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'streamcanlitv2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
    oGui.setEndOfDirectory()
def iostreamcanlitv2():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://mobile.canlitvlive.io/')
    oGui.addDir(SITE_IDENTIFIER, 'iostream', 'Yeni TV Kanallari', 'genres.png', oOutputParameterHandler)

           
    sUrl = 'http://mobile.canlitvlive.io/?s=Yerel'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<li><a class="subheader">Kategoriler</a></li>(.+?)<div class="nav-wrapper navbar searcharea">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<li><a href="(.*?)"><i class="material-icons">.*?</i>(.*?)</a></li>'
                                                             
    sHtmlContent = sHtmlContent        
   
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
           
            sTitle = aEntry[1]
            sPicture = "http://mobile.canlitvlive.io/images/mobil-footer.png"  
            sUrl = str(aEntry[0])
                       
            #sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'iostream', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
       
    oGui.setEndOfDirectory()
def iostream(sSearch = ''):
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '</center>(.+?)<div class="mobireklam">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult    
    sPattern = '<a href="(.*?)" title=".*?"><center><h2 class="lsttop">(.*?)</h2></center><img class="logo lozad" data-src="(.*?)"'
                 
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()                                                               

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = alfabekodla(aEntry[1])
           
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
                
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'iossshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
    oGui.setEndOfDirectory()            








def iossshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = cRequestHandler(Url).request()  

                     

    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    playlist= re.findall('file:.*?"(.*?)"', dat, re.S)[0] 
    url= playlist + '|' + Header

    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'') 


def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
      