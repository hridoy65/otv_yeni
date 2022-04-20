# -*- coding: utf-8 -*-
"""

    Copyright (C) 2018-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""
def get_key(x):
	p = 3
	while True:
		if p > len(x):
			break
		pl = len(str(p))
		x = x[:p] + x[p + pl:]
		p += 12 - pl
	x = x.replace('w_OizD', 'a')
	x = x.replace('Xhi_Lo', 'A')
	return x
             

API_KEY = get_key('Xhi3_LoIzw_OizD15SyCNReMvKL27nw_OizDWRR395T5uGWpvn451I2VYc78Gy463')
CLIENT_ID = get_key('4113447027255-v15bgs05u1o3m278mpjs2vcd0394w_OizDfrg5160drbw_Oiz63D.w_OizDpp75s.googleus87ercontent.99com')
CLIENT_SECRET = get_key('Zf93pqd2rxgY2ro159rK20BMxif27')

from . import JSONStore


class APIKeyStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'api_keys.json')

    def set_defaults(self):
        data = self.get_data()
        if 'keys' not in data:
            data = {'keys': {'personal': {'api_key': API_KEY, 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}, 'developer': {}}}
        if 'personal' not in data['keys']:
            data['keys']['personal'] = {'api_key': API_KEY, 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
        if 'developer' not in data['keys']:
            data['keys']['developer'] = {}
        self.save(data)
