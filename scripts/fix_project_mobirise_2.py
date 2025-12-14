import re
from pathlib import Path
p = Path(r"e:\babakmodarresi.github.io\project.mobirise")
s = p.read_text(encoding='utf-8')
# remove any occurrence where showButtons has checked (with optional whitespace and optional >)
s_new = re.sub(r'name=\\"showButtons\\"\s*checked', 'name=\\"showButtons\\"', s)
# Also handle single quotes
s_new = re.sub(r"name='showButtons'\s*checked", "name='showButtons'", s_new)
# ensure we didn't accidentally change too much
if s_new == s:
    print('no change')
else:
    p.write_text(s_new, encoding='utf-8')
    print('updated')
