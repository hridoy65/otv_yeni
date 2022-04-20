#-*- coding: utf-8 -*-

from resources.sites.LIVETV2 import *  

HOST = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)


TIK='|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

def showMessage(heading='OTV_MEDIA', message = '', times = 2000, pics = ''):
                try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
                except Exception as e:
                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
SITE_IDENTIFIER = 'diziizlehdfull_net'
SITE_NAME = 'diziizlehdfull.org'
MOVIE_HD = (True, 'showGenre')
def diziizlehdfulltr():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.tv/tum-bolumler/')
    oOutputParameterHandler.addParameter('sMovieTitle', 'BolumD dizi izle')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'DIZI-ARA', 'search.png', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.tv/tum-bolumler/')
    oOutputParameterHandler.addParameter('sMovieTitle', 'BolumD dizi izle')
    oGui.addDir(SITE_IDENTIFIER, 'diziabc', 'DIZILER-ABC', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.tv/tum-bolumler/')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Tüm Bölümler', 'search.png', oOutputParameterHandler)
                                              
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.tv/tum-bolumler/?tip=populer')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Popüler Bölümler', 'search.png', oOutputParameterHandler)
                                               
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.dizibox.tv/efsane-diziler/')
    oGui.addDir(SITE_IDENTIFIER, 'ssshowMovies', 'Efsane Diziler', 'search.png', oOutputParameterHandler)
    
        
    oInputParameterHandler = cInputParameterHandler()
                 
    oGui.setEndOfDirectory()
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

def showSearch(): #affiche les genres
 oGui = cGui()
 sSearchText = oGui.showKeyBoard()
 if (sSearchText != False):
    sUrl = 'https://www.dizibox.tv/'  
 
    post_data = {"s": sSearchText}
    r = s.post(sUrl , headers={"Referer": "https://www.dizibox.tv/","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": UA,"Connection": "Keep-Alive","x-requested-with": "XMLHttpRequest"}, data=post_data, timeout=10)
    data = r.text                                                                                                   
        
    sJson=to_utf8(data )
    

                                  
    logger.info("data : %s" % data)
    playlist = re.findall('<figure class="figure big-cover pull-left m-r-1">.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"', data, re.S)
    for sUrl,sPicture,sTitle in playlist:
            
           
            sTitle = malfabekodla(sTitle)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addMovie(SITE_IDENTIFIER, 'FilmABCde', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

 oGui.setEndOfDirectory()  



def ssshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
     
        sHtmlContent = reponse.read()
        sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl = oInputParameterHandler.getValue('siteUrl')
   
        sHtmlContent =getHtml(ssUrl)                                                                                                                             
                          
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<a class="thumbnail-gradien.*?" href="(.*?)".*?<img src=\'(.*?)\' alt=\'(.*?)\''

                                                                  
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
        
               
            sThumbnail = str(aEntry[1])
          
              
                
            
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'mHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

           
        if not sSearch:
            sNextPage = sEcho(ssUrl)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def sshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
       sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        ssUrl = oInputParameterHandler.getValue('siteUrl')
   
        sHtmlContent =getHtml(ssUrl)                                                                                                                              
       
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<a class="thumbnail-gradien.*?" href="(.*?)".*?<img src=\'(.*?)\' alt=\'(.*?)\''
                  
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #
   
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sUrl = str(aEntry[0])
        
               
            sThumbnail = str(aEntry[1])
          
              
                
            
            sTitle =aEntry[2] 
          
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'mHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        if not sSearch:
            sNextPage =  sEcho(ssUrl)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def diziabc():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    sHtmlContent = getHtml(Url) 
               
    sPattern = ' <div id="alphabetical-category" class="p-x-2">(.*?)<div id="sub-menu" class="ff-2">'
    oParser = cParser()
    #sHtmlContent = oParser.parse(sHtmlContent, sPattern)
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult      
    Pattern = '<a href="#(.*?)" class="alphabetical-category-link" title="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
           
          
                            
            sUrl = str(aEntry[1])
            sTitle = aEntry[0]
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'FilmABC', sTitle, '', '', '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()


   



def FilmABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    le = oInputParameterHandler.getValue('sMovieTitle')
    abc = 'https://www.dizibox.tv/tum-bolumler/'
    
    sHtmlContent=getHtml(abc) 
               
    sPattern = "<ul class='alphabetical-category-list list-unstyled' data-index='#"+le+"'><li>(.*?)</ul>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult      
    Pattern = '<a title="(.+?)" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[0])
                            
            sUrl = str(aEntry[1])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'FilmABCde', sTitle, '', '', '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()


def FilmABCde():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    le = oInputParameterHandler.getValue('sMovieTitle')
    #abc = 'https://www.dizibox.tv/tum-bolumler/'
    
    sHtmlContent=getHtml(Url) 
               
    sPattern = '<div id="seasons-list" class="bg-dark p-b-0">(.*?)<section id="category-posts"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult      
    Pattern = "<a href='(.+?)' class='.+?'>(.+?)</a>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'FilmABCdef', sTitle, '', '', '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()


def FilmABCdef():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    le = oInputParameterHandler.getValue('sMovieTitle')
    #abc = 'https://www.dizibox.tv/tum-bolumler/'
    
    sHtmlContent=getHtml(Url) 
     
                
    Pattern = '<div class="post-title">.+?<a href="(.+?)" class="season-episode link-unstyled full-width">(.+?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    
    if not (aResult[0] == False):
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
           
            sTitle = malfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'mHosters', sTitle, '', '', '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()



   

def FilmABCD():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                      
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request();
    sPicture= re.search('<i class="icon icon-youtube">.+?<img src="(.+?)"', sHtmlContent).group(1)+ TIK
    BILGI=re.search('<div class="tv-story-wrapper m-t-2">.+?<p>(.+?)</p>', sHtmlContent).group(1)
    if '<div class="post-title">' in sHtmlContent:
         oParser = cParser()
         Pattern = '<div class="post-title">.*?<a href="([^"]+)" class="season-episode link-unstyled full-width">([^<]+)</a>'
         oParser = cParser()
         aResult = oParser.parse(sHtmlContent, Pattern)
    else:
         Pattern2 = "<a href='([^']+)' class='btn btn-s btn-default-ligh.*?'>([^<]+)</a>"
         oParser = cParser()
         aResult = oParser.parse(sHtmlContent, Pattern2) 
    
    
    
    if not (aResult[0] == False):
        total = len(aResult[1])
       
        for aEntry in aResult[1]:
            sTitle = malfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
#            oGui.addTV(SITE_IDENTIFIER, 'Hosters',sTitle, '', '', '', oOutputParameterHandler)
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, BILGI, oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def ASCIIDecode(string):

    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+2)] == '\\x':
            c = chr(int(string[(i+2):(i+4)], 16))
            i+=3
        if string[i:(i+2)] == '\\u':
            cc = int(string[(i+2):(i+6)], 16)
            if cc > 256:
                #ok c'est de l'unicode, pas du ascii
                return ''
            c = chr(cc)
            i+= 5
        ret = ret + c
        i = i + 1

    return ret
 
        

     



