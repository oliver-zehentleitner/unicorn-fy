#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev/test_one_stream.py
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
import logging
import os
import time
import threading

# https://docs.python.org/3/library/logging.html#logging-levels
logging.getLogger("unicorn_fy")
logging.basicConfig(level=logging.INFO,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is not False:
            unicorn_fied_data = UnicornFy.binance_com_websocket(oldest_stream_data_from_stream_buffer)
            print("===================================================================================================")
            print(str(oldest_stream_data_from_stream_buffer))
            print("===================================================================================================")
            print(str(unicorn_fied_data))
            print("===================================================================================================")
        else:
            time.sleep(0.01)


# To use this library you need a valid UNICORN Binance Suite License:
# https://technopathy.club/-87b0088124a8
ubwa = BinanceWebSocketApiManager()

worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(ubwa,))
worker_thread.start()

#channels = {'aggTrade', 'trade', 'kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_2h', 'kline_4h',
#            'kline_6h', 'kline_8h', 'kline_12h', 'kline_1d', 'kline_3d', 'kline_1w', 'kline_1M', 'miniTicker',
#            'ticker', 'bookTicker', 'depth5', 'depth10', 'depth20', 'depth', 'depth@100ms'}
#arr_channels = {'!miniTicker', '!ticker', '!bookTicker'}

stream_id = ubwa.create_stream('ticker', ['btcusdt', 'bnbbtc', 'ethbtc'])
time.sleep(10)
ubwa.print_stream_info(stream_id)
ubwa.get_stream_subscriptions(stream_id)
time.sleep(10)
ubwa.stop_manager()

