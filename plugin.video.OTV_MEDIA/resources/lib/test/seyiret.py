# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import re
try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range
from phpserialize import unserialize
from resources.lib.logger import logger 

import json
from collections import OrderedDict

# Manage core logic by this class
class Settlement :
    @staticmethod
    def default_key(d):
        result = 0
        for key, _ in d.items():
           	# Check key is integer and key is not less than result
            if(type(key) is int and key >= result) :
                # Get new key
                result = key + 1
        return result
    
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# file_exists
# file_get_contents
# unserialize
# serialize
# file_put_contents
# preg_match_all
# key_exists
# ord
# join
# preg_match
# preg_replace
# chr
#----------------------------

class JSFuck :
    MIN = 32;
    MAX = 126;
    USE_CHAR_CODE = 'USE_CHAR_CODE';
    SIMPLE = OrderedDict([('false','![]'),('true','!![]'),('undefined','[][[]]'),('NaN','+[![]]'),('Infinity','+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])')]);
    CONSTRUCTORS = OrderedDict([('Array','[]'),('Number','(+[])'),('String','([]+[])'),('Boolean','(![])'),('RegExp','Function("return/"+false+"/")()'),('Function','[]["fill"]')]);
    MAPPING = OrderedDict([('a','(false+"")[1]'),('b','([]["entries"]()+"")[2]'),('c','([]["fill"]+"")[3]'),('d','(undefined+"")[2]'),('e','(true+"")[3]'),('f','(false+"")[0]'),('g','(false+[0]+String)[20]'),('h','(+(101))["to"+String["name"]](21)[1]'),('i','([false]+undefined)[10]'),('j','([]["entries"]()+"")[3]'),('k','(+(20))["to"+String["name"]](21)'),('l','(false+"")[2]'),('m','(Number+"")[11]'),('n','(undefined+"")[1]'),('o','(true+[]["fill"])[10]'),('p','(+(211))["to"+String["name"]](31)[1]'),('q','(+(212))["to"+String["name"]](31)[1]'),('r','(true+"")[1]'),('s','(false+"")[3]'),('t','(true+"")[0]'),('u','(undefined+"")[0]'),('v','(+(31))["to"+String["name"]](32)'),('w','(+(32))["to"+String["name"]](33)'),('x','(+(101))["to"+String["name"]](34)[1]'),('y','(NaN+[Infinity])[10]'),('z','(+(35))["to"+String["name"]](36)'),('A','(+[]+Array)[10]'),('B','(+[]+Boolean)[10]'),('C','Function("return escape")()(("")["italics"]())[2]'),('D','Function("return escape")()([]["fill"])["slice"]("-1")'),('E','(RegExp+"")[12]'),('F','(+[]+Function)[10]'),('G','(false+Function("return Date")()())[30]'),('H',JSFuck().USE_CHAR_CODE),('I','(Infinity+"")[0]'),('J',JSFuck().USE_CHAR_CODE),('K',JSFuck().USE_CHAR_CODE),('L',JSFuck().USE_CHAR_CODE),('M','(true+Function("return Date")()())[30]'),('N','(NaN+"")[0]'),('O','(NaN+Function("return{}")())[11]'),('P',JSFuck().USE_CHAR_CODE),('Q',JSFuck().USE_CHAR_CODE),('R','(+[]+RegExp)[10]'),('S','(+[]+String)[10]'),('T','(NaN+Function("return Date")()())[30]'),('U','(NaN+Function("return{}")()["to"+String["name"]]["call"]())[11]'),('V',JSFuck().USE_CHAR_CODE),('W',JSFuck().USE_CHAR_CODE),('X',JSFuck().USE_CHAR_CODE),('Y',JSFuck().USE_CHAR_CODE),('Z',JSFuck().USE_CHAR_CODE),(' ','(NaN+[]["fill"])[11]'),('!',JSFuck().USE_CHAR_CODE),('"','("")["fontcolor"]()[12]'),('#',JSFuck().USE_CHAR_CODE),('$',JSFuck().USE_CHAR_CODE),('%','Function("return escape")()([]["fill"])[21]'),('&','("")["link"](0+")[10]'),('\'',JSFuck().USE_CHAR_CODE),('(','(undefined+[]["fill"])[22]'),(')','([0]+false+[]["fill"])[20]'),('*',JSFuck().USE_CHAR_CODE),('+','(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]])+[])[2]'),(',','([]["slice"]["call"](false+"")+"")[1]'),('-','(+(.+[0000000001])+"")[2]'),('.','(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]'),('/','(false+[0])["italics"]()[10]'),(':','(RegExp()+"")[3]'),(';','("")["link"](")[14]'),('<','("")["italics"]()[0]'),('=','("")["fontcolor"]()[11]'),('>','("")["italics"]()[2]'),('?','(RegExp()+"")[2]'),('@',JSFuck().USE_CHAR_CODE),('[','([]["entries"]()+"")[0]'),('\\',JSFuck().USE_CHAR_CODE),(']','([]["entries"]()+"")[22]'),('^',JSFuck().USE_CHAR_CODE),('_',JSFuck().USE_CHAR_CODE),('`',JSFuck().USE_CHAR_CODE),('{','(true+[]["fill"])[20]'),('|',JSFuck().USE_CHAR_CODE),('}','([]["fill"]+"")["slice"]("-1")'),('~',JSFuck().USE_CHAR_CODE)]);
    GLOBAL = 'Function("return this")()';
    def __init__(self,string) :
        if string:
            #data = file_get_contents("jsfuck.data");
            self.MAPPING = unserialize(string);
        else : 
            self.FillMissingChars();
            self.FillMissingDigits();
            self.ReplaceMap();
            self.ReplaceStrings();
            #data = serialize(self.MAPPING);
            #file_put_contents("jsfuck.data", data);
        
    
    def Encode(self,string , wrapWithEval = False, runInParentScope = False):
        output = OrderedDict([]);
        r = "";
        for i,val in self.SIMPLE.items() :
            r += "" + str(i) + "|";
        
        
        r += ".";
        if (re.findall("/" + str(r) + "/",  matches)) :
            for find in matches[0].values() : 
                if (key_exists(find, self.SIMPLE)) :
                    output[Settlement.default_key(output)] = str("[" + str(JSFuck().SIMPLE[find])) + "]+[]";
                else : 
                    if (key_exists(find, self.MAPPING)) :
                        output[Settlement.default_key(output)] = self.MAPPING[find];
                    else : 
                        replacement = str(str(str(str(str("([]+[])[" + str(self.Encode("constructor"))) + "][") + str(self.Encode("fromCharCode"))) + "](") + str(self.Encode((string) ord(find)))) + ")";
                        output[Settlement.default_key(output)] = replacement;
                        self.MAPPING[find] = replacement;
                    
                
            
        
        output = join("+", output);
        if (re.search("/^\\d\$/", input)) :
            output += "+[]";
        
        if (wrapWithEval) :
            if (runInParentScope) :
                output = str(str(str(str(str("[][" + str(self.Encode("fill"))) + "][") + str(self.Encode("constructor"))) + "](") + str(self.Encode("return eval"))) + str(")()(" + str(output) + ")");
            else : 
                output = str(str(str("[][" + str(self.Encode("fill"))) + "][") + str(self.Encode("constructor"))) + str("](" + str(output) + ")()");
            
        
        return output;
    
    def FillMissingChars(self) :
      def replace(pattern, replacement):
          return re.sub(pattern, replacement, value, flags=re.I)

        for key,value in self.MAPPING.items() :
            if (value == self.USE_CHAR_CODE) :
                charCode = ord(key);
                charCodeHex = hex(charCode);
                replace = replace('/(\\d+)/', '+($1)+"', charCodeHex);
                self.MAPPING[key] = str('Function("return unescape")()("%"' + str(replace)) + '")';
            
        
        
    
    def FillMissingDigits(self) :
        number = 0;
        while ( number < 10 ) :
            output = "+[]";
            if (number > 0) :
                output = "+!" + str(output) + "";
            
            i = 1;
            while ( i < number ) :
                output = "+!+[]" + str(output) + "";
                i+=1;
            
            if (number > 1) :
                output = output[1: ];
            
            self.MAPPING[number] = "[" + str(output) + "]";
            number+=1;
        
    
    def ReplaceMap(self) :
       
      def replace(pattern, replacement):
          return re.sub(pattern, replacement, value, flags=re.I)
 
        i = self.MIN;
        while ( i <= self.MAX ) :
            char = chr(i);
            value = self.MAPPING[char];
            if (empty(value)) :
                continue;
            
            for key,val in self.CONSTRUCTORS.items() :
                value = replace("/\\b" + str(key) + "/", str(val) + '["constructor"]', value);
            
            
            for key,val in JSFuck().SIMPLE.items() :
                value = replace("/" + str(key) + "/", val, value);
            
            
            value = self.NumberReplacer(value, "/(\\d\\d+)/i");
            value = self.DigitReplacer(value, "/\\((\\d)\\)/i");
            value = self.DigitReplacer(value, "/\\[(\\d)\\]/i");
            value = replace("/GLOBAL/", self.GLOBAL, value);
            value = replace("/\\+\"\"/", "+[]", value);
            value = replace("/\"\"/", "[]+[]", value);
            self._MAPPING[char] = value;
            i+=1;
        
    
    def ReplaceStrings(self) :
        for key,value in self._MAPPING.items() :
            self._MAPPING[key] = self.MappingReplacer((string) value, "/\"([^\"]+)\"/i");
        
        
        count = JSFuck().MAX - JSFuck().MIN;
        while (True) :
            missing = self.FindMissing();
            if (len(missing) == 0) :
                break;
            
            for key,value in missing.items() :
                value = self.ValueReplacer(value, "/[^\\[\\]\\(\\)\\!\\+]{1}/", missing);
                self._MAPPING[key] = value;
            
            
            if (count-=1 == 0) :
                throw  Exception("Could not compile the following chars: " + json.dumps(self.FindMissing()));
            
        
    
    def FindMissing(self) -> array :
        missing = OrderedDict([]);
        for key,value in self._MAPPING.items() :
            if (re.search("/[^\\[\\]\\(\\)\\!\\+]{1}/", value)) :
                missing[key] = value;
            
        
        
        return missing;
    
    def NumberReplacer(self,matches):
        if matches:
            i = len(matches[0]) - 1;
            while ( i >= 0 ) :
                find = matches[0][i][0];
                offs = matches[0][i][1];
                begin = value[0:0 + offs];
                end = value[offs + len(find): ];
                values = OrderedDict([]);
                j = 0;
                while ( j < len(find) ) :
                    values[j] = find[j];
                    j+=1;
                
                head = (int) values.pop(next(iter(values)));
                output = "+[]";
                if (head > 0) :
                    output = "+!" + str(output) + "";
                
                j = 1;
                while ( j < head ) :
                    output = "+!+[]" + str(output) + "";
                    j+=1;
                
                if (head > 1) :
                    output = output[1: ];
                
                merged = OrderedDict({**OrderedDict([(0,output)]), **values});
                joined = join("+", merged);
                value = str(str(begin) + str(self.DigitReplacer(joined, "/(\\d)/"))) + str(end);
                i-=1;
            
        
        return value;
    
    def DigitReplacer(self,matches):
        if matches :
            i = len(matches[1]) - 1;
            while ( i >= 0 ) :
                find = matches[1][i][0];
                offs = matches[1][i][1];
                begin = value[0:0 + offs];
                end = value[offs + len(find): ];
                value = str(str(begin) + str(self._MAPPING[find])) + str(end);
                i-=1;
            
        
        return value;
    
    def MappingReplacer(self,matches):
        if matches :
            i = len(matches[1]) - 1;
            while ( i >= 0 ) :
                find = matches[1][i][0];
                offs = matches[1][i][1];
                begin = value[0:0 + offs - 1];
                end = value[offs + len(find) + 1: ];
                values = OrderedDict([]);
                j = 0;
                while ( j < len(find) ) :
                    values[j] = find[j];
                    j+=1;
                
                value = str(str(begin) + join("+", values)) + str(end);
                i-=1;
            
        
        return value;
    
    def ValueReplacer(self,matches):
        if matches:
            i = len(matches[0]) - 1;
            while ( i >= 0 ) :
                find = matches[0][i][0];
                offs = matches[0][i][1];
                begin = value[0:0 + offs];
                end = value[offs + len(find): ];
                if (not key_exists(find, missing)) :
                    value = str(str(begin) + str(self._MAPPING[find])) + str(end);
                else : 
                    value = value;
                
                i-=1;
            
        
        return value;
    



