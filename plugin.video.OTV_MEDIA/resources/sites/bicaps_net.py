#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
SITE_IDENTIFIER = 'bicaps_net'
SITE_NAME = 'Bicaps.net'
SITE_DESC = 'Films  streaming'

URL_MAIN = 'https://www.fullhdfilmizlesene.net/'






def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    if PY3:    
        data = base64.b64decode(data)
        data = to_utf8(data)
        return data
    else:    
        return base64.decodestring(data)
        
def base64fix(c):
    if c.isalpha():
        x = c.lower()
        if x < 'n':
            x = 13
        else:
            x = -13
        return chr(ord(c) + x)
    else:
        return c
#[(1, 'ATOM', None, None, 'fullhdfilmizlesene_parse:https://rapidvid.net/vod/v1x44cfeac6', None, None, None, None, None, None)]        


def fullhdfilmizlesene_parse( url):
                son_url = ''
                film_quality = []
                video_tulpe = []
                error = None
               # url = re.findall("'fullhdfilmizlesene_parse:(.*?)'", url)[0]
                page = getHtml(url) 
                page =page.replace('\\x','').replace('\/','/')
                
                logger.info('page >%s' % page) 
                if '"file": "' in page :
                                link3 = re.findall('"file": "(.*?)"', page)[0]
                                
                                if PY3:
                                    import codecs
                                    son_url = codecs.decode(link3, 'hex').decode('ascii')
                                    return son_url
                                else:    
                                    son_url = link3.decode('hex')
                                    return son_url                        
                if 'eval(function(p,' in page :

                            link2 = re.findall('(eval\(function\(p,a,c,k,e,d.*?\}\)\);)', page)[0]
                            gg =  cPacker().unpack(link2)
                            gg = gg.replace("\\'","'").replace('\\\\\\\\','\\\\\\')
                            ff =  cPacker().unpack(gg)
                            cc = ff.replace("\\","").replace("x","")
                            if PY3:
                                cc = to_utf8(cc)
                            if re.search('"file":".*?","label":.*?"file":".*?","label"', cc):
                                for match in re.finditer('"file":"(.*?)","label":"(.*?)"', cc):
                                    film_quality.append(match.group(2))
                                    link = match.group(1)
                                    if PY3:
                                        import codecs
                                        link = str(codecs.decode(link, 'hex'))[2:-1]
                                    else:
                                        link = link.decode('hex')
                                    if link.startswith("//"):
                                        link = "https:" + link
                                    video_tulpe.append(link)
                            else:
                                link3 = re.findall('"file":"(.*?)"', cc)[0]
                                if PY3:
                                    import codecs
                                    son_url = str(codecs.decode(link3, 'hex'))[2:-1]
                                    return son_url
                                else:    
                                    son_url = link3.decode('hex')
                                    return son_url                        


                else:

                                son_url = 'http:'+re.findall('"hls":"(.*?)"', page)[0]
                                return son_url



