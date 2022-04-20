# -*- coding: utf-8 -*-
"""

    Copyright (C) 2014-2016 bromix (plugin.video.youtube)
    Copyright (C) 2016-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""
def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

from .directory_item import DirectoryItem
from .. import constants


class SearchHistoryItem(DirectoryItem):
    def __init__(self, context, query, image=None, fanart=None, location=False):
        if image is None:
            image = context.create_resource_path('media/search.png')

        params = {'q': query}
        if location:
            params['location'] = location

        DirectoryItem.__init__(self, query, context.create_uri([constants.paths.SEARCH, 'query'], params=params), image=image)
        if fanart:
            self.set_fanart(fanart)
        else:
            self.set_fanart(context.get_fanart())

        context_menu = [(context.localize(constants.localize.SEARCH_REMOVE),
                         'RunPlugin(%s)' % context.create_uri([constants.paths.SEARCH, 'remove'], params={'q': query})),
                        (context.localize(constants.localize.SEARCH_RENAME),
                         'RunPlugin(%s)' % context.create_uri([constants.paths.SEARCH, 'rename'], params={'q': query})),
                        (context.localize(constants.localize.SEARCH_CLEAR),
                         'RunPlugin(%s)' % context.create_uri([constants.paths.SEARCH, 'clear']))]
        self.set_context_menu(context_menu)
