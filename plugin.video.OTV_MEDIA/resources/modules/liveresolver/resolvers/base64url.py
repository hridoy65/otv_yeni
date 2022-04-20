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
import base64
from resources.modules.log_utils import log
from resources.modules.constants import USER_AGENT


try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse  # Python 2


class Resolver():

	def __init__(self):
		self.hosts = {}
		self.headers = {'User-Agent': USER_AGENT, 'Cache-control': 'no-cache'}
		self.s = requests.session()
		self.s.headers.update(self.headers)

	def isSupported(self, url, html):
		return bool(re.search('atob\([\"\']', html)) and not 'wigistream' in url

	def resolve(self, url, html='', referer=None):
		
		#try:
		r = html
		#r = self.s.get(url).text
		s = re.findall('atob\([\"\']([^\"\']+)', r)[0]
		s = base64.b64decode(s).decode('utf-8')
		if 'm3u8' in s:
			return {'url': s, 'headers': {'referer': url}}
		return None
		#except:
		#	return None