def fullhdfilmizlesene( url):
        try:
            page = getHtml(url)          
            video_list_temp = []
            chan_counter = 0
            if '"tr":"' in page:
                vid_link = re.findall('"tt":"([^"]+)".*?"t":\{"tr":"([^"]+)"', page)
                for text in vid_link:
                    vidid = text[1]
                    name = text[0]
                    lnk = ""
                    for v in vidid:
                        lnk = lnk + base64fix(v)
                    vidlink = decode_base64(lnk)
                    nametxt = decode_base64(name)
                    nametxt = nametxt.upper()
                    if "youtube" not in vidlink:
                        vidlink = vidlink
                    chan_counter += 1			
                    chan_tulpe =  vidlink
                    video_list_temp.append(chan_tulpe)
            else:
                vid_link = re.findall('"tt":"([^"]+)".*?"t":\["([^"]+)"', page)
                for text in vid_link:
                    vidid = text[1]
                    name = text[0]
                    lnk = ""
                    for v in vidid:
                        lnk = lnk + base64fix(v)
                    vidlink = decode_base64(lnk)
                    nametxt = decode_base64(name)
                    nametxt = nametxt.upper()
                    if "youtube" not in vidlink:
                        vidlink = vidlink
                    chan_counter += 1			
                    chan_tulpe =  vidlink
                    video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print ('ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp))
            return video_list_temp
        except:
            print ('ERROR get_videos')

 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.fullhdfilmizlesene.net/arama?ara=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
   
    
    for i in range(0,27) :
        
        
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
   
def bicaps(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/yeni-filmler')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'YENI FILMLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/en-cok-begenilen')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK BEGENILENLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/en-cok-izlenen')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'EN COK IZLENENLER', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.com/filmler')
    oGui.addDir(SITE_IDENTIFIER, 'FilmT', 'Film Türleri-Genre', 'genres.png', oOutputParameterHandler)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.fullhdfilmizlesene.net/filmizle/turkce-dublaj-film-izle')
    oGui.addDir(SITE_IDENTIFIER, 'Yillar', 'Yillar', 'genres.png', oOutputParameterHandler)

    sUrl = 'https://www.fullhdfilmizlesene.net/filmizle/turkce-dublaj-film-izle'

    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<h2>Filtreler</h2></div>(.+?)<div class="clear">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">.+?</a></li>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
           
            Link = aEntry[0]
           
            sTitle  = sTitle  + ' [COLOR skyblue]' + sTitle +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sTitle, '', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    

def FilmT():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl)  
    oParser = cParser()               
    sPattern = '<div class="sidebar-icerik">(.+?)<div class="temizle">'
 
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">'
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
    sPattern = '<ul class="yil">(.+?)<div class="clear">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="(.+?)" title="(.+?)">.+?</a></li>'
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
   
    data = cRequestHandler(sUrl).request() 
                          
    sHtmlContent = re.findall('<img src="(.*?)" alt="(.*?)" width=".*?" height=".*?" class="afis">.*?<div class="dty">.*?<a href="(.*?)"', data, re.S)
         
    for sPicture,sTitle,sUrl in sHtmlContent:
             
                       
            sTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()   
def showMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sHtmlContent=getHtml(sUrl) 
    sPattern = '<img src=".*?" data-src="(.*?)" alt="(.*?)".*?<h2><a href="(.*?)".*?<span class="trz-tda">(.*?)</span>'
    oParser = cParser()                  
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):                              
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
            sTitle = aEntry[1]+'-'+ aEntry[3]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[2])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            #not found better way
            sTitle = malfabekodla(sTitle)
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
           

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next_Page >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
 
def __checkForNextPage(sHtmlContent):
    sPattern = "<li class='secili'><a href='javascript:void.+?'>+?<a href='(.+?)'"
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
def dHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sHtmlContent=getHtml(sUrl) 
    oParser = cParser()
    sPattern = '<script>(.+?)<noscript><link'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            
            Title = malfabekodla(aEntry[1])
            sTitle = malfabekodla(aEntry[2])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'ddstreams',  sTitle, '', sThumbnail, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()
