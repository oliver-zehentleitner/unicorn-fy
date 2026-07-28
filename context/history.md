# History

## Three-org lineage

**Status:** superseded — repo now lives under `oliver-zehentleitner`, MIT-licensed
**Evidence:** confirmed
**Source:** git history

The repo's earliest commits (from 2019-04, e.g. `562af8e`) reference `github.com/unicorn-data-analysis/unicorn-binance-websocket-api` and an `@unicorn-data.com` author email — a pre-LUCIT identity, not a LUCIT-first origin like the framing used elsewhere might suggest. It moved to the `LUCIT-Systems-and-Development` org in 2022 (commits `e5b82fc`, `b207c7a`, both 2022-01-03), briefly switched to a proprietary `LSOSL` license in 2023-11 (commit `1c78b1f`) — reverted back to MIT roughly 2.5 weeks later (`2310d9b`/`9ee5aae`) — and finally de-branded to `oliver-zehentleitner` in 2025-06. Residual cleanup (conda-forge migration, `build_conda.yml` removal, remaining org-URL references) continued into April 2026 (`11ef2c3`, `4212c7c`).

**Reason:** LUCIT is no longer part of how this project is licensed, distributed, or supported. The LSOSL license switch itself appears to have been a short-lived experiment reverted quickly, not a lasting decision.

**Confirmed: this repo was split out of `unicorn-binance-websocket-api`.** This repo's own initial commit (`562af8e`, 2019-04-04) is a fresh, empty repo (just `LICENSE`/`README.md`/`.gitignore`) — but its next few commits (e.g. `ea33d69`) already reference issue URLs under `github.com/unicorn-data-analysis/unicorn-binance-websocket-api`, i.e. the combined project this code originally lived in. The split itself is documented in the *other* repo's history: `unicorn-binance-websocket-api` commit `04868179` (2019-04-30): "unicorn_fy bug, splitting unicorn_fy and websocket into 2 projects." So the normalization logic and the WebSocket client were one project for the first few weeks, then split into today's two repos.

## `orjson` as the suite-wide JSON standard

**Status:** active
**Evidence:** confirmed
**Source:** commit `637911a`

`orjson` replaced `ujson` here, framed explicitly as a suite-wide standardization, not a per-repo preference. The same commit also fixed an unrelated bug: `binance_websocket()` had `unicorn_fied` containing a method reference instead of the actual version string.

**Reason:** consistency across the suite's modules (see the parallel `ujson`→stdlib/`orjson` cleanups in the sibling REST-API and WebSocket-API repos) rather than a reason specific to this repo.
