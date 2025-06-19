#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev/get_results.py
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

from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
from unicorn_fy.unicorn_fy import UnicornFy
import time
import logging
import os

logging.getLogger("unicorn_fy")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

# To use this library you need a valid UNICORN Binance Suite License:
# https://technopathy.club/-87b0088124a8
binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com")
stream_id = binance_websocket_api_manager.create_stream(['ticker'], ['btcusdt', 'bnbbtc', 'ethbtc'])
#binance_websocket_api_manager.create_stream(['miniTicker'], ['btcusdt', 'bnbbtc', 'ethbtc'])
#binance_websocket_api_manager.create_stream(['!miniTicker'], ['arr'])
#binance_websocket_api_manager.create_stream(['!ticker'], ['arr'])

time.sleep(10)
binance_websocket_api_manager.get_stream_subscriptions(stream_id)
time.sleep(5)
print(str(binance_websocket_api_manager.get_results_from_endpoints()))
time.sleep(5)

while True:
    oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
    if oldest_stream_data_from_stream_buffer:
        oldest_stream_data_from_stream_buffer = UnicornFy.binance_com_websocket(oldest_stream_data_from_stream_buffer)
        print(oldest_stream_data_from_stream_buffer)