def ddstreams():
    oGui = cGui()                           
    oInputParameterHandler = cInputParameterHandler()
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('siteUrl')
    liste = []
    liste.append( ['TR Dublaj','tr'] ) 
    liste.append( ['Altyazi','en'] ) 

    for Title,sUrl2 in liste:
        
         urlm= 'https://www.fullhdfilmizlesene.net/player/api.php?id=%s&type=t&name=%s&get=video&pno=%s&format=json&ssl=true'%(url,name,sUrl2)
         sTitle=name+'-'+ Title
         oOutputParameterHandler = cOutputParameterHandler()
         oOutputParameterHandler.addParameter('siteUrl', urlm)
         oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
         oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
         oGui.addDir(SITE_IDENTIFIER, 'lmstreams',  sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()  
def mfullhdfilmizlesene(url):
    url1 = url.split('?')[0]
    url_onek = '/'.join(url1.split('/')[:-3])
#    sec = re.findall('\?l=(\d)',url)[0]
    try:
        page = getHtml(url)
    except:
        pass
    flag = False
    try:
        code = re.findall('"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)".*?"types":"(.*?)"',page)
        if 'tr,en' in code[0][3]:
            flag = True
    except:
        code = re.findall('"vidid":"(.*?)","name":"(.*?)","nameTxt":"(.*?)"',page)
    sources = []
    for cod in code:
        if 'atom' in cod[2].lower() or 'turbo' in cod[2].lower() or 'vmol' in cod[2].lower() or 'voltran' in cod[2].lower():
            sources.append(cod)
    if len(sources) > 1:
        for source in sources:
            kaynaklar.append(source[1])
        code = select(kaynaklar,sources,1)
        if code is None:
            return None
        elif code ==  'selection cancelled':
            return code
    elif len(sources) == 1:
        code = sources[0]
    elif len(sources) < 1:
        return None
    if not flag:
        url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0]
    else:
        if sec == "0":
            url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0] + '&pno=tr' 
        if sec == "1":
            url2 = url_onek + '/player/api.php?type=t&get=video&name='+ code[1] + '&id=' + code[0] + '&pno=en'
    page = getHtml(url2)
    try:
        url3 = re.findall('src="(.*?)"', page)[0]
    except:
        url3 = re.findall('src=\"(.*?)\""', page)[0]
    if 'vidmoly' in url3:
        return url3.replace('\/','/')
    else:                  
        page = getHtml(url3)
        try:
            m3u8_raw = re.findall('"file"\s*:\s*"(.*?)"',page)[0].replace("\\x", "")
            if isPy3 == False:
                m3u8 = m3u8_raw.decode('hex')
            else:
                m3u8 = bytes.fromhex(m3u8_raw).decode('utf-8')
            cc_json = re.findall('jwSetup\.tracks\s*=\s*(\[.*?\])',page)[0]
            json_data = json.loads(cc_json)
            subtitles = []
            try:
                ccs = json_data[0]["file"]
                if 'http' in ccs:
                    subtitles.append(ccs)
            except:
                ccs = json_data[1]["file"]
                if 'http' in ccs:
                    subtitles.append(ccs)
            if sec == '1':
                return [m3u8,subtitles]
            elif sec == '0':
                return m3u8
        except:
            me =re.findall('"file": "(.*?)"',page)[0]#.replace("\\/", "/")
            mem = malfabekodla(me)
            logger.info('Url >%s' % mem )
            return mem

def Hosters():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        name = oInputParameterHandler.getValue('sMovieTitle')
        
        url =fullhdfilmizlesene(Url)
        logger.info('Urlll >%s' % url[0] )
        url =fullhdfilmizlesene_parse( url[0])
        url =url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        logger.info('Url >%s' % url )
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')                                          
def partstreams():
    oGui = cGui()                           
    oInputParameterHandler = cInputParameterHandler()
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('sitUrl')
    eTitle = oInputParameterHandler.getValue('MovieTitle')
    liste = []
    liste.append( ['part 1','1'] ) 
    liste.append( ['part 2','2'] ) 
    liste.append( ['part 3','3'] ) 
    for Title,sUrl2 in liste:
        
         urlm= 'https://www.fullhdfilmizlesene.net/player/api.php?id=%s&type=p&name=%s&get=video&pno=%s&format=json&ssl=true'%(url,name,sUrl2)
