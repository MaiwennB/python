#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
import os
import socket
import json

class Psutil():
    def __init__(self):
        self.data = []

    def _get_process_if(self):
        None

    def getInfo(self):
        Info = {}

        Info['nomHost'] = socket.gethostname()

        disk = psutil.disk_usage('/')
        Info['disk'] = json.dumps(disk)

        Info['OS'] = os.name

        cpu_stats = psutil.cpu_stats()
        Info['CPU_STAT'] = json.dump(cpu_stats)

        return Info

    def publish():
        None

if __name__ == '__main__':
    self = Psutil()
    self.getInfo()