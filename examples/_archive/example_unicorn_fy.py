#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_unicorn_fy.py
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
# Copyright (c) 2019-2025, Oliver Zehentleitner (https://www.linkedin.com/in/oliver-zehentleitner/)
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

import json

# recevied data format from binance:
received_stream_data_json = {"stream": "btcusdt@trade",
                             "data": {"e": "trade",
                                      "E": 1556876873656,
                                      "s": "BTCUSDT",
                                      "t": 117727701,
                                      "p": "5786.76000000",
                                      "q": "0.03200500",
                                      "b": 341831847,
                                      "a": 341831876,
                                      "T": 1556876873648,
                                      "m": True,
                                      "M": True}}

received_stream_data_json = json.dumps(received_stream_data_json)

print("raw format:")
print(received_stream_data_json)

# unicorn_fy the format:
unicorn_fied_stream_data = UnicornFy.binance_com_websocket(received_stream_data_json)
print("unicorn_fied:")
print(unicorn_fied_stream_data)

# recevied data format from binance:
received_stream_data_json = {"stream": "ethbtc@ticker",
                             "data": {"e": "24hrTicker",
                                      "E": 1556877162244,
                                      "s": "ETHBTC",
                                      "p": "-0.00057000",
                                      "P": "-1.926",
                                      "w": "0.02918378",
                                      "x": "0.02959500",
                                      "c": "0.02902900",
                                      "Q": "0.51600000",
                                      "b": "0.02901600",
                                      "B": "0.47500000",
                                      "a": "0.02903000",
                                      "A": "5.48000000",
                                      "o": "0.02959900",
                                      "h": "0.02963400",
                                      "l": "0.02820900",
                                      "v": "222630.30500000",
                                      "q": "6497.19329404",
                                      "O": 1556790762240,
                                      "C": 1556877162240,
                                      "F": 119982523,
                                      "L": 120137417,
                                      "n": 154895}}

received_stream_data_json = json.dumps(received_stream_data_json)

print("raw format:")
print(received_stream_data_json)

# unicorn_fy the format:
unicorn_fied_stream_data = UnicornFy.binance_com_websocket(received_stream_data_json)
print("unicorn_fied:")
print(unicorn_fied_stream_data)


