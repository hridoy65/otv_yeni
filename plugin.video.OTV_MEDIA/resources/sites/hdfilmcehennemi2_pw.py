#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'hdfilmcehennemi2_pw'
SITE_NAME = 'HDfilmcehennemi2'

 
URL_MAIN = 'https://www.hdfilmcehennemi2.pw/'
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
				

TURK_SINEMA = (True, 'showGenre')

HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
 
 
def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.hdfilmcehennemi2.co/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
       
         
def mshowMovies(sSearch=''):
    oGui = cGui()
  #  grab = cTMDb()
    addons = addon()

    oInputParameterHandler = cInputParameterHandler()

    iPage = 1
    term = ''
    if (oInputParameterHandler.exist('page')):
        iPage = oInputParameterHandler.getValue('page')

    if (oInputParameterHandler.exist('sSearch')):
        sSearch = oInputParameterHandler.getValue('sSearch')

    if sSearch:
        result = grab.getUrl('search/movie', iPage, 'query=' + sSearch)
        sUrl = ''

    else:
        if (oInputParameterHandler.exist('session_id')):
            term += 'session_id=' + oInputParameterHandler.getValue('session_id')

        sUrl = oInputParameterHandler.getValue('siteUrl')
        result = grab.getUrl(sUrl, iPage, term)

    try:
        total = len(result)
        if (total > 0):
            total = len(result['results'])
            progress_ = progress().VScreate(SITE_NAME)

            for i in result['results']:
                progress_.VSupdate(progress_, total)
                if progress_.iscanceled():
                    break

                # Mise en forme des infos (au format meta imdb)
                i = grab._format(i, '',"movie")

                sId, sTitle, sGenre, sThumb, sFanart, sDesc, sYear = i['imageUrl'], i['movieName'], i['genre'], i['imageUrl'], i['backdrop_path'], i['description'], i['year']

                if not isMatrix():
                    sTitle = sTitle.encode("utf-8")

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl',  sId)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('sTmdbId', sId)
                oOutputParameterHandler.addParameter('type', 'film')

                if isMatrix():
                    oOutputParameterHandler.addParameter('searchtext', sTitle)
                else:
                    oOutputParameterHandler.addParameter('searchtext', cUtil().CleanName(sTitle))

                cGui.CONTENT = "movies"
                oGuiElement = cGuiElement()
                oGuiElement.setTmdbId(sId)
                oGuiElement.setSiteName('globalSearch')
                oGuiElement.setFunction('showSearch')
                oGuiElement.setTitle(sTitle)
                oGuiElement.setFileName(sTitle)
                oGuiElement.setIcon('films.png')
                oGuiElement.setMeta(1)
                oGuiElement.setThumbnail(sThumb)
                oGuiElement.setPoster(sThumb)
                oGuiElement.setFanart(sFanart)
                oGuiElement.setCat(1)
                oGuiElement.setDescription(sDesc)
                oGuiElement.setYear(sYear)
                oGuiElement.setGenre(sGenre)

                oGui.addFolder(oGuiElement, oOutputParameterHandler)

            progress_.VSclose(progress_)

            if (int(iPage) > 0):
                iNextPage = int(iPage) + 1
                oOutputParameterHandler = cOutputParameterHandler()
                if sSearch:
                    oOutputParameterHandler.addParameter('sSearch', sSearch)

                oOutputParameterHandler.addParameter('siteUrl', sUrl)
                oOutputParameterHandler.addParameter('page', iNextPage)
                oGui.addNext(SITE_IDENTIFIER, 'showMovies', 'Page ' + str(iNextPage), oOutputParameterHandler)

    except TypeError as e:
        oGui.addText(SITE_IDENTIFIER, '[COLOR red]Aucun résultat n\'a été trouvé.[/COLOR]')

    # changement mode
    view = addons.getSetting('visuel-view')

    oGui.setEndOfDirectory(view)   
