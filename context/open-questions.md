# Open questions

## Bare `except KeyError: pass` blocks vs. the suite's fail-loud convention

**Type:** undefined — open question awaiting maintainer input, not yet classifiable as decision/workaround/incident/constraint
**Status:** unknown — needs maintainer input

`unicorn_fy.py` has dozens of bare `except KeyError: pass` blocks (e.g. around lines 214, 224, 252, 259, 273...) that silently tolerate schema mismatches rather than raising. Commit `31d7fa1` (see `adapters.md`) shows this is a deliberate pattern for tolerating varying/unknown event shapes from Binance, not an oversight.

**Why this needs an answer:** the rest of the suite documents a "fail loud on broken invariants, never silently continue" convention (see the sibling `unicorn-binance-depth-cache-cluster`'s `context/fail-loud.md` for a concrete example). Whether this repo's catch-all-and-swallow pattern is considered a deliberate, scoped exception to that convention (tolerating *shape* variance in an adapter layer, as opposed to *data-integrity* violations like an out-of-sync order book) or something worth tightening isn't stated anywhere. Worth asking directly rather than assuming either way.
