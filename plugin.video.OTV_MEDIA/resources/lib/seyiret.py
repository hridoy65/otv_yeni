#!/usr/bin/env python

import sys
import re
try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

from future.utils import iteritems     
try:
    import ssl
    import socket
    timeout = 30
    socket.setdefaulttimeout(timeout)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
except ImportError:
    pass
try:
    import json
    import math
    import httplib
except:
    pass
try:
    import http.cookiejar as cookielib
    from urllib.parse import urlencode as Urlencode
    from urllib.parse import unquote_plus as Unquote_plus
    from urllib.parse import unquote as Unquote
    from urllib.parse import quote 
    from urllib.parse import urlparse 
    from urllib.parse import urljoin 
    from urllib.parse import parse_qsl 
    from urllib.parse import parse_qs 
    from html.parser import HTMLParser
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPHandler
    from urllib.request import install_opener
    PY3 = True; unicode = str; unichr = chr; long = int
except:
    import cookielib
    from HTMLParser import HTMLParser
    from urllib import urlencode as Urlencode
    from urllib import unquote_plus as Unquote_plus
    from urllib import unquote as Unquote
    from urllib import quote 
    from urlparse import urlparse 
    from urlparse import urljoin 
    from urlparse import parse_qsl 
    from urlparse import parse_qs 
    from urllib2 import Request    
    from urllib2 import urlopen
    from urllib2 import HTTPCookieProcessor
    from urllib2 import build_opener
    from urllib2 import HTTPBasicAuthHandler
    from urllib2 import HTTPHandler
    from urllib2 import install_opener  

       
