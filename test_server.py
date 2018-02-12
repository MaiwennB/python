#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

"""
Application de tests
"""


if __name__ == '__main__':  # Script executed directly?
    r = requests.post('http://localhost:8517/api/push_host_infos/', json={'key1': 'value1', 'key2': 'value2'})
    print "Status : ", r.status_code
    print r.json()