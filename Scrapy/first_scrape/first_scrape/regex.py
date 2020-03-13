import re

string = ['abcde', 'abc123def', '1ijklmn', 'o12232p11']
pattern = '[abcde]'

a = [re.findall(pattern, x) for x in string]
print("Patternnn", a)