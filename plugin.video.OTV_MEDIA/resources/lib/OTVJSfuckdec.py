#-*- coding: utf-8 -*-
# Name:        otv-jsfuckdecoder
# Purpose:
# Version:     2.0
# Author:      orhan
#
# Created:     05.03.2022
# Copyright:   (c) orhan 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import re
from future.utils import iteritems     
       
class OTVJSfuck(object):
 KARAKTER_KODUNU_KULLAN = "KARAKTER_KODUNU_KULLAN"
 SIMPLE = {
        'Infinity':   '+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])',
        'dogru':       '!![]',      
        'tanimsiz':  '[][[]]',
        'NaN':        '+[![]]',
         'Numara':   '(+[])',
        'Sicim':   '([]+[])',  
        'Dizi':   '([][])',                                         
        'Boole':  '(![])',
        'islev': '[][fill]',     
        'yanlis':      '![]',  
    }
                 

 LMAPPING = {                 
        'a':   '(yanlis[])[1]',
        'b':   '([][entries]()[])[2]',
        'd':   '(tanimsiz[])[2]',
        'e':   '(dogru[])[3]',
        'f':   '(yanlis[])[0]',
        'g':   '(yanlis[0]Sicim)[20]',
        'h':   '((101))[toSicim[name]](21)[1]',      
        'i':   '([yanlis]tanimsiz)[10]',              
        'j':   '([][entries]()[])[3]',
        'k':   '((20))[toSicim[name]](21)',
        'l':   '(yanlis[])[2]',
        'n':   '(tanimsiz[])[1]',
        'o':   '(dogru[][fill])[10]',  
        'p':   '((2[1][1]))[toSicim[name]](31)[1]',
        'p':   '((211))[toSicim[name]](31)[1]',      
        'q':   '((212))[toSicim[name]](31)[1]',              
        'r':   '(dogru[])[1]',                   
        's':   '(yanlis[])[3]',
        't':   '(dogru[])[0]',                                   
        'u':   '(tanimsiz[])[0]',
        'v':   '((31))[toSicim[name]](32)',
        'w':   '((32))[toSicim[name]](33)',
        'x':   '((101))[toSicim[name]](34)[1]', 
        'y':   '(NaN[Infinity])[10]',
        'z':   '((35))[toSicim[name]](36)',    
        'A':   '([][])[10]',     #([]Dizi)[10]
        'B':   '([]Boole)[10]',
        'C':   '[][fill](return escape)()(Sicim[italics]())[2]',                      
        'D':     '[][fill](return escape)()([][fill])[slice](-1)',
        'F':   '([][][fill])[10]',
        'G':   '(yanlis[][fill](return Date)()())[30]',
        'H':   KARAKTER_KODUNU_KULLAN,
        'I':   '(Infinity[])[0]',
        'J':   KARAKTER_KODUNU_KULLAN,
        'K':   KARAKTER_KODUNU_KULLAN,
        'L':   KARAKTER_KODUNU_KULLAN,
        'M':   '(dogru[][fill](return Date)()())[30]',         
        'N':   '(NaN[])[0]',
        'P':   KARAKTER_KODUNU_KULLAN,                    
        'Q':   KARAKTER_KODUNU_KULLAN,                 
        'S':   '([]Sicim)[10]',
        'T':   '(NaN[][fill](return Date)()())[30]',               
        'V':   KARAKTER_KODUNU_KULLAN,
        'W':   KARAKTER_KODUNU_KULLAN,
        'X':   KARAKTER_KODUNU_KULLAN,
        'Y':   KARAKTER_KODUNU_KULLAN,
        'Z':   KARAKTER_KODUNU_KULLAN,            
        '.':   '((11e20)[])[1]',                
        ' ':   '(NaN[][fill])[11]',            
        '!':   KARAKTER_KODUNU_KULLAN,                       
        '"':   'Sicim[fontcolor]()[12]',
        '#':   KARAKTER_KODUNU_KULLAN,                  
        '$':   KARAKTER_KODUNU_KULLAN,
        '%':   '[][fill](return escape)()([][fill])[21]',     
        '\'':  KARAKTER_KODUNU_KULLAN,
        '(':   '(tanimsiz[][[fill[])[22]',
        ')':   '([0]yanlis[][[fill[])[20]',
        '*':   KARAKTER_KODUNU_KULLAN,                                 
        '':   ('((![](![][])[![]![]![]]'
                '[![]][[]][[]])[])[2]'),
        ',':   '([][[slice[][[call[](yanlis[])[])[1]',
        '-':   '((.[[]000000001])[])[2]',
         '/':   '(yanlis[0])[italics]()[10]',                   
        ':':   '([][fill](return/yanlis/)()()[])[3]',
        ';':   '([])[[link[]([)[14]',                               
        '<':   '([])[[italics[]()[0]',
        '=':   'Sicim[fontcolor]()[11]',
        '>':   '([])[[italics[]()[2]',
        '?':   '([][fill](return/yanlis/)()()[])[2]',
        '@':   KARAKTER_KODUNU_KULLAN,                           
        '[':   '([][[entries[]()[])[0]',
        '\\':  KARAKTER_KODUNU_KULLAN,
        ']':   '([][[entries[]()[])[22]',
        '^':   KARAKTER_KODUNU_KULLAN,                                     
        '_':   KARAKTER_KODUNU_KULLAN,
        '`':   KARAKTER_KODUNU_KULLAN,
        '{':   '(dogru[][fill])[20]',             
        '|':   KARAKTER_KODUNU_KULLAN,                                        
        '}':   '([][fill][])[slice](-1)',  
        'c':   '([][fill][])[3]',          
        'm':   '(Numara[])[11]',                            
        '':   '(([][fill(return/yanlis/)()(/)[])[1])',             
        'orhantv':   ')[split(t)[join]")()',
        'orhantv':   '[][fill(return"(',
        'orhantv':   ')split(t)join")()',
        'E':   '([][fill](return/yanlis/)()[])[12]', #(RegExp[])[12]  
        'U':   '(NaN[][fill](return{})()[toSicim[name]][call]())[11]',
        'R':   '([][][fill](return/yanlis/)())[10]',              
        'O':   '(NaN[][fill](return{})())[11]',   
        '&':   'Sicim[link](0")[10]',           
        'orhantv':   '[][fill](return unescape)()',                                    
        '~':   KARAKTER_KODUNU_KULLAN           
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
              js =  js.replace('t334','Ãœ')
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
              js =  js.replace('t247','ï¿½') 
              js =  js.replace('t100','@')  
              js =  js.replace('t43','#') 
              js =  js.replace('t42','"')  
              js =  js.replace('t41','!')  
              js =  js.replace('t260','ï¿½') 
              js =  js.replace('t47',"'")   
              js =  js.replace('t52','*')    
              js =  js.replace('t53','+')   
              js =  js.replace('t264','ï¿½') 
              js =  js.replace('t337','ï¿½') 
              js =  js.replace('t137','_')               
              js =  js.replace('t176','~')   
              js =  js.replace('t52','*')   
              js =  js.replace('t55','-')      
              js =  js.replace('((11e20)[])[1]','.')
              return js                                                                     
                               
 def jsfuckescape(self,Sicim):
    Sicim = Sicim.replace(')[])', '').replace("(%(", "\\x").replace(')', '').replace('orhantv', '').replace('[][fill](return unescape(', '')
    i = 0
    l = len(Sicim)
    ret = ''
    while i < l:
        c =Sicim[i]
        if Sicim[i:(i+2)] == '\\x':
            c = chr(int(Sicim[(i+2):(i+4)],16))
            i+=3
        if Sicim[i:(i+2)] == '\\t':
            c = Sicim[(i+2):(i+6)]
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
        
        js = js.replace('[])0]', '[])[0]')
        js = js.replace('[])0', '[])[0]')
        js = js.replace('[])1', '[])[1]')                                                                                                                                                                                                                                                                                                                                                                  
        js = js.replace('[])2', '[])[2]')
        js = js.replace('[])3', '[])[3]')
        js = re.sub('\+(?!\+)', '', js)
        js = js.replace('++', '+').replace('(![]01)', '(101)').replace('![]![]![]![]![]', '5').replace('![]![]![]![]', '4').replace('[![]1]', '[11]').replace('(![]![]![]', '(3').replace('(![]![]', '(2').replace('[![]![]![]', '[3').replace('[![]![]', '[2').replace('(![]', '(1').replace('[![]', '[1').replace('yanlis[]3', '(yanlis[])[3]').replace('(yanlis[]2', '(yanlis[])[2]').replace('(yanlis[]1', '(yanlis[])[1]').replace('(yanlis[]0', '(yanlis[])[0]')
        if not  '[0]' in js:
            js = js.replace('[])0]', '[])[0]')
            js = js.replace('[])0', '[])[0]')
            js = js.replace('[])1', '[])[1]')                                                                                                                                                                                                                                                                                                                                                                  
            js = js.replace('[])2', '[])[2]')
            js = js.replace('[])3', '[])[3]')
            js = js.replace('[])0]', '[])[0]')
            js = js.replace('[]0', '[])[0]')
            js = js.replace('[]1', '[])[1]')
            js = js.replace('[]2', '[])[2]')
            js = js.replace('[]3', '[])[3]')
        js = self.repl_mapp(js)                                                                                                                                
        if 'flat' in js or 'filter' in js:                                                                                               
            js = js.replace('filter', 'flat') 
            js = js.replace('(dogru[][flat)[10]', '(dogru[][fill])[10]').replace('([][flat[])[3]', '([][fill][])[3]').replace('flat', 'fill')   
            js =self.repl_octal(js)                                                                                                                                    
            js = js.replace('(31)1', '(31)[1]')
            js = js.replace('(yanlis0)', '(yanlis[0])')                         
            js = js.replace('[])0]', '[])[0]')
            js = js.replace('[])0', '[])[0]')                                                                                                                  
            js = js.replace('[])1', '[])[1]')
            js = js.replace('[])2', '[])[2]')                                                
            js = js.replace('[][fill(return"(', '')    
            js = js.replace('(yanlisSicim)[10]', 'S').replace('(yanlisNaNSicim)[20]', 'g[name]').replace('String', 'Sicim')    
            js =self.repl_octal(js) 
            js =self.repl_octal(js) 
            js =  js.replace('((11e20)[])[1]','.').replace('(yanlis[yanlis])[italics]()[10]', '/').replace('[1]', '') .replace('[0]', '')  
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

