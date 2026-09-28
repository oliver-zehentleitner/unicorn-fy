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
**See:** adapters.md#shape-mismatches-dont-fail-the-normalizer-does-what-it-can-and-errors-belong-on-the-result — 79b64d5f-c693-4a82-9928-a8182c609124 — as of 2026-09-28

Previously, only explicitly-listed event types were unwrapped/normalized; anything else fell through and crashed with `KeyError: 'data'`. Replaced with a catch-all: any payload with a top-level `e` key and no `data` wrapper (e.g. `listenKeyExpired`) is now wrapped, instead of relying on an enumerated list of known event types.

**Rejected alternative:** keep extending the explicit whitelist every time Binance adds a new event type.

**Reason:** the whitelist approach means the library breaks on every new Binance event type until someone notices and adds it — the catch-all tolerates unknown-but-well-shaped events instead of crashing on them. This explains the number of bare `except KeyError: pass` blocks throughout `unicorn_fy.py` — see the next entry for how this pattern sits against the suite's fail-loud convention.

## Shape mismatches don't fail: the normalizer does what it can, and errors belong on the result

**Id:** 79b64d5f-c693-4a82-9928-a8182c609124
**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** maintainer, 2026-09-28; the 29 `except KeyError` handlers in `unicorn_fy.py`; commit `31d7fa1`
**See:** adapters.md#catch-all-replacing-an-event-type-whitelist — 86f7088c-eb13-45cd-90b8-73a365d4822a — as of 2026-09-28
**See:** https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster — e325b6fb-117a-4f10-aa63-6d070b01188a — as of 2026-09-28
**Revisit when:** the unicorn-fy rewrite lands

unicorn-fy does not fail on a payload whose shape it doesn't fully know: it normalizes what it recognizes and passes the rest through. The `except KeyError` handlers in `unicorn_fy.py` — a missing `stream` key on a non-combined stream or a subscription reply, a field an event type doesn't carry — are that rule in code.

**Reason:** the maintainer's rule: the normalizer must not fail, it does what it can. It is the same logic as the catch-all that replaced the event-type whitelist (`See` above): a new or varying shape from Binance is expected, not a broken invariant. This is where unicorn-fy stands apart from the suite's fail-loud cases, like the cluster's `#6000` for an out-of-sync order book: there the data would be wrong; here it is only shaped differently.

**Rejected alternative:** raising on a missing key, fail-loud style. Rejected by that rule — the caller would lose the whole message over a field the normalizer only wanted to enrich.

**Open part:** the errors are to be attached to the result, so a caller can see what could not be normalized — today the handlers `pass` and the error is dropped silently. The planned rewrite of unicorn-fy is where that changes.

## Init value `False` → `{}`

**Id:** 35a07689-77e0-4f96-bf06-b630e424f152
**Type:** incident
**Status:** active
**Evidence:** confirmed
**Source:** commit `f8d6341`, fixes #44

`unicorn_fied_data` was initialized to `False`; an unmatched event type left it as `False`, and the next step (item assignment) crashed with `TypeError: bool object does not support item assignment`. Changed the default to `{}`.