def sEcho(s):
    if not '/page/' in s:
        s = s +'/page/1'
    if '/page/1' in s:
        s = s.replace('/page/1', '/page/2')
        return s
    if '/page/2' in s:
        s = s.replace('/page/2', '/page/3')
        return s
    if '/page/3' in s:
        s = s.replace('/page/3', '/page/4')
        return s
    if '/page/4' in s:
        s = s.replace('/page/4', '/page/5')
        return s
    if '/page/5' in s:
        s = s.replace('/page/5', '/page/6')
        return s
    if '/page/6' in s:
        s = s.replace('/page/6', '/page/7')
        return s
    if '/page/7' in s:
        s = s.replace('/page/7', '/page/8')
        return s
    if '/page/8' in s:
        s = s.replace('/page/8', '/page/9')
        return s
    if '/page/9' in s:
        s = s.replace('/page/9', '/page/10')
        return s
    if '/page/10' in s:
        s = s.replace('/page/10', '/page/11')
        return s
    if '/page/11' in s:
        s = s.replace('/page/11', '/page/12')
        return s
    if '/page/12' in s:
        s = s.replace('/page/12', '/page/13')
        return s
    if '/page/13' in s:
        s = s.replace('/page/13', '/page/14')
        return s
    if '/page/14' in s:
        s = s.replace('/page/14', '/page/15')
        return s
    if '/page/15' in s:
        s = s.replace('/page/15', '/page/16')
        return s
    if '/page/16' in s:
        s = s.replace('/page/16', '/page/17')
        return s
    if '/page/17' in s:
        s = s.replace('/page/17', '/page/18')
        return s
    if '/page/18' in s:
        s = s.replace('/page/18', '/page/19')
        return s
    if '/page/19' in s:
        s = s.replace('/page/19', '/page/20')
        return s
    if '/page/20' in s:
        s = s.replace('/page/20', '/page/21')
        return s
    if '/page/21' in s:
        s = s.replace('/page/21', '/page/22')
        return s
    if '/page/22' in s:
        s = s.replace('/page/22', '/page/23')
        return s
    if '/page/23' in s:
        s = s.replace('/page/23', '/page/24')
        return s
    if '/page/24' in s:
        s = s.replace('/page/24', '/page/25')
        return s
    if '/page/25' in s:
        s = s.replace('/page/25', '/page/26')
        return s
    if '/page/26' in s:
        s = s.replace('/page/26', '/page/27')
        return s
    if '/page/27' in s:
        s = s.replace('/page/27', '/page/28')
        return s
    if '/page/28' in s:
        s = s.replace('/page/28', '/page/29')
        return s
    if '/page/29' in s:
        s = s.replace('/page/29', '/page/30')
        return s
    if '/page/30' in s:
        s = s.replace('/page/30', '/page/31')
        return s
    if '/page/31' in s:
        s = s.replace('/page/31', '/page/32')
        return s
    if '/page/32' in s:
        s = s.replace('/page/32', '/page/33')
        return s
    if '/page/33' in s:
        s = s.replace('/page/33', '/page/34')
        return s
    if '/page/34' in s:
        s = s.replace('/page/34', '/page/35')
        return s
    if '/page/35' in s:
        s = s.replace('/page/35', '/page/36')
        return s
    if '/page/36' in s:
        s = s.replace('/page/36', '/page/37')
        return s
    if '/page/37' in s:
        s = s.replace('/page/37', '/page/38')
        return s
    if '/page/38' in s:
        s = s.replace('/page/38', '/page/39')
        return s
    if '/page/39' in s:
        s = s.replace('/page/39', '/page/40')
        return s
    if '/page/40' in s:
        s = s.replace('/page/40', '/page/41')
        return s
    if '/page/41' in s:
        s = s.replace('/page/41', '/page/42')
        return s
    if '/page/42' in s:
        s = s.replace('/page/42', '/page/43')
        return s
    if '/page/43' in s:
        s = s.replace('/page/43', '/page/44')
        return s
    if '/page/44' in s:
        s = s.replace('/page/44', '/page/45')
        return s
    if '/page/45' in s:
        s = s.replace('/page/45', '/page/46')
        return s
    if '/page/46' in s:
        s = s.replace('/page/46', '/page/47')
        return s
    if '/page/47' in s:
        s = s.replace('/page/47', '/page/48')
        return s
    if '/page/48' in s:
        s = s.replace('/page/48', '/page/49')
        return s
    if '/page/49' in s:
        s = s.replace('/page/49', '/page/50')
        return s 
       

