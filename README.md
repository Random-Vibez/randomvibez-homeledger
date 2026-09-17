# HomeLedger

HomeLedger is a browser-local recurring home-maintenance ledger. Record what was last completed, see overdue/upcoming work, and mark a job complete to calculate its next review date.

It has no backend, account, uploads, analytics, runtime network calls, or reminders. Data stays in this browser; exports and printouts are not encrypted. Do not enter passwords, access codes, alarm codes, financial details, or other secrets. This is a planning aid, not safety, warranty, legal, or manufacturer advice.

## Verification

Run `node --check app.js`, `python3 -m pytest -q public/homeledger/tests/test_static.py`, and a local HTTP smoke test. The public host policy is in `.htaccess`.
