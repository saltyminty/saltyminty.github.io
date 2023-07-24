#!/usr/bin/env python3
"""Check a built portfolio for missing local links, images, scripts and CSS assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urljoin, unquote
import re
import sys

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src', 'poster'):
            if attrs.get(key):
                self.urls.append(attrs[key])
        if attrs.get('srcset') and not attrs['srcset'].startswith('data:'):
            self.urls.extend(part.strip().split()[0] for part in attrs['srcset'].split(',') if part.strip())

def check(root):
    root = root.resolve()
    errors = set()
    checked = 0
    html_files = sorted(root.rglob('*.html'))
    for source in html_files + sorted(root.rglob('*.css')):
        text = source.read_text(errors='replace')
        if source.suffix == '.html':
            parser = References()
            parser.feed(text)
            urls = parser.urls
            if 'No CV data found' in text or 'CV rendering is unavailable' in text:
                errors.add((str(source.relative_to(root)), 'CV did not render'))
        else:
            urls = [m.strip().strip('\'"') for m in re.findall(r'url\(([^)]+)\)', text)]
        base = '/' + str(source.relative_to(root))
        for url in urls:
            if not url or url.startswith(('#', '//')) or urlsplit(url).scheme:
                continue
            target_url = urlsplit(urljoin(base, url)).path
            target = root / unquote(target_url).lstrip('/')
            checked += 1
            if not (target.is_file() or target.is_dir() and (target / 'index.html').is_file()):
                errors.add((str(source.relative_to(root)), url))
    for source, url in sorted(errors):
        print(f'{source}: missing {url}')
    print(f'Checked {len(html_files)} HTML pages and {checked} local references; {len(errors)} errors.')
    return int(bool(errors))

if __name__ == '__main__':
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_dir():
        raise SystemExit('Usage: python3 bin/check_site.py PATH_TO_BUILT_SITE')
    raise SystemExit(check(Path(sys.argv[1])))