def hdfilmcehennemi2(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi2.co/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Yeni Eklenenler', 'search.png', oOutputParameterHandler)
    

    sUrl = 'https://www.hdfilmcehennemi2.co/'

    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<a href="(https://www.hdfilmcehennemi2.*?/kategori/.*?)">(.*?)</a>'
                                     
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
           
            Link = aEntry[0]
           
            sTitle  = sTitle  + ' [COLOR skyblue]' + sTitle +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Link))
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sTitle, '', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
def showDIZI(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="col-6 col-sm-3 poster-container px-2 px-sm-1 mb-3 mb-sm-2">.*?<a href="(.*?)".*?<img.*?data-src="(.*?)" alt="(.*?)".*?<h2 class="title px-3">(.*?)</h2>'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]                                                                                             
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            dec = aEntry[3]
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'showDIZI2', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
 
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
def showDIZI2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) #               
                
    sPattern = '<div class="card-list-item no-image col-12 col-sm-3">.*?<a href="(.*?)" title="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            sTitle = aEntry[1]
            sUrl = (aEntry[0])
            
            sDisplayTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def FilmT():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl)  
    oParser = cParser()               
    sPattern = '<span>Özel Kategoriler</span>(.+?)</nav>'

    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                              
                
    sPattern = '<a class="nav-link text-truncate" href="(https://www.hdfilmcehennemi2.co/.+?)" title=".+?">(.+?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showMovies',  sTitle, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def Yillar():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<li class="nav-item dropdown">(.+?)<li class="nav-item ">'
                 
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" class="dropdown-item">(.+?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showMovies',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

 
    oGui.setEndOfDirectory()

def searchowMovies(sUrl):
    oGui = cGui()
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<div class="moviefilm">.*?<a href="(.*?)".*?<i class=".*?sub"></i>(.*?)</span><img src="(.*?)" alt="(.*?)"'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            
            sTitle = aEntry[3]+'-'+ aEntry[1]                                                                                          
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            dec = aEntry[2]
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
                         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

            if 'www.hdfilmcehennemi2.*?/dizi/' in sUrl:
                oGui.addMovie(SITE_IDENTIFIER, 'showDIZI2', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
 
           

        oGui.setEndOfDirectory()
def showMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl = oInputParameterHandler.getValue('siteUrl')
    logger.info("ssUrl2 : %s" % ssUrl) 
    sHtmlContent=getHtml(ssUrl) 
#<span class="poster-lang"><i class="tr-sub"></i>(.*?)</span><img src="https://www.hdfilmcehennemi2.co/wp-content/uploads/2022/03/Lucy-and-Desi-izle-170x240.jpg" alt="Lucy and Desi izle" height="170px"
    sPattern = '<div class="moviefilm">.*?<a href="(.*?)".*?<i class=".*?sub"></i>(.*?)</span><img src="(.*?)" alt="(.*?)"'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            
            sTitle = aEntry[3]+'-'+ aEntry[1]                                                                                          
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            dec = aEntry[2]
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
                         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

            if 'www.hdfilmcehennemi2.*?/dizi/' in sUrl:
                oGui.addMovie(SITE_IDENTIFIER, 'showDIZI2', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, dec, oOutputParameterHandler)
 
           
        logger.info("ssUrl : %s" % ssUrl)                
        sNextPage = sEcho(str(ssUrl))#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
 
         

def __checkForNextPage(sHtmlContent):
    sPattern = '<a class="nextpostslink" rel="next" href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl
    return False
def blmstreams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    name= oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    data = cRequestHandler(sUrl).request() 
    aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')          
def aaddLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  
   
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
     
    link =  getHtml(sUrl)        
    ret =re.findall('<link rel="alternate" type="application/json" href="(.+?)"',link,re.DOTALL)[0]
    

    sHtmlContent=getHtml(ret) 
    sHtmlContent= sHtmlContent.replace('\\','')
    oParser = cParser()
                
    sPattern = '<p><!--nextpage--><!--baslik:(.*?)--><iframe loading="lazy" src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    for urlm in aResult[1]:
        sUrl2 = urlm[1]                         
        if not 'http' in sUrl2:       
           sUrl2='https:'+ sUrl2
        
        sTitle = urlm[0]
        sTitle= sTitle.replace('Bu00f6lu00fcm','Bölüm')
                           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle) )
        oGui.addDir(SITE_IDENTIFIER, 'streamer',  sTitle, 'genres.png', oOutputParameterHandler)
           

    oGui.setEndOfDirectory()
