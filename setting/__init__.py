# -*- coding: utf-8 -*-
"""
@file: __init__.py.py
@time: 2021/6/22
@desc:
"""

from fake_headers import Headers

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()
