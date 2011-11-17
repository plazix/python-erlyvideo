# -*- coding: utf-8 -*-

from hashlib import sha1
import base64
import hmac
import simplejson

from api import ErlyvideoApi
from exceptions import EventUnsupportException, APIErrorException
from models import ErlyvideoStats, ErlyvideoOptions, ErlyvideoEvent


__all__ = ['ErlyvideoApi', 'EventUnsupportException', 'APIErrorException', 'ErlyvideoStats', 
            'ErlyvideoOptions', 'ErlyvideoEvent', 'erlyvideo_session_string']


def erlyvideo_session_string(user_id, additional_data={}):
    """
    Формирует строку с данными сессии для erlyvideo

    :param user_id: ID пользователя
    :param additional_data: дополнительные данные, которые необходимо передать erlyvideo
    :return: строка с данными сессии
    """
    session = {'user_id': user_id}
    session.update(additional_data)
    session_base64 = base64.b64encode(simplejson.dumps(session))
    session_signature = hmac.new(ERLYVIDEO_SECRET_KEY, session_base64, digestmod=sha1).hexdigest()
    return '%s--%s' % (session_base64, session_signature)
