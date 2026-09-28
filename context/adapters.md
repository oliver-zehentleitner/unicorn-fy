# Adapting to Binance's stream shape changes

## WS API userData envelope unwrap

**Id:** 67603c5a-14d0-4559-8709-34bcea467b02
**Type:** workaround
**Status:** active
**Evidence:** confirmed
**Source:** commit `1503d59`, merge `3b2e144`, 2026-04-10

Binance removed the REST listenKey endpoints for Spot/Margin in February 2026. UBWA switched to the WS API subscription flow instead, which wraps userData events in `{"subscriptionId": 0, "event": {...}}`. `binance_websocket()` now unwraps that envelope before handing the payload to the existing normalization pipeline.

**Reason:** this is a forced adaptation to an external Binance API change, not a design choice — the envelope shape is Binance's, not this library's.

## Catch-all replacing an event-type whitelist

**Id:** 86f7088c-eb13-45cd-90b8-73a365d4822a
**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** commit `31d7fa1`, fixes #41
**See:** open-questions.md#bare-except-keyerror-pass-blocks-vs-the-suites-fail-loud-convention — 79b64d5f-c693-4a82-9928-a8182c609124 — as of 2026-09-28

Previously, only explicitly-listed event types were unwrapped/normalized; anything else fell through and crashed with `KeyError: 'data'`. Replaced with a catch-all: any payload with a top-level `e` key and no `data` wrapper (e.g. `listenKeyExpired`) is now wrapped, instead of relying on an enumerated list of known event types.

**Rejected alternative:** keep extending the explicit whitelist every time Binance adds a new event type.

**Reason:** the whitelist approach means the library breaks on every new Binance event type until someone notices and adds it — the catch-all tolerates unknown-but-well-shaped events instead of crashing on them. This explains the number of bare `except KeyError: pass` blocks throughout `unicorn_fy.py` — see `open-questions.md` for how this pattern sits against the suite's fail-loud convention.

## Init value `False` → `{}`

**Id:** 35a07689-77e0-4f96-bf06-b630e424f152
**Type:** incident
**Status:** active
**Evidence:** confirmed
**Source:** commit `f8d6341`, fixes #44

`unicorn_fied_data` was initialized to `False`; an unmatched event type left it as `False`, and the next step (item assignment) crashed with `TypeError: bool object does not support item assignment`. Changed the default to `{}`.
