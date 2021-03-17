'''
If module not found error occurs.
import os, sys
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
'''


from main import getLink
print(getLink('https://drive.google.com/file/d/0B9cVpIKZxC6fc3RhcnRlcl9maWxlX2Rhc2hlclYw/view?usp=sharing'))
print(getLink('https://drive.google.com/file/d/0B9cVpIKZxC6fc3RhcnRlcl9maWxlX2Rhc2hlclYw/view?usp=sharing','pdf'))

