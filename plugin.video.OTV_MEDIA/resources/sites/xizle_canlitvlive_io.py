#-*- coding: utf-8 -*-
from resources.sites.LIVETV2 import *
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
#from resources.lib.gui.guiElement import cGuiElement
#canlitvio.png
SITE_IDENTIFIER = 'xizle_canlitvlive_io'
SITE_NAME = 'xizle_canlitvlive_io'

def sEcho(s):
    s=s
    if '=1' in s:
        s=s.replace('=1','=2')
        return s 
    if '=2' in s:
        s=s.replace('=2','=3')
        return s 
    if '=3' in s:	
        s=s.replace('=3','=4')
        return s 
    if '=4' in s:	
        s=s.replace('=4','=5')
        return s 
    if '=5' in s:	
        s=s.replace('=5','=6')
        return s 
  
def Canlitvlive_io():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    oParser = cParser()
    Uurl = "https://izle.canlitvlive.io" 

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Uurl, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
       print(e.read())
       print(e.reason)

    sHtmlContent = response.read()
    head = response.headers
    response.close()
    cookies = head['Set-Cookie']
    sPattern = '(__cfduid=[0-9a-z]+;).+?(PHPSESSID=[0-9a-z]+)'
    aResult = oParser.parse(str(cookies), sPattern)
    if (aResult[0] == True):
        cookies = str(aResult[1][0][0]) + str(aResult[1][0][1])
    sPattern = '<a href="(https://izle.canlitvlive.io/.*?)" title="(.*?)">'
                
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
           
            sTitle = aEntry[1]
            sPicture = 'https://izle.canlitvlive.io/assets/v5/img/apple-icon-180x180.png'

            sUrl = str(aEntry[0])
                                        
            sTitle = malfabekodla(sTitle)
            sTitle =sTitle.replace('Ä±','ı').replace('Ã','Ç').replace('Ã¼','ü')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
            oGui.addMovie(SITE_IDENTIFIER, 'Canlitvlive2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
  
    oGui.setEndOfDirectory()

def Canlitvlive2():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    oParser = cParser()
  

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Url, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
       print(e.read())
       print(e.reason)

    sHtmlContent = to_utf8(response.read())
    head = response.headers
    response.close()
   
   
#    cf =to_utf8(body)
    sPattern = '<li class=jgifhover data-bg-normal=".*?" data-bg-hover="(.*?)".*?<a href="(.*?)" title="(.*?)"'
                
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])

        for aEntry in aResult[1]:
           
            sTitle = aEntry[2]
            sPicture = aEntry[0]

            sUrl ='https://izle.canlitvlive.io'+ str(aEntry[1])
                                                       
            sTitle = malfabekodla(sTitle)
            sTitle =sTitle.replace('Ä±','ı').replace('Ã','Ç').replace('Ã¼','ü').replace('Å','ş').replace('Ã§','ç').replace('Ã¶','ö')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'Canlitvlivedecode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
  
    oGui.setEndOfDirectory()

def deCFEmail(fp):                                                                                          
        try:
            r = int(fp[:2],16)
            email = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)])
            return email
        except (ValueError):
            pass

def cookie2( Url ):
    oGui = cGui()
   
    
  

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Url, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
       print(e.read())
       print(e.reason)

    sHtmlContent = to_utf8(response.read())
    head = response.headers
    return head
#    sPattern = 'Set-Cookie: token=(.*?);'
#    oParser = cParser()
#    aResult = oParser.parse(head, sPattern)
#    if (aResult[0] == True):
#         return  aResult[1][0]