def hextranslate(s):
        res = ""
        for i in range(len(s)/2):
                realIdx = i*2
                res = res + chr(int(s[realIdx:realIdx+2],16))
        return res    
     



  
def __checkForNextPage(sHtmlContent):
    sPattern = '<span class="current">.+?</span> <a href="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]                              

    return False

 

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request();
    if not "<option class='woca-current-page'" in sHtmlContent:
         dizibox2(Url) 
#               
    
    sPattern = "<option value='(.*?)'>(.*?)</option>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        for aEntry in aResult[1]:
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            sUrl = (aEntry[0])
            
            sDisplayTitle = malfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'dizibox', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
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
            url = (url).replace("#", "|")
            url = url.strip()  # 
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')    
  
def dizibox2(url):  
  data= requests.session().get(url ,headers={"Referer": "https://www.dizibox.pw/","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Host": "www.dizibox.pw","Connection": "Keep-Alive","Upgrade-Insecure-Requests": "1"}).text
  return data



def MakeToken(sLoc):
        
        def base36encode(number):
            if not isinstance(number, (int, long)):
                raise TypeError('number must be an integer')
            if number < 0:
                raise ValueError('number must be positive')
            alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            base36 = ''
            while number:
                number, i = divmod(number, 36)
                base36 = alphabet[i] + base36
            return base36 or alphabet[0]
            
        #oRequest = cRequestHandler('http://www.wat.tv/servertime2')
        #stime = oRequest.request()
        #stime = base36encode(int(stime))
            
        stime = base36encode(int(time.time()))

        timesec = hex(int(stime, 36))[2:]
        while(len(timesec)<8):
            timesec = "0" + timesec

        key = '9b673b13fa4682ed14c3cfa5af5310274b514c4133e9b3a81e6e3aba009l2564'
        token = md5.new(key + sLoc + timesec).hexdigest() + '/' + timesec
        return token