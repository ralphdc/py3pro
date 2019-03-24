#!/usr/bin/env python3

from config import Config
from Function import *


class Download():


    TARGET = 'http://www.zi-han.net/theme/hplus/'

    def __init__(self):
        pass


    def run(self):

        init_page = send_request_text('get', self.TARGET)

        print(init_page)


