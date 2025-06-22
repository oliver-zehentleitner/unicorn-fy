[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-fy.svg?label=github&color=blue)](https://github.com/oliver-zehentleitner/unicorn-fy/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/oliver-zehentleitner/unicorn-fy/total?color=blue)](https://github.com/oliver-zehentleitner/unicorn-fy/releases)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-fy?color=blue)](https://pypi.org/project/unicorn-fy/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-fy)](https://pepy.tech/project/unicorn-fy)
[![License](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-fy.svg?color=blue)](https://oliver-zehentleitner.github.io/unicorn-fylicense.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/issues)
[![codecov](https://codecov.io/gh/oliver-zehentleitner/unicorn-fy/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/oliver-zehentleitner/unicorn-fy)
[![CodeQL](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/codeql-analysis.yml)
[![Unit Tests](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/build_wheels.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/unicorn-fy)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://technopathy.club)
[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/oliver-zehentleitner/unicorn-fy)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)

[![LUCIT-UNICORNFY-Banner](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/logo/LUCIT-UNICORNFY-Banner-Readme.png)](https://github.com/oliver-zehentleitner/unicorn-fy)

# UnicornFy
[Supported Exchanges](#supported-exchanges) | [Installation](#installation-and-upgrade) | [Change Log](#change-log) | [Documentation](#documentation) | 
[Examples](#examples) | [Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) 
| [Contributing](#contributing) | [Disclaimer](#disclaimer) 

A Python SDK to convert received raw data from crypto exchange API endpoints into well-formed python dictionaries.

Part of ['UNICORN Binance Suite'](https://github.com/oliver-zehentleitner/unicorn-binance-suite).

```
import unicorn_fy

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

ufy = unicorn_fy.UnicornFy()

unicorn_fied_stream_data = ufy.binance_com_websocket(received_stream_data_json)
print(unicorn_fied_stream_data)
```

Output:

```
{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1556876873656, 'symbol': 'BTCUSDT',
 'trade_id': 117727701, 'price': '5786.76000000', 'quantity': '0.03200500', 'buyer_order_id': 341831847,
 'seller_order_id': 341831876, 'trade_time': 1556876873648, 'is_market_maker': True, 'ignore': True,
 'unicorn_fied': ['binance', '0.16.0']}
```

This lib is integrated into 
[UNICORN Binance WebSocket API](https://www.lucit.tech/unicorn-binance-websocket-api.html) 
and can be activated by setting parameter 
[`output_default` of `BinanceWebSocketApiManager()` to `UnicornFy`](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output_default#module-unicorn_binance_websocket_api.manager) 
or for specific streams with the parameter 
[`output` of `create_stream()` to `UnicornFy`](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager.create_stream).

## Get the right [logger](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/examples/_archive/example_logging.py):
```
logging.getLogger("unicorn_fy")
```

## What are the benefits of UnicornFy
### Supported exchanges:

***Websockets***

| Exchange | Docs            | Status | 
| -------- | --------------- | ------ |
| [Binance](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Isolated Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Futures](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | STABLE |
| [Binance Futures Testnet](https://testnet.binancefuture.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_coin_futures_websocket) | STABLE |
| [Binance Coin Futures](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_coin_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_coin_futures_websocket) | NEEDS_YOUR_HELP |
| [Binance Coin Futures Testnet](https://testnet.binancefuture.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_coin_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | NEEDS_YOUR_HELP |
| [Binance US](https://www.binance.us) ([API](https://github.com/binance-us/binance-official-api-docs)) | [`binance_us_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_us_websocket) | STABLE |
| [Binance TR](https://www.trbinance.com) ([API](https://www.trbinance.com/apidocs)) | [`trbinance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.trbinance_com_websocket) | STABLE |
| [Binance DEX](https://www.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |
| [Binance DEX Testnet](https://testnet.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |

***REST***

None

- Available as a package via `pip` and `conda` as precompiled C extension with stub files for improved Intellisense 
  functions and source code for easier debugging of the source code. [To the installation.](#installation-and-upgrade)

- Excessively tested on Linux, Mac and Windows

If you like the project, please 
[![star](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/star.png)](https://github.com/oliver-zehentleitner/unicorn-fy/stargazers) it on 
[GitHub](https://github.com/oliver-zehentleitner/unicorn-fy)! 

## Installation and Upgrade
The module requires Python 3.8 and runs smoothly up to and including Python 3.13.

[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

For the PyPy interpreter we offer packages only from Python version 3.9 and higher.

The current dependencies are listed 
[here](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki/Installation).

### Packages are created automatically with GitHub Actions
When a new release is to be created, we start two GitHubActions: 

- [Build and Publish Anaconda](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)
- [Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/build_wheels.yml) 

Both start virtual Windows/Linux/Mac servers provided by GitHub in the cloud with preconfigured environments and 
create the respective compilations and stub files, pack them into wheels and conda packages and then publish them on 
GitHub, PYPI and Anaconda. This is a transparent method that makes it possible to trace the source code behind a 
compilation.

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static 
  typing and C-level performance. By compiling Python code into C, Cython Wheels can significantly enhance the 
  execution speed of Python code, especially in  computationally intensive tasks. This means faster runtimes and more 
  efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and 
  efficiency. It uses Just-In-Time (JIT) compilation, which can dramatically improve the performance of Python code. 
  Our PyPy Wheels are tailored for compatibility with PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

On Raspberry Pi and other architectures for which there are no pre-compiled versions, the package can still be 
installed with PIP. PIP then compiles the package locally on the target system during installation. Please be patient, 
this may take some time!

#### Installation
`pip install unicorn-fy`

#### Update
`pip install unicorn-fy --upgrade`

### A Conda Package of the latest version with `conda` from [Anaconda](https://anaconda.org/lucit)
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

The `unicorn-fy` package is also available as a Cython version for the `linux-64`, `osx-64` 
and `win-64` architectures with [Conda](https://docs.conda.io/en/latest/) through the 
[`lucit` channel](https://anaconda.org/lucit). 

For optimal compatibility and performance, it is recommended to source the necessary dependencies from the 
[`conda-forge` channel](https://anaconda.org/conda-forge). 

#### Installation
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

```
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-fy
```

#### Update
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

`conda update -c lucit unicorn-fy`

### From source of the latest release with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-fy)

#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-fy/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 0.16.0) you determined [here](https://github.com/oliver-zehentleitner/unicorn-fy/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/archive/0.16.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-fy)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-fy/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-fy/archive/master.zip)
 and use:
 
- ./environment.yml
- ./meta.yaml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-fy/changelog.html](https://oliver-zehentleitner.github.io/unicorn-fy/changelog.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-fy)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-fymodules.html)

## Examples
- [Look here!](https://github.com/oliver-zehentleitner/unicorn-fy/tree/master/examples/)

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-fy](https://github.com/oliver-zehentleitner/unicorn-fy)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-fy/wiki](https://github.com/oliver-zehentleitner/unicorn-fy/wiki)

## Social
- [Discussions](https://github.com/oliver-zehentleitner/unicorn-fy/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/watch.png)](https://github.com/oliver-zehentleitner/unicorn-fy/watchers) 
the repository on [GitHub](https://github.com/oliver-zehentleitner/unicorn-fy), write your 
[own script](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/examples/_archive/example_version_of_this_package.py) 
with using 
[`is_update_available()`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=is_update#unicorn_fy.unicorn_fy.UnicornFy.is_update_availabe) 
 or you use the 
[monitoring API service](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service).

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-fy/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-fy#installation-and-upgrade). 
If the issue still exists, provide the error trace, OS and python version and explain how to reproduce the error. 
A demo script is appreciated.

If you don't find an issue related to your topic, please open a new issue:
[https://github.com/oliver-zehentleitner/unicorn-fy/issues](https://github.com/oliver-zehentleitner/unicorn-fy/issues)

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-fy/security/policy)

## Contributing
[UnicornFy](https://github.com/oliver-zehentleitner/unicorn-fy)  is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-fy)](https://github.com/oliver-zehentleitner/unicorn-fy/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/heart.png) open source!

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.
