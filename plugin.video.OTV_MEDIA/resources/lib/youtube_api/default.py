# -*- coding: utf-8 -*-
#from resources.sites.LIVETV2 import *





from resources.lib.youtube_api.kodion import runner
from resources.lib.youtube_api import youtube

__provider__ = youtube.Provider()
runner.run(__provider__)

from resources.lib.youtube_api.kodion import service
service.run()