#        link =  cRequestHandler(urlm).request() 
#        link= link.replace('\\','')
#        urlll =re.findall('<ifram.+?[SRC|src]=["|\'](.*?)["|\']',link,re.DOTALL)[0]
         sTitle=eTitle+'-'+ Title
         oOutputParameterHandler = cOutputParameterHandler()
         oOutputParameterHandler.addParameter('siteUrl', urlm)
         oOutputParameterHandler.addParameter('MovieTitle', str(sTitle))
         oGui.addDir(SITE_IDENTIFIER, 'lmstreams',  sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def mmlmstreams():         
        oGui = cGui()
        
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
#    Title = oInputParameterHandler.getValue('sMovieTitle')
        sThumb = oInputParameterHandler.getValue('sThumbnail')
        name = oInputParameterHandler.getValue('MovieTitle')
#        data = cRequestHandler(url).request()  
        data=requests.session().get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36","cookie": "pl=1; list_type=normal; _ga=GA1.2.716840295.1568547510; _gid=GA1.2.469201334.1568547510; __cfduid=dd457b4ae0b423872250a867deacb90401568547501; fullhd_source=fast; fullhd_sourceType=t; plok=1; plokk=1; plox=1; __ga_rc=18","Connection": "Keep-Alive","Accept-Encoding": "gzip"}).text
        data=str(data)
        aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,data,'')
def lmstreams():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        Title= oInputParameterHandler.getValue('sMovieTitle')
        sUrl = oInputParameterHandler.getValue('siteUrl')
        data = getHtml(sUrl) 
   
        data= data.replace('\\','')
        link = re.findall('src=\"(.*?)"', data)[0]
        if  '/player/okru/' in link:
            link= link.replace('https://www.fullhdfilmizlesene.net/player/okru/plysv2.php?id=','').replace('&','?')
            link ='https://ok.ru/videoembed/'+ link
        if  'turkakisi.com/movie' in link:
            line =  cRequestHandler(link).request() 
            line= line.replace('\/\/cdn0','https://cdn0').replace('\/','/')
            urll =re.findall('"hls":"(.*?)"',line,re.DOTALL)[0]
            playOTV2(urll,Title)
        if  'cdn.dochub' in link:
            line =  cRequestHandler(link).request()                         
	   
            urll =re.findall('"file":"(.*?)"',line,re.DOTALL)[0]+'|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            playOTV2(urll,Title)
            return
        if  'gov2a.php' in link:
	    #from adult_eu import *    
            urla= "https://www.fullhdfilmizlesene.net/"
            referer=[('Referer',urla)]                                      
            lin=gegetUrl(link,headers=referer)       
	    
            link2 = re.findall('skin:[\s\S]*?(eval[\s\S]*?}\)\));', lin)[0]
            lin1 =  cPacker().unpack(link2)
            lin1 = lin1.replace("\\'","'")
            lin2 =  cPacker().unpack(lin1)
            lin2 = lin2.replace("\\","").replace("x","")
            urll = re.findall('"file":"(.*?)"', lin2)[0].decode('hex')
            playOTV2(urll,Title)
            return
        if  'awsbeta17.php' in link:
	    #from adult_eu import *    
            lin2= link
            urll =re.findall('https://.*?&f=(.*?)&ip=.*?', lin2)[0]
            if 'BluRay' in urll:
                urll = 'http://secourgeon.cf'+ urll
            else:
                urll = 'http://fillingham.ga'+ urll
            playOTV2(urll,Title)
            return
        sstreams(link)


def playOTV2(Url,name):         
        
      
      aaddLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,Url,'')
	
def aaddLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")                                                                  	

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok  
def sstreams(urlll):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sHosterUrl= urlll
            
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
          sMovieTitle = cUtil().DecoTitle(sMovieTitle)
          cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()

def streams():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
    urlm= 'https://www.fullhdfilmizlesene.net/player/api.php?id=%s&type=t&name=%s&get=video&format=json&callback=jQuery111203512659266764322_1561399057691&_=1561399057695'%(url,sMovieTitle)
    
    link =  getHtml(url)
    link= link.replace('\\','')
    sHosterUrl =re.findall('<ifram.+?[SRC|src]=["|\'](.*?)["|\']',link,re.DOTALL)[0]
            
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()