# unicorn-fy Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

[Discussions about unicorn-fy releases!](https://github.com/oliver-zehentleitner/unicorn-fy/discussions/categories/releases)

[How to upgrade to the latest version!](https://oliver-zehentleitner.github.io/unicorn-fyreadme.html#installation-and-upgrade)

## 0.16.1.dev (development stage/unreleased/unstable)

## 0.16.1
### Added
- build_wheels.yml:  
  CIBW_ARCHS_LINUX: "x86_64 aarch64"
  CIBW_ARCHS_MACOS: "x86_64 arm64 universal2"
  CIBW_ARCHS_WINDOWS: "AMD64"
  CIBW_MUSLLINUX_X86_64_IMAGE: "musllinux_1_1"

## 0.16.0
### Added
- Python 3.13 support

## 0.15.0
### Added
- `__version__` and made use of it.
### Changed
- Moved from https://github.com/LUCIT-Systems-and-Development/ to https://github.com/oliver-zehentleitner
### Removed
- `binance_je_websocket()` 
- `jex_com_websocket()`

## 0.14.2
### Added
- Since Unicorn-Fy is delivered as a compiled C extension, IDEs such as Pycharm and Visual Code cannot use information 
  about available methods, parameters and their types for autocomplete and other intellisense functions. As a solution, 
  from now on stub files (PYI) will be created in the build process and attached to the packages. The IDEs can 
  automatically obtain the required information from these.

## 0.14.1
`unicorn-fy` can now also be installed on all architectures on which there are no precompiled packages from LUCIT. PIP 
now automatically recognises whether there is a suitable precompiled package and if not, the source is automatically 
compiled on the target system during the installation process with Cython. Even if you don't have to do anything 
special, please note that this process takes some time!

## 0.14.0
### Added
- Wheels for arm64 (Raspberry Pi)
- PR "futures account update: handle multi_assets_mode update" https://github.com/oliver-zehentleitner/unicorn-fy/pull/38
- PR "Updated All Futures Market Streams, Implemented Proper Coin-Futures Handling" https://github.com/oliver-zehentleitner/unicorn-fy/pull/39  

## 0.13.1
- Building conda packages and distribute them via https://anaconda.org/lucit

## 0.13.0
### Added 
- `debug` parameter to `UnicornFy()`
- Cython and PyPy Wheels support

## 0.12.2
Codebase equal to 0.12.0, testing azure pipe

## 0.12.1
Codebase equal to 0.12.0, just preparing conda-forge packaging

## 0.12.0
### Fixed
- `is_update_availabe()` typo to `is_update_available()`

## 0.11.1
### Changed
- Moved from https://github.com/oliver-zehentleitner to https://github.com/LUCIT-Systems-and-Development/
- Correctly scope loggers so that it plays nicely with others, logger name is "unicorn_fy".
### Fixed
- `binance_futures_websocket()` did not convert bids of depth streams ([issue#232](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/issues/232))

## 0.11.0
### Adding 
- Implement missing ACCOUNT_UPDATE (binance futures) event (Thx @folktale42
[PR#28](https://github.com/oliver-zehentleitner/unicorn-fy/pull/28))
- Support for Perpetual Coin Futures `binance_com_coin_futures_websocket()` - NOT READY!!!)

## 0.10.0
### Added
- Support for `ORDER_TRADE_UPDATE`, `ACCOUNT_CONFIG_UPDATE`, `MARGIN_CALL`
 and `ACCOUNT_UPDATE` in `binance_futures_websocket()` (Thx @StarBalll
[PR#23](https://github.com/oliver-zehentleitner/unicorn-fy/pull/23) and 
[PR#25](https://github.com/oliver-zehentleitner/unicorn-fy/pull/25)
- unittests for `ORDER_TRADE_UPDATE`, `ACCOUNT_CONFIG_UPDATE`
 and `ACCOUNT_UPDATE` in `binance_futures_websocket()`

## 0.9.0
### Added
- Support for `balanceUpdate` in `binance_websocket()` and `binance_futures_websocket()`
[PR#19 thx @davivc](https://github.com/oliver-zehentleitner/unicorn-fy/pull/21)

## 0.8.0
### Added
- TRBinance.com

## 0.7.0
### Added
- Support for `listStatus` in `binance_websocket()` 
[issue#19](https://github.com/oliver-zehentleitner/unicorn-fy/issues/19)

## 0.6.0
### Added
- Binance-com-margin
- Binance-com-isolated_margin
- Jex.com

## 0.5.0
### Added
- `outboundAccountPosition` [issue#11](https://github.com/oliver-zehentleitner/unicorn-fy/issues/11) - thanks to 
@bmschwartz
- handling for results
### Fixed
- `ModuleNotFoundError: No module named 'unicorn_fy.unicorn_fy'; 'unicorn_fy' is not a package` 
[PR#10](https://github.com/oliver-zehentleitner/unicorn-fy/pull/10), 
[issue#9](https://github.com/oliver-zehentleitner/unicorn-fy/issues/9)
- thanks to @uggel

## 0.4.1
### Added
- `account_permissions` in `outboundAccountInfo`

## 0.4.0
### Fixed
- all kind of tickers
- result msg handling
- error msg handling
### Removed
- Exception handling to show python error trace

## 0.3.5
### Fixed
- `!miniTicker@arr` structure

## 0.3.4
### Fixed
- `!miniTicker@arr` structure

## 0.3.3
### Added
- TypeError exception

## 0.3.2
### Changed
- ujson instead of stock json
- exception handling
### Added
- binance.com-futures (copy of binance_websocket() with suggested modification of 
[issue #1](https://github.com/oliver-zehentleitner/unicorn-fy/issues/1))

## 0.3.1
### Changes
- Moved docs to github pages

## 0.3.0
### Adding
- binance_us_websocket()
### Changes
- exchange name to return dict

## 0.2.0
### Adding
- binance_com_websocket()
- binance_je_websocket()
- is_update_availabe()
- get_latest_version()
- get_version()
- get_latest_release_info()

### Depricated
- binance_websocket()

## 0.1.1
### Fixed
- create pypi package

## 0.1.0 
- Released
