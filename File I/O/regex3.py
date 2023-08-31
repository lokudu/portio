import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'lokudu@gmail.com'

pattern2 = re.compile(r"([A-Za-z0-9$&@#%*()]{8,\d})")
passwaord = 'P@mel@@2o2o'
a = pattern.search(string)

check = pattern2.fullmatch(passwaord)

print(check)