class JSUnfuckIt(object):
    '''
    Encodes/Decodes Javascript using JSFuck 0.4.0
    (https://github.com/aemkei/jsfuck)

    Class variables:
    USE_CHAR_CODE   -- string used to indicate which keys in MAPPING will
                                           be encoded using their ASCII character code

    MIN                            -- int the position within MAPPING dictionary to start
                                          iterating from, for the final encoding pass

    MAX                          -- int the maximum value to iterate in MAPPING
                                         on the final encode

    SIMPLE                    -- dictionary of built-in Javascript types and values

    CONSTRUCTORS   -- dictionary of mostly Javascript data types

    MAPPING                -- dictionary of every character to be mapped and decoded

    GLOBAL                  -- string used to replace 'GLOBAL' value on final encode

    '''

    USE_CHAR_CODE = "USE_CHAR_CODE"

    MIN, MAX = 32, 126

    SIMPLE = {
        'false':      '![]',
        'true':       '!![]',
        'undefined':  '[][[]]',
        'NaN':        '+[![]]',
        'Infinity':   ('+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+'
                       '!+[]]+[+[]]+[+[]]+[+[]])')  # +"1e1000"
    }

    CONSTRUCTORS = {
        'Array':    '[]',
        'Number':   '(+[])',
        'String':   '([]+[])',
        'Boolean':  '(![])',
        'Function': '[]["fill"]',
        'RegExp':   'Function("return/"+false+"/")()'
    }

    MAPPING = {
        'a':   '(false+"")[1]',
        'b':   '([]["entries"]()+"")[2]',
        'c':   '([]["fill"]+"")[3]',
        'd':   '(undefined+"")[2]',
        'e':   '(true+"")[3]',
        'f':   '(false+"")[0]',
        'g':   '(false+[0]+String)[20]',
        'h':   '(+(101))["to"+String["name"]](21)[1]',
        'i':   '([false]+undefined)[10]',
        'j':   '([]["entries"]()+"")[3]',
        'k':   '(+(20))["to"+String["name"]](21)',
        'l':   '(false+"")[2]',
        'm':   '(Number+"")[11]',
        'n':   '(undefined+"")[1]',
        'o':   '(true+[]["fill"])[10]',
        'p':   '(+(211))["to"+String["name"]](31)[1]',
        'q':   '(+(212))["to"+String["name"]](31)[1]',
        'r':   '(true+"")[1]',
        's':   '(false+"")[3]',
        't':   '(true+"")[0]',
        'u':   '(undefined+"")[0]',
        'v':   '(+(31))["to"+String["name"]](32)',
        'w':   '(+(32))["to"+String["name"]](33)',
        'x':   '(+(101))["to"+String["name"]](34)[1]',
        'y':   '(NaN+[Infinity])[10]',
        'z':   '(+(35))["to"+String["name"]](36)',

        'A':   '(+[]+Array)[10]',
        'B':   '(+[]+Boolean)[10]',
        'C':   'Function("return escape")()(("")["italics"]())[2]',
        'D':   'Function("return escape")()([]["fill"])["slice"]("-1")',
        'E':   '(RegExp+"")[12]',
        'F':   '(+[]+Function)[10]',
        'G':   '(false+Function("return Date")()())[30]',
        'H':   USE_CHAR_CODE,
        'I':   '(Infinity+"")[0]',
        'J':   USE_CHAR_CODE,
        'K':   USE_CHAR_CODE,
        'L':   USE_CHAR_CODE,
        'M':   '(true+Function("return Date")()())[30]',
        'N':   '(NaN+"")[0]',
        'O':   '(NaN+Function("return{}")())[11]',
        'P':   USE_CHAR_CODE,
        'Q':   USE_CHAR_CODE,
        'R':   '(+[]+RegExp)[10]',
        'S':   '(+[]+String)[10]',
        'T':   '(NaN+Function("return Date")()())[30]',
        'U':   ('(NaN+Function("return{}")()["to"+String'
                '["name"]]["call"]())[11]'),
        'V':   USE_CHAR_CODE,
        'W':   USE_CHAR_CODE,
        'X':   USE_CHAR_CODE,
        'Y':   USE_CHAR_CODE,
        'Z':   USE_CHAR_CODE,

        ' ':   '(NaN+[]["fill"])[11]',
        '!':   USE_CHAR_CODE,
        '"':   '("")["fontcolor"]()[12]',
        '#':   USE_CHAR_CODE,
        '$':   USE_CHAR_CODE,
        '%':   'Function("return escape")()([]["fill"])[21]',
        '&':   '("")["link"](0+")[10]',
        '\'':  USE_CHAR_CODE,
        '(':   '(undefined+[]["fill"])[22]',
        ')':   '([0]+false+[]["fill"])[20]',
        '*':   USE_CHAR_CODE,
        '+':   ('(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]'
                '+[+!+[]]+[+[]]+[+[]])+[])[2]'),
        ',':   '([]["slice"]["call"](false+"")+"")[1]',
        '-':   '(+(.+[0000000001])+"")[2]',
        '.':   ('(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+'
                '[]+!+[]]+[+[]])+[])[+!+[]]'),
        '/':   '(false+[0])["italics"]()[10]',
        ':':   '(RegExp()+"")[3]',
        ';':   '("")["link"](")[14]',
        '<':   '("")["italics"]()[0]',
        '=':   '("")["fontcolor"]()[11]',
        '>':   '("")["italics"]()[2]',
        '?':   '(RegExp()+"")[2]',
        '@':   USE_CHAR_CODE,
        '[':   '([]["entries"]()+"")[0]',
        '\\':  USE_CHAR_CODE,
        ']':   '([]["entries"]()+"")[22]',
        '^':   USE_CHAR_CODE,
        '_':   USE_CHAR_CODE,
        '`':   USE_CHAR_CODE,
        '{':   '(true+[]["fill"])[20]',
        '|':   USE_CHAR_CODE,
        '}':   '([]["fill"]+"")["slice"]("-1")',
        '~':   USE_CHAR_CODE
    }

    GLOBAL = 'Function("return this")()'

    def __init__(self, js):
        self.js = js

        self.__fillMissingDigits()
        self.__fillMissingChars()
        self.__replaceMap()
        self.__replaceStrings()

    def decode(self):
        '''
        Decodes JSFuck'd Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        '''
        
