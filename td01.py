#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import sys
import binascii
from future_builtins import hex
import logging
import socket
from decimal import Decimal
import traceback
import ctypes
import ConfigParser
import os
import erppeek
from unidecode import unidecode


_LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}


#LOG_LEVEL à extraire depuis config
LOG_LEVEL = 'info'
logging.basicConfig()
__logger = logging.getLogger('python_td01')
# hdlr = logging.FileHandler("./python_td01.log")
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# __logger.addHandler(hdlr)
try:
    level = _LEVELS.get(LOG_LEVEL)
except Exception:
    print u"Niveau de log incorrect. Choisir parmi : debug, info, warning, error, critical"
    sys.exit()
__logger.setLevel(level)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.errorhandler(404)  # Surchage de la 404
def ma_page_404(error):
    __logger.warning('Erreur URL : %s' % error)
    reponse = make_response("Erreur 404", 404)
    return reponse



@cross_origin()
# @app.route('/api/push_host_infos/<infos>', methods=['GET', 'POST'])
# def push_host_infos(infos):
@app.route('/api/push_host_infos/', methods=['GET', 'POST'])
def push_host_infos():
    try:
        data = request.data
        __logger.info('Informations reçues : %s' % data)
        result = 'OK'
    except Exception:
        return jsonify('Error\n%s' % traceback.format_exc())
    return jsonify(result)

if __name__ == '__main__':
    reload(sys)
    if hasattr(sys, "setdefaultencoding"):
        sys.setdefaultencoding("utf-8")
    __logger.info('Application en écoute, avec niveau de log %s' % level)
    print "Application en écoute sur port 8517"
    app.run(host="0.0.0.0", port=int("8517"))