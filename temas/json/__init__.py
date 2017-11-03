# -*- coding: latin-1 -*-
import json


def dumps(objeto, **kwargs):
    encoding = kwargs.pop('encoding', None)
    v = json.dumps(objeto, **kwargs)
    if encoding is not None and isinstance(v, str):
        v = v.encode(encoding)
    return v