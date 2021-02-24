import re

# pass raw strings to compile function, text for pattern looking for
phonenumregex = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
mo = phonenumregex.search('call me at 9493675436 or another 9495767239')
print(mo.group())

print(phonenumregex.findall('call me at 9493675436 or another 9495767239'))
