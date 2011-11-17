# -*- coding: utf-8 -*-

import simplejson
from urllib2 import build_opener, HTTPBasicAuthHandler

from exceptions import APIErrorException

# todo добавить поддержку коммерческой версии

class ErlyvideoApi(object):
    API_STREAMS_URI = '/erlyvideo/api/streams/'
    API_STREAM_URI = '/erlyvideo/api/stream/%s/'
    API_STREAM_HEALTH_URI = '/erlyvideo/api/stream_health/%s/' # true, {"error":"unknown"}

    __opener = None

    def __init__(self, host, port=8082, user='', password=''):
        if user and password:
            auth = HTTPBasicAuthHandler()
            auth.add_password('Django', '%s:%s' % (host, port), user, password)
            self.__opener(auth)
        else:
            self.__opener = build_opener()

    def __request(self, url):
    	# todo добавить проверки
        data = self.__opener(url)
        data = simplejson.loads(''.join(data))

        if 'error' in data:
        	raise APIErrorException(data['error'])
        return data

    def get_filelist(self):
        # todo написать
        pass

    def get_streams(self):
        data = self.__request(self.API_STREAMS_URI)
        return data['streams']

    def get_stream_health(self, name):
        # todo написать
        pass

    def get_stream(self, name):
        data = self.__request(self.API_STREAM_URI % name)
        return data['stream']

    def get_licenses(self):
        # todo написать
        pass
