# -*- coding: utf-8 -*-
# Credits to:
#                    _                                     
#                   ( )_  _                                
#   _ _  _ __       | ,_)(_)   ___       _ _  _ _      __  
# /'_` )( '__)(`\/')| |  | | /'___)    /'_` )( '_`\  /'__`\
#( (_| || |    >  < | |_ | |( (___  _ ( (_| || (_) )(  ___/
#`\__,_)(_)   (_/\_)`\__)(_)`\____)(_)`\__,_)| ,__/'`\____)
#                                            | |           
#                                            (_)           
#

import re
import requests
from resources.modules import cache

try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse  # Python 2

HOSTS_URL = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
try:
	from urllib.parse import urlparse, quote_plus, urlencode
except:
	from urlparse import urlparse
	from urllib import quote_plus, urlencode

def getit():
	return requests.get(HOSTS_URL).text

def isAd(host):
	hst = cache.get(getit, 2880)
	h = urlparse(host).netloc
	return (h in hst)