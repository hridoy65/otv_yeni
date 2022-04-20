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


class NextPageItem(DirectoryItem):
    def __init__(self, context, current_page=1, image=None, fanart=None):
        new_params = {}
        new_params.update(context.get_params())
        new_params['page'] = str(current_page + 1)
        name = context.localize(constants.localize.NEXT_PAGE, 'Next Page')
        if name.find('%d') != -1:
            name %= current_page + 1

        DirectoryItem.__init__(self, name, context.create_uri(context.get_path(), new_params), image=image)
        if fanart:
            self.set_fanart(fanart)
        else:
            self.set_fanart(context.get_fanart())

        self.next_page = True
