#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev/test_conversion.py
#
# Part of ‘UnicornFy’
# Project website: https://github.com/oliver-zehentleitner/unicorn-fy
# Github: https://github.com/oliver-zehentleitner/unicorn-fy
# Documentation: https://oliver-zehentleitner.github.io/unicorn-fy
# PyPI: https://pypi.org/project/unicorn-fy
#
# License: MIT
# https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/LICENSE
#
# Author: Oliver Zehentleitner
#
# Copyright (c) 2019-2025, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from unicorn_fy.unicorn_fy import UnicornFy

data = '{"e":"ACCOUNT_UPDATE","T":1617859763506,"E":1617859763511,"a":{"B":[{"a":"USDT","wb":"1790.86605837","cw":"1790.86605837"}],"P":[{"s":"CHZUSDT","pa":"0","ep":"0.00000","cr":"0","up":"0","mt":"cross","iw":"0","ps":"BOTH","ma":"USDT"},{"s":"CHZUSDT","pa":"2684","ep":"0.45855","cr":"79.89127995","up":"2.03986684","mt":"cross","iw":"0","ps":"LONG","ma":"USDT"}],"m":"ORDER"}}'

result = UnicornFy.binance_futures_websocket(data)
print(f"result: {result}")
