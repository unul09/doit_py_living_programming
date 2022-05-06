import os, re

pattern = r'is'
script = '1 is one in english'

#re.match(pattern, script).group()
re.search(pattern, script).group()