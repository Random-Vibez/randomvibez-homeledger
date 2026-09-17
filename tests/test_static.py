from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_static_contract():
    html=(ROOT/'index.html').read_text(); js=(ROOT/'app.js').read_text(); css=(ROOT/'styles.css').read_text(); policy=(ROOT/'.htaccess').read_text()
    for marker in ['localStorage','Export JSON','Import JSON','no secrets','cookie-banner.js','Mark complete today','lastDone']:
        assert marker in html or marker in js
    for bad in ['fetch(','XMLHttpRequest','innerHTML','document.write','eval(','WebSocket']:
        assert bad not in js
    for marker in ['MAX_ITEMS=40','MAX_STATE',"connect-src 'none'",'frame-ancestors','prefers-reduced-motion','@media print']:
        assert marker in js+css+policy
    for name in ['cookie-banner.js','cookie-banner.css','favicon.svg','LICENSE','SECURITY.md','README.md']:
        assert (ROOT/name).is_file()
def test_calendar_and_import_contract():
    js=(ROOT/'app.js').read_text()
    assert 'addMonths' in js and 'Existing data is unchanged' in js and 'x.items.length<=MAX_ITEMS' in js
if __name__=='__main__':
    test_static_contract();test_calendar_and_import_contract();print('static contract: PASS')
