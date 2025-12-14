from pathlib import Path
old = 'https://www.instagram.com/babakmodarresii/'
new = 'https://www.instagram.com/beelzee.bob/'
root = Path(r'e:\babakmodarresi.github.io')
count = 0
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in ('.html', '.mobirise') or p.name == 'project.mobirise' or p.suffix == '':
        # target .html and project.mobirise explicitly
        if p.suffix.lower() not in ('.html',) and p.name != 'project.mobirise':
            continue
        try:
            s = p.read_text(encoding='utf-8')
        except Exception:
            continue
        if old in s:
            s2 = s.replace(old, new)
            p.write_text(s2, encoding='utf-8')
            print(f'Updated {p}')
            count += s.count(old)
print('Total replacements occurrences:', count)
