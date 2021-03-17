# Drive-URL-Decoder

Simple module to get direct download Link for all well known Cloud storages at one place.

Sample Usage:
```
from main import getLink
print(getLink('https://drive.google.com/file/d/0B9cVpIKZxC6fc3RhcnRlcl9maWxlX2Rhc2hlclYw/view?usp=sharing'))
print(getLink('https://drive.google.com/file/d/0B9cVpIKZxC6fc3RhcnRlcl9maWxlX2Rhc2hlclYw/view?usp=sharing','pdf'))
```
Included Sites / Services

- Dropbox
- One Drive
- Google Drive
- Google Docs, Sheets, Slides

Todo -

- Publish a package
- Add more sites
- Add more features (currently; only **to direct link** feature)

Known Supported Formats:
- Google Docs - doc,pdf
- Google Slide - pdf,pptx
- Google Sheet - xlsx,pdf,csv

License : [![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/)
