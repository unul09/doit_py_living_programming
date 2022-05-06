import re
aa = 'aa'
character_pattern = repr(aa)
script = 'laaff, d'
lines = re.findall(character_pattern, script)

print(lines)