class OTVJSfuck(object):
 USE_CHAR_CODE = "USE_CHAR_CODE"
 SIMPLE = {
        'Infinity':   '+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])',
        'true':       '!![]',      
        'undefined':  '[][[]]',
        'NaN':        '+[![]]',
         'Number':   '(+[])',
        'String':   '([]+[])',  
        'Array':   '([][])',                                         
        'Boolean':  '(![])',
        'Function': '[][fill]',     
        'false':      '![]',  
    }


 LMAPPING = {                 
        'a':   '(false[])[1]',
        'b':   '([][entries]()[])[2]',
        'd':   '(undefined[])[2]',
        'e':   '(true[])[3]',
        'f':   '(false[])[0]',
        'g':   '(false[0]String)[20]',
        'h':   '((101))[toString[name]](21)[1]',      
        'i':   '([false]undefined)[10]',              
        'j':   '([][entries]()[])[3]',
        'k':   '((20))[toString[name]](21)',
        'l':   '(false[])[2]',
        'n':   '(undefined[])[1]',
        'o':   '(true[][fill])[10]',  
        'p':   '((2[1][1]))[toString[name]](31)[1]',
        'p':   '((211))[toString[name]](31)[1]',      
        'q':   '((212))[toString[name]](31)[1]',              
        'r':   '(true[])[1]',                   
        's':   '(false[])[3]',
        't':   '(true[])[0]',                                   
        'u':   '(undefined[])[0]',
        'v':   '((31))[toString[name]](32)',
        'w':   '((32))[toString[name]](33)',
        'x':   '((101))[toString[name]](34)[1]', 
        'y':   '(NaN[Infinity])[10]',
        'z':   '((35))[toString[name]](36)',    
        'A':   '([][])[10]',     #([]Array)[10]
        'B':   '([]Boolean)[10]',
        'C':   '[][fill](return escape)()(String[italics]())[2]',                      
        'D':     '[][fill](return escape)()([][fill])[slice](-1)',
        'F':   '([][][fill])[10]',
        'G':   '(false[][fill](return Date)()())[30]',
        'H':   USE_CHAR_CODE,
        'I':   '(Infinity[])[0]',
        'J':   USE_CHAR_CODE,
        'K':   USE_CHAR_CODE,
        'L':   USE_CHAR_CODE,
        'M':   '(true[][fill](return Date)()())[30]',         
        'N':   '(NaN[])[0]',
        'P':   USE_CHAR_CODE,                    
        'Q':   USE_CHAR_CODE,                 
        'S':   '([]String)[10]',
        'T':   '(NaN[][fill](return Date)()())[30]',               
        'V':   USE_CHAR_CODE,
        'W':   USE_CHAR_CODE,
        'X':   USE_CHAR_CODE,
        'Y':   USE_CHAR_CODE,
        'Z':   USE_CHAR_CODE,            
        '.':   '((11(true[])320)[])1',                
        ' ':   '(NaN[][fill])[11]',            
        '!':   USE_CHAR_CODE,                       
        '"':   'String[fontcolor]()[12]',
        '#':   USE_CHAR_CODE,                  
        '$':   USE_CHAR_CODE,
        '%':   '[][fill](return escape)()([][fill])[21]',     
        '\'':  USE_CHAR_CODE,
        '(':   '(undefined[][[fill[])[22]',
        ')':   '([0]false[][[fill[])[20]',
        '*':   USE_CHAR_CODE,                                 
        '':   ('((![](![][])[![]![]![]]'
                '[![]][[]][[]])[])[2]'),
        ',':   '([][[slice[][[call[](false[])[])[1]',
        '-':   '((.[[]000000001])[])[2]',
         '/':   '(false[0])[italics]()[10]',                   
        ':':   '([][fill](return/false/)()()[])[3]',
        ';':   '([])[[link[]([)[14]',                               
        '<':   '([])[[italics[]()[0]',
        '=':   'String[fontcolor]()[11]',
        '>':   '([])[[italics[]()[2]',
        '?':   '([][fill](return/false/)()()[])[2]',
        '@':   USE_CHAR_CODE,                           
        '[':   '([][[entries[]()[])[0]',
        '\\':  USE_CHAR_CODE,
        ']':   '([][[entries[]()[])[22]',
        '^':   USE_CHAR_CODE,                                     
        '_':   USE_CHAR_CODE,
        '`':   USE_CHAR_CODE,
        '{':   '(true[][fill])[20]',             
        '|':   USE_CHAR_CODE,
        '}':   '([][fill][])[slice](-1)',  
        'c':   '([][fill][])[3]',          
        'm':   '(Number[])[11]',                            
        '':   '(([][fill(return/false/)()(/)[])[1])',             
        'orhantv':   ')[split(t)[join]")()',
        'orhantv':   '[][fill(return"(',
        'orhantv':   ')split(t)join")()',
        'E':   '([][fill](return/false/)()[])[12]', #(RegExp[])[12]  
        'U':   '(NaN[][fill](return{})()[toString[name]][call]())[11]',
        'R':   '([][][fill](return/false/)())[10]',              
        'O':   '(NaN[][fill](return{})())[11]',   
        '&':   'String[link](0")[10]',           
        'orhantv':   '[][fill](return unescape)()',                                    
        '~':   USE_CHAR_CODE           
    }
 def __init__(self, js):
        self.js = js
 def fuckend(self,js):                    
              js =js.replace('[][fill(return"(', '').replace(')[split(t)[join]")()', '').replace('orhantv', '').replace(']', '').replace('[', '').replace(']', '')
              js =  js.replace('t101','A')  
              js =  js.replace('t102','B') 
              js =  js.replace('t103','C') 
              js =  js.replace('t104','D') 
              js =  js.replace('t105','E') 
              js =  js.replace('t106','F')                                                                                                                                                                                                              
              js =  js.replace('t107','G') 
              js =  js.replace('t110','H')  
              js =  js.replace('t111','I')  
              js =  js.replace('t112','J')  
              js =  js.replace('t113','K')  
              js =  js.replace('t114','L')  
              js =  js.replace('t115','M')  
              js =  js.replace('t117','O') 
              js =  js.replace('t120','P') 
              js =  js.replace('t121','Q') 
              js =  js.replace('t122','R') 
              js =  js.replace('t123','S')  
              js =  js.replace('t124','T')  
              js =  js.replace('t125','U')  
              js =  js.replace('t334','Ü')
              js =  js.replace('t126','V')  
              js =  js.replace('t127','W')  
              js =  js.replace('t130','X')  
              js =  js.replace('t131','Y')  
              js =  js.replace('t132','Z') 
              js =  js.replace('t142','b') 
              js =  js.replace('t143','c')                              
              js =  js.replace('t147','g')
              js =  js.replace('t150','h')    
              js =  js.replace('t152','j')  
              js =  js.replace('t153','k')   
              js =  js.replace('t155','m') 
              js =  js.replace('t157','o') 
              js =  js.replace('t160','p') 
              js =  js.replace('t161','q') 
              js =  js.replace('164a','r') 
              js =  js.replace('t164','t') 
              js =  js.replace('t166','v') 
              js =  js.replace('t167','w')               
              js =  js.replace('t170','x')          
              js =  js.replace('t171','y')          
              js =  js.replace('t172','z')             
              js =  js.replace('t174','|')
              js =  js.replace('t72',':')
              js =  js.replace('t73',';')
              js =  js.replace('t133','[')
              js =  js.replace('t135',']')
              js =  js.replace('t173','{')
              js =  js.replace('t136','^')
              js =  js.replace('t175','}')
              js =  js.replace('t54',',')
              js =  js.replace('t74','<')
              js =  js.replace('t76','>')
              js =  js.replace('t140','`')
              js =  js.replace('t77','?')
              js =  js.replace('t75','=')
              js =  js.replace('t50','(')
              js =  js.replace('t40',' ')
              js =  js.replace('t51',')')
              js =  js.replace('t57','/')
              js =  js.replace('t134','\\') 
              js =  js.replace('t46','&')                
              js =  js.replace('t45','%')  
              js =  js.replace('t44','$')  
              js =  js.replace('t247','�') 
              js =  js.replace('t100','@')  
              js =  js.replace('t43','#') 
              js =  js.replace('t42','"')  
              js =  js.replace('t41','!')  
              js =  js.replace('t260','�') 
              js =  js.replace('t47',"'")   
              js =  js.replace('t52','*')    
              js =  js.replace('t53','+')   
              js =  js.replace('t264','�') 
              js =  js.replace('t337','�') 
              js =  js.replace('t137','_')               
              js =  js.replace('t176','~')   
              js =  js.replace('t52','*')   
              js =  js.replace('t55','-')      
              js =  js.replace('((11e20)[])[1]','.')
              return js                                                                     
                               
 def jsfuckescape(self,string):
    string = string.replace(')[])', '').replace("(%(", "\\x").replace(')', '').replace('orhantv', '').replace('[][fill](return unescape(', '')
    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+2)] == '\\x':
            c = chr(int(string[(i+2):(i+4)],16))
            i+=3
        if string[i:(i+2)] == '\\t':
            c = string[(i+2):(i+6)]
            c=c.replace('\\', '').replace('(', '').replace('x', '')#.replace('40', '')
            c = chr(int(c,8))                                     
            i+=5     
        ret = ret + c
        i += 1
    return ret                                       
 def decode(self):       
 
            js =self.decode2()         
            js =self.jsfuckescape(js)
            return js    
  
 def repl_mapp(self, js):
        x = 0
        while x < 4:                        
            start_js = self.js
            for key, val in iteritems(self.LMAPPING):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                js = js.replace(val, key)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                js = js.replace('[constructor]', '')
            if start_js == self.js:
                break                  
               
        return js
 def repl_octal(self, js):
        x = 0
        while x < 4:
            start_js = self.js
            for key, val in iteritems(self.LMAPPING):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                js = js.replace(val, key)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                js = js.replace('[constructor]', '')
            if start_js == self.js:
                break                  
        return js               

 def decode2(self, js=None):
        js = self.js                  
        js = js.replace('+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])', 'Infinity')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]', '9')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]', '8')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]', '7')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]', '6')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]+!+[]]', '5')
        js = js.replace('[!+[]+!+[]+!+[]+!+[]]', '4')
        js = js.replace('[!+[]+!+[]+!+[]]', '3')
        js = js.replace('[!+[]+!+[]]', '2')
        js = js.replace('[+!+[]]', '1')
        js = js.replace('[+[]]', '0')
        js = js.replace('[+!+[]+', '[1').replace('(+!+[]+0+1)', '(101)')
        for key, val in iteritems(self.SIMPLE):                                                                                                                   
            js = js.replace(val, key)                                                                                                                                                                                                                                                  
        logger.info("js-1-----...%s" %js)                                                                                                                      
        js = re.sub('\+(?!\+)', '', js)
        js = js.replace('++', '+').replace('(![]01)', '(101)').replace('![]![]![]![]![]', '5').replace('![]![]![]![]', '4').replace('[![]1]', '[11]').replace('(![]![]![]', '(3').replace('(![]![]', '(2').replace('[![]![]![]', '[3').replace('[![]![]', '[2').replace('(![]', '(1').replace('[![]', '[1')#.replace('![]![]![]', '3').replace('![]![]', '2').replace('![]', '1')
        if not  '[0]' in js:
            js = js.replace('[])0]', '[])[0]')
            js = js.replace('[])0', '[])[0]')
            js = js.replace('[])1', '[])[1]')
            js = js.replace('[])2', '[])[2]')
            js = js.replace('[])3', '[])[3]')
        js = self.repl_mapp(js)                                                                                                                                
        if 'flat' in js:                                                                                               
            js = js.replace('(true[][flat)[10]', '(true[][fill])[10]').replace('([][flat[])[3]', '([][fill][])[3]').replace('flat', 'fill')  
            js =self.repl_octal(js)                                                                                                                                    
            js = js.replace('(31)1', '(31)[1]')
            js = js.replace('(false0)', '(false[0])')                         
            js = js.replace('[])0]', '[])[0]')
            js = js.replace('[])0', '[])[0]')
            js = js.replace('[])1', '[])[1]')
            js = js.replace('[])2', '[])[2]')
            js = js.replace('[][fill(return"(', '')     
            js =self.repl_octal(js) 
            js =self.repl_octal(js) 
            js =self.fuckend(js) 
            return js 
        js =self.repl_mapp(js)
        if '[][fill][constructor]' in js:
            js = self.uneval(js)
        self.js = js
        return js
 def uneval(self, js):
        js = js.replace('[][fill][constructor](', '')
        js = js[:-2]
        ev = 'return eval)()('
        if ev in js:
            js = js[(js.find(ev) + len(ev)):]
        return js

