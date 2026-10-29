"""Refresh only the marked reading list from the public portfolio RSS feed."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlsplit
import re
import xml.etree.ElementTree as ET

FEED = 'https://khushal075.github.io/rss.xml'
ROOT = Path(__file__).resolve().parents[1]

def build_entries(xml_bytes):
    items = ET.fromstring(xml_bytes).findall('./channel/item')
    entries = []
    for item in items[:4]:
        title = ' '.join((item.findtext('title') or '').split())
        link = (item.findtext('link') or '').strip()
        url = urlsplit(link)
        if not title or url.scheme != 'https' or url.netloc != 'khushal075.github.io' or not url.path.startswith('/blog/'):
            raise ValueError('Unexpected blog entry; leaving README unchanged')
        title = re.sub(r'([\\`*_{}\[\]<>])', r'\\\1', title)
        entries.append(f'- [{title}]({link})')
    if not entries:
        raise ValueError('No posts found; leaving README unchanged')
    return '\n'.join(entries)

def main():
    with urlopen(FEED, timeout=30) as response:
        data = response.read(1_000_001)
    if len(data) > 1_000_000:
        raise ValueError('Feed too large')
    entries = build_entries(data)
    readme = ROOT / 'README.md'
    text = readme.read_text()
    pattern = r'<!-- BLOG:START -->.*?<!-- BLOG:END -->'
    replacement = '<!-- BLOG:START -->\n' + entries + '\n<!-- BLOG:END -->'
    updated, count = re.subn(pattern, lambda _: replacement, text, flags=re.S)
    if count != 1:
        raise ValueError('Expected exactly one reading-list marker pair')
    if text != updated:
        readme.write_text(updated)
        print('Updated blog reading list')
    else:
        print('Reading list already current')

if __name__ == '__main__':
    main()
