# -*- coding: utf-8 -*-

import simplejson
from urllib2 import build_opener, HTTPBasicAuthHandler

from exceptions import APIErrorException

# todo добавить поддержку коммерческой версии


__docformat__ = "restructuredtext"


class FreeErlyvideoApi(object):
    API_STREAMS_URI = '/erlyvideo/api/streams/'
    API_STREAM_URI = '/erlyvideo/api/stream/%s/'
    API_STREAM_HEALTH_URI = '/erlyvideo/api/stream_health/%s/'

    __opener = None

    def __init__(self, host, port=8082, user='', password=''):
        if user and password:
            auth = HTTPBasicAuthHandler()
            auth.add_password('Django', '%s:%s' % (host, port), user, password)
            self.__opener(auth)
        else:
            self.__opener = build_opener()

    def __request(self, url):
        """
        Запрос к серверу erlyvideo.

        Возвращает распарсенный ответ сервера erlyvideo.

        В случае ошибки обращение к серверу или если сервер возвращает ошибку, то бросается исключение APIErrorException
        с информацией об ошибке.

        :param url: сслыка на метод api
        :return:
        """
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
        """
        Информация о потоках
        """
        data = self.__request(self.API_STREAMS_URI)
        return data['streams']

    def get_stream_health(self, name):
        """
        :param name: имя потока
        :return:
        """
        return self.__request(self.API_STREAM_URI % name)

    def get_stream(self, name):
        """
        Информация о потоке.

        :param name: имя потока
        """
        data = self.__request(self.API_STREAM_URI % name)
        return data['stream']

    def get_licenses(self):
        # todo написать
        pass


class CommercialErlyvideoApi(FreeErlyvideoApi):
    # todo написать
    pass
