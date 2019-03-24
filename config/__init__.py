#!/usr/bin/env python3

import os

def Config():

    env = os.environ.get('APP_MODE', 'dev')

    if env == 'dev':
        from .Develop import Develop
        return Develop()
    elif env == 'prd':
        from .Product import Product
        return Product()
    else:
        from .Default import Default
        return Default()