def streamer():
            oGui = cGui()     
            oInputParameterHandler = cInputParameterHandler()
            Url = oInputParameterHandler.getValue('siteUrl')
            name = oInputParameterHandler.getValue('sMovieTitle')
            from resources.scripts import parsers
            url = parsers.parse(Url)
            subs = []
            is_array = lambda var: isinstance(var, (list))
            if is_array(url):
                subs =url[1]
                url = url[0]
                isArray = True
            url = url.replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    
def mHosters():
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

def mmHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) 
    sHtmlContent= sHtmlContent.replace('<i class="tr-flag"></i>','<svg xmlns="tr-flag"/></svg>').replace('href="#" data-bs-toggle="modal" data-bs-target="#videoModal" data-trailer="','href="')
    
    oParser = cParser()                  
    sPattern = '<a class="nav-link.*?href="(.*?)".*?<svg xmlns=".*?"/></svg>(.*?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
                                    
                
            Title = malfabekodla(aEntry[1]).replace('Sinema Modu','')
            logger.info("body : %s" % Title)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]).replace('#',''))
            oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            if not 'http' in str(aEntry[0]):
                oGui.addTV('youtubecom_tr', 'YouTubeplay',  Title, '', sThumbnail, '', oOutputParameterHandler)
            else:
            
                oGui.addTV(SITE_IDENTIFIER, 'streams',  Title, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
     
    link =  getHtml(url)
    link= link.replace('\\','')
    Url =re.findall('<iframe class=".*?" data-src="(.*?)"',link,re.DOTALL)[0]
    data =GetvideoUrl(Url)
    if  'https://hdfilmcehennemi.download' in data:
        data =Getvideo(data)
        data =data+ '|Referer=&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' 
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')   

       
def Getvideo(url):
    page = getHtml(url)
    page= page.replace('\n','').replace('\t','')
    links_labels = re.findall('<a class="btn btn-primary ms-2 me-2" href="(.*?)">(.*?)</a>', page)
    for link in links_labels:
        qualitylist.append(link[1])
        videolist.append('https://hdfilmcehennemi.download'+ link[0])
    return select(qualitylist,videolist)
   
                          
def GetvideoUrl(sUrl):  # Recupere les liens des regex
    chain  =getHtml(sUrl)
    if  'initPlayer("https://hdfilmcehennemi.fun' in chain:
        r = re.search('<a href="(https://hdfilmcehennemi.download/download.+?)"', chain)
        if (r):
            url = r.group(1)
       # url = url + '|Referer=' + sUrl + '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' 
            return url
    else:
        r = re.search('sources:.+?file:"(https://.+?)"', chain)
        if (r):
            url = r.group(1)
            url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' 
            return url
