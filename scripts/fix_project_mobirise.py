import io
import sys
from pathlib import Path
p = Path(r"e:\babakmodarresi.github.io\project.mobirise")
text = p.read_text(encoding='utf-8')
# remove Useless Button label and the trailing <br>
text = text.replace('Useless Button<br>', '')
# remove checked on showButtons inputs (both with and without escaped quotes)
text = text.replace('name="showButtons" checked', 'name="showButtons"')
text = text.replace("name='showButtons' checked", "name='showButtons'")
# Also remove any stray anchor that became empty like >\n                </div>\n            </div> - keep structure
p.write_text(text, encoding='utf-8')
print('done')