#        if js:
#            self.js = js
        js  =  self.js
       # js = str(js).replace('++', '+')
        js = self.__mapping(js)
        logger.info("js-%s " %js)
        # removes concatenation operators
        js = re.sub('\+(?!\+)', '', js)
        js = str(js).replace('++', '+')

        # check to see if source js is eval'd
        if '[][fill][constructor]' in js:
            js = self.uneval(js)

        self.js = js

        return js

    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        '''
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        '''
        output = []

        if not js:
            js = self.js

            if not js:
                return ''

        regex = ''

        for i in self.SIMPLE:
            regex += i + '|'

        regex += '.'

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append('[' + replacement + ']+[]')

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        '([]+[])[' + self.encode('constructor') + ']'
                        '[' + self.encode('fromCharCode') + ']'
                        '(' + self.encode(str(ord(c[0]))) + ')')

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, self.js)

        output = '+'.join(output)

        if re.search(r'^\d$', self.js):
            output += "+[]"

        if wrapWithEval:
            if runInParentScope:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + self.encode('return eval') + ')()'
                          '(' + output + ')')

            else:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + output + ')')

        self.js = output

        return output

    def uneval(self, js):
        '''
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        '''
        js = str(js).replace('[][fill][constructor](', '')
        js = js[:-2]

        ev = 'return eval)()('

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def __mapping(self, js):
        '''
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        '''             
        
        #for key in sorted(self.MAPPING, key=lambda k: len(self.MAPPING[k]), reverse=True):
       #   if self.MAPPING.get(key) in  self.js:
        #    self.js = self.js.replace(self.MAPPING.get(key), '{}'.format(key))
        
        from future.utils import iteritems
        for key, value in iteritems(self.MAPPING):
                 #for key, val in self.SIMPLE.items():
                   
       # list(self.MAPPING.get(key)), key=lambda x: len(x[1]), reverse=True):
            #logger.info("key-%s " %key)
            #logger.info("value-%s " %value)
            self.js = self.js.replace(value, key)
            logger.info("js-%s " %self.js)
        return self.js
    def l__fillMissingDigits(self):
        n = {'!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]': '9',
             '!+[]+!![]+!![]+!![]+!![]': '5', '!+[]+!![]+!![]+!![]': '4',
             '!+[]+!![]+!![]+!![]+!![]+!![]': '6', '!+[]+!![]': '2',
             '!+[]+!![]+!![]': '3', '(+![]+([]+[]))': '0', '(+[]+[])': '0', 
             '(+!![]+[])': '1', '!+[]+!![]+!![]+!![]+!![]+!![]+!![]': '7',
             '!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]': '8', '+!![]': '1',
             '[+[]]': '[0]', '!+[]+!+[]': '2', '[+!+[]]': '[1]', '(+20)': '20',
             '[+!![]]': '[1]', '[+!+[]+[+[]]]': '[10]', '+(1+1)': '11'}
        
        for i in xrange(2, 20):
            key = '+!![]' * (i - 1)
            key = '!+[]' + key
            n['(' + key + ')'] = str(i)
            key += '+[]'
            n['(' + key + ')'] = str(i)
            n['[' + key + ']'] = '[' + str(i) + ']'
     
        for i in xrange(2, 10):
            key = '!+[]+' * (i - 1) + '!+[]'
            n['(' + key + ')'] = str(i)
            n['[' + key + ']'] = '[' + str(i) + ']'
             
            key = '!+[]' + '+!![]' * (i - 1)
            n['[' + key + ']'] = '[' + str(i) + ']'
                
        for i in xrange(0, 10):
            key = '(+(+!+[]+[%d]))' % (i)
            n[key] = str(i + 10)
            key = '[+!+[]+[%s]]' % (i)
            n[key] = '[' + str(i + 10) + ']'
            
        for tens in xrange(2, 10):
            for ones in xrange(0, 10):
                key = '!+[]+' * (tens) + '[%d]' % (ones)
                n['(' + key + ')'] = str(tens * 10 + ones)
                n['[' + key + ']'] = '[' + str(tens * 10 + ones) + ']'
        
        for hundreds in xrange(1, 10):
            for tens in xrange(0, 10):
                for ones in xrange(0, 10):
                    key = '+!+[]' * hundreds + '+[%d]+[%d]))' % (tens, ones)
                    if hundreds > 1: key = key[1:]
                    key = '(+(' + key
                    n[key] = str(hundreds * 100 + tens * 10 + ones)
        return n
    def __fillMissingDigit(self) :
        number = 0;
        while ( number < 10 ) :
            output = "+[]";
            if (number > 0) :
                output = "+!" + str(output) + "";
            
            i = 1;
            while ( i < number ) :
                output = "+!+[]" + str(output) + "";
                i+=1;
            
            if (number > 1) :
                output = output[1: ];
            
            self._MAPPING[number] = "[" + str(output) + "]";
            number+=1;

    def m__fillMissingDigits(self):
        '''
        Calculates 0-9's encoded value and adds it to MAPPING

        '''
        for number in range(10):
            output = '+[]'

            if number > 0:
                output = '+!' + output

            for i in range(number - 1):
                output = '+!+[]' + output

            if number > 1:
                output = output[1:]

            self.MAPPING[str(number)] = '[' + output + ']'

    def __fillMissingChars(self):
        '''
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        '''
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r'\d+', hexidec)
                letter_search = re.findall(r'[^\d+]', hexidec)

                digit = digit_search[0] if digit_search else ''
                letter = letter_search[0] if letter_search else ''

                string = ('Function("return unescape")()("%%"+(%s)+"%s")'
                          % (digit, letter))

                self.MAPPING[key] = string

    def __replaceMap(self):
        '''
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        '''
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = '+[]'

            values.pop(0)

            if head > 0:
                output = '+!' + output

            for i in range(1, head):
                output = '+!+[]' + output

            if head > 1:
                output = output[1:]

            return re.sub(r'(\d)', digitReplacer, '+'.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = ''

            if not value:
                continue

            while value != original:
                original = value
                from future.utils import iteritems
                for  key, val in iteritems(self.CONSTRUCTORS):
                    #self.js = self.js.replace(val, key)
                #for key, val in self.CONSTRUCTORS.items():
                    value = replace(r'\b' + key, val + '["constructor"]')
               
                for  key, val in iteritems(self.SIMPLE):
                #for key, val in self.SIMPLE.items():
                    self.js = self.js.replace(val, key)
                    value = replace(key, val)
                    #value = replace(key, val)

            value = replace(r'(\d\d+)', numberReplacer)
            value = replace(r'\((\d)\)', digitReplacer)
            value = replace(r'\[(\d)\]', digitReplacer)

            value = replace(r'GLOBAL', self.GLOBAL)
            value = replace(r'\+""', '+[]')
            value = replace(r'""', '[]+[]')

            self.MAPPING[character] = value

    def __replaceStrings(self):
        '''
        Replaces strings added in __replaceMap with there encoded values

        '''
        regex = r'[^\[\]\(\)\!\+]'

        # determines if there are still characters to replace
        def findMissing():
            done = False
            # python 2 workaround for nonlocal
            findMissing.missing = {}
            from future.utils import iteritems
            for key, value in iteritems(self.MAPPING):
           # for key, value in self.MAPPING.items():
                if re.findall(regex, value):
                    findMissing.missing[key] = value
                    done = True

            return done

        def mappingReplacer(x):
            return '+'.join(list(x.group(1)))

        def valueReplacer(x):
            x = x.group()
            return x if x in findMissing.missing else self.MAPPING[x]

        for key in self.MAPPING:
            self.MAPPING[key] = re.sub(r'\"([^\"]+)\"', mappingReplacer,
                                       self.MAPPING[key], flags=re.I)

        while findMissing():
            for key in findMissing.missing:
                value = self.MAPPING[key]
                value = re.sub(regex, valueReplacer, value)

                self.MAPPING[key] = value
                findMissing.missing[key] = value


