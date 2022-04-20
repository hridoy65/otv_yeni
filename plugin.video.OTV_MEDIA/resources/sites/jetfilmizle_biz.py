#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import * 
SITE_IDENTIFIER = 'jetfilmizle_biz'


 
URL_MAIN = 'https://jetfilmizle.xyz/'


TURK_SINEMA = (True, 'showGenre')
 
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read() 

def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://jetfilmizle.xyz/filmara.php'
        post_data = {"s": sSearchText}
        r = s.post(sUrl , headers={"Cookie": "_ga=GA1.2.1944649352.1646917866; _gid=GA1.2.1884536816.1646917866; __asc=b1c795fd17f73f450d7c671f845; __auc=b1c795fd17f73f450d7c671f845; __cf_bm=N_LY9G4vENQZh8Xf3YZPtEW5SkTa6W9Yl5Swx9dmuD4-1646917866-0-AQMg1NzU2E5AkJzDTliIzR4l8YeMwHiSdUvPPAad8K8RXQWD9VAQxGiC+wdtOlW1PHQZDpkPNstmcdBEfepyW57h/4JaeDWCLr7AUS2GCqR7tr3bVKqvTbTaB5kU+flASw==; __atuvc=2%7C10; __atuvs=6229f8e971ca3466001; _gat=1","Origin": "https://jetfilmizle.xyz","Referer": "https://jetfilmizle.xyz/","Content-Type": "application/x-www-form-urlencoded","User-Agent": UA,}, data=post_data, timeout=10)
        data = r.text                                                                                                   
        data=to_utf8(data )
        logger.info("data: %s" % data )                 
        sHtmlContent = re.findall('<div class="col-md-4 col-xs-12 col-sm-24">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"', data, re.S)
         
        for sUrl,sPicture,sTitle in sHtmlContent:
            if not 'http' in sUrl: 
                sUrl = 'https://jetfilmizle.xyz'+ sUrl      
           # sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()           
   
def jetfilmizle(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhan/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)

	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://jetfilmizle.xyz/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)


    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://jetfilmizle.xyz/'
    sHtmlContent =getHtml(sUrl)     
   
    sPattern = '<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><a title="(.*?)" href="(.*?)">'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            
            Link = aEntry[1]
           
            sTitle = malfabekodla(aEntry[0])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  Link)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies',sTitle, '', '', '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()    

 
def showMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:


        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<article class="movie .*?">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        sHtmlContent =getHtml(sUrl)         
        sPattern = '<article class="movie .*?">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
     
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = malfabekodla(aEntry[2])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
   
def __checkForNextPage(sHtmlContent):
    sPattern = '<span class=\'current\'>.+?</span><a class="page larger" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False
 
    
def Hosters():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            sUrl = oInputParameterHandler.getValue('siteUrl')
            name = oInputParameterHandler.getValue('sMovieTitle')
            from resources.scripts import parsers
            url = parsers.parse(sUrl)
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = url.replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    




def mshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','')


    sPattern = '<div id="movie" style="z-index: auto;"><p><iframe.+?src=[\'|"](.+?)[\'|"]'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:

            sHosterUrl = str(aEntry)
            if 'mail.ru' in sHosterUrl:
                       id_raw = re.findall('mail.ru/.*?mail/(.*?)/.*?/(\d*)\.html',  sHosterUrl)
                       if id_raw:
                           (m_user, m_id) = id_raw[0]
                       Url = "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (m_user, m_id)
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'mailru', sMovieTitle, '', '', '', oOutputParameterHandler)	     

            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
              
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

       

    oGui.setEndOfDirectory()
