import json
import requests

from cache import vocabulary_cache


HOST = "https://mastertables.athento.com/"


class MasterTablesClient:
    host = HOST
    api_key = "default"


    def __init__(self, api_key, host=HOST):
        self.api_key = api_key


    @vocabulary_cache
    def get_vocabulary(self, vocabulary, category=None):
        url = self.host
        url += "vocabularies/api/public_api/get_vocabulary/"
        querystring = {"api_key":self.api_key, "vocabulary": vocabulary}
        if category:
            querystring['category'] = category

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = json.loads(response.text)
        if res.has_key('vocabulary'):
            res = res['vocabulary']
        detail = res.get('detail', '')
        if detail == 'Authentication credentials were not provided.':
            raise AttributeError
        return res


    def get_vocabulary_reverse(self, vocabulary, category=None):
        res = self.get_vocabulary(vocabulary)
        res = dict((v,k) for k,v in res.iteritems())
        return res


    def get_values(self, vocabulary):
        res = self.get_vocabulary(vocabulary)
        res = res.keys()
        return res