def Canlitvlivedecode():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    logger.info("Urrl : %s" % Urrl )
    Uurl = "https://izle.canlitvlive.io" 

    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {"User-Agent": UA}
    req = urllib2.Request(Uurl, None, headers)
    try:
       response = urllib2.urlopen(req)
    except UrlError as e:
     #  print(e.read())
       print(e.reason)
                    
    sHtmlContent = response.read()
    head = to_utf8(response.headers)
    response.close()
    cookies = head['Set-Cookie']
    sPattern = '(__cfduid=[0-9a-z]+;).+?(PHPSESSID=[0-9a-z]+)'
    aResult = oParser.parse(str(cookies), sPattern)
    if (aResult[0] == True):
        cookies = str(aResult[1][0][0]) + str(aResult[1][0][1])

    headers = {'Host': 'izle.canlitvlive.io',
                   'Connection': 'keep-alive',
                   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                   'sec-ch-ua-mobile': '?0',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Sec-Fetch-Site': 'none',
                   'Sec-Fetch-Mode': 'navigate',
                   'Sec-Fetch-User': '?1',
                   'Sec-Fetch-Dest': 'document',
                   'Referer': Urrl,
                   'Accept-Language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
                   'Cookie': cookies }
   
  
    req = urllib2.Request(Urrl, None, headers)
    response = urllib2.urlopen(req)
    body = response.read()
    head = response.headers
    response.close()
    logger.info("cookies : %s" % cookies )    
    cf =to_utf8(body)
    if not  '/cdn-cgi/l/email-protectio' in cf:
        tokenn= re.search('"token": "(.+?)"', cf).group(1)
        payload = {'token' : tokenn}
    else: 
        cfmail= re.search('<a href="/cdn-cgi/l/email-protection#(.+?)">', cf).group(1)
        token= re.search('data-cfemail="(.+?)"', cf).group(1)
        decodemail=deCFEmail(cfmail)
        payload = {'email' : decodemail ,'data' : token}
    #'https://izle.canlitvlive.io/ctlio.php?data={"url":"https://izle.canlitvlive.io/watch.php?tv=show-tv","ref":"","ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","if":false,"ifurl":"2"}
    #https://izle.canlitvlive.io/ctlio.php?data=%7B%22url%22%3A%22https%3A%2F%2Fizle.canlitvlive.io%2Fwatch.php%3Ftv%3Dshow-tv%22%2C%22ref%22%3A%22%22%2C%22ua%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F98.0.4758.102%20Safari%2F537.36%22%2C%22if%22%3Afalse%2C%22ifurl%22%3A%222%22%7D
   # Urrlm='https://izle.canlitvlive.io/ctlio.php?data=%7B%22url%22%3A%22https%3A%2F%2Fizle.canlitvlive.io%2Fshow-tv-canli-izle-220304%22%2C%22ref%22%3A%22https%3A%2F%2Fizle.canlitvlive.io%2F%22%2C%22ua%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F98.0.4758.102%20Safari%2F537.36%22%2C%22if%22%3Afalse%2C%22ifurl%22%3A%222%22%7D'
#    Urrlm='https://raw.githubusercontent.com/orhantv/otv_yeni/master/plugin.video.OTV_MEDIA/220301.html'
    
#    tent = getHtml(Urrlm) 
    #logger.info("tent : %s" % tent )
    from OTVJSfuckdec import OTVJSfuck  
#    data= re.search('mplayer.src\((.+?)\);',cf).group(1)
   # Urll=OTVJSfuck(data).decode()
   # logger.info("Urrl : %s" % data )
    
    Ur= OTVJSfuck(cf).decode()
    Urll= re.search('mplayer.src.(.+?);',Ur).group(1)
    #logger.info("cookies : %s" % cookies )
    headerss = {   'Host': 'izle.canlitvlive.io',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                   'Accept': '*/*',
                   'Accept-Language': 'de-DE,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2',
                   'Connection': 'keep-alive',
                   'Referer': Urrl,
                   'Cookie': cookies}                     
   
   
                                      
    
    s = requests.Session()
    r = s.post(Urll ,  headers=headerss,data=payload , allow_redirects=False)
    urrl=r.headers['Location']
  
    logger.info("Urrl : %s" % urrl)
    Urll =urrl+'|Host=str01.mitream.net&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36&Referer='+Urrl
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,Urll ,'')  
      



#print("OK")#?data=%7B%22url%22%3A%22https%3A%2F%2Fizle.canlitvlive.io%2Fwatch.php%3Ftv%3Dshow-tv%22%2C%22ref%22%3A%22%22%2C%22ua%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F98.0.4758.102%20Safari%2F537.36%22%2C%22if%22%3Afalse%2C%22ifurl%22%3A%222%22%7D                               
def addLink(name, url, iconimage):
    ok = True
    
    liz = xbmcgui.ListItem(name)
    liz.setInfo(type='video', infoLabels={'Title': name})
    liz.setArt({'thumb': iconimage, 'icon': iconimage, 'fanart': iconimage})
    liz.setProperty('Fanart_Image', iconimage)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
    xbmc.Player().play(url,liz)
    sys.exit()
    return ok 



