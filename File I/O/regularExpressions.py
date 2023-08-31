import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search this inside this text please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group(2))