"""Prepare the static Site for its GitHub Pages project path."""
from pathlib import Path
import shutil,re
src=Path(__file__).parent/'dist';out=Path(__file__).parent/'_site'
if out.exists():shutil.rmtree(out)
shutil.copytree(src,out)
repo='vremya-expertov-sochi'
base=f'https://korew22220-dev.github.io/{repo}'
old='https://vremya-expertov-sochi.korew22220.chatgpt.site'
for f in out.rglob('*.html'):
 s=f.read_text()
 s=s.replace(old,base)
 for attr in ['href','src','data-photo']:
  s=s.replace(f'{attr}="/',f'{attr}="/{repo}/')
 f.write_text(s)
(out/'sitemap.xml').write_text((src/'sitemap.xml').read_text().replace(old,base))
(out/'robots.txt').write_text((src/'robots.txt').read_text().replace(old,base))
(out/'.nojekyll').write_text('')
print('Prepared',len(list(out.rglob('index.html'))),'pages for',base)
