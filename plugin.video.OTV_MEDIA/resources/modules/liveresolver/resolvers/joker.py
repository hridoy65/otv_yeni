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
import json
from resources.lib.modules.log_utils import log
from resources.lib.modules.constants import USER_AGENT

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
		False
	def resolve(self, url, html = '', referer=None):
		#try:
			r = self.s.get(url).text
			
			fid = re.findall('id\s*=\s*[\"\']([^\"\']+).+?jokersplayer.+?\.js', r)[0]
			u = 'http://www.jokersplayer.xyz/embed.php?u=' + fid
			import resolvers
			return resolvers.resolve(u, referer=url)
		#except:
	#		return None
		
		
#ro = Resolver()
#print(ro.resolve('http://live.jokerswidget.com/freelivematch/8600731461373460.html'))
