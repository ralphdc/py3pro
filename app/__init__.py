#!/usr/bin/env python3

from .Download import Download

class GetHandler():

    _ITEM_ = {
        'download': Download
    }


    @classmethod
    def get_unit(cls, unit, **kwargs):
        if unit in cls._ITEM_:
            return cls._ITEM_.get(unit)(**kwargs)
        else:
            raise Exception("[Error] - GetHandler get unit error, unit not found...")

