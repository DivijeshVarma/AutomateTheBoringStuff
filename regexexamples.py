import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo)
print(mo.group())
print(mo.group(1))

############
# wo group can appear 1 or zero times
# ?-- 0 or 1

batRegex2 = re.compile(r'Bat(wo)?man')
mo2 = batRegex2.search('welcome Batwoman')
mo44 = batRegex2.search('welcome Batwowowoman')
print(mo2.group())
print(mo44 == None)

#############
# first 3 digits group can appear 1 or zero times
phoneRegex = re.compile(r'(\d\d\d)?\d\d\d\d\d\d\d')
mo3 = phoneRegex.search('my phone no is 4938484')
print(mo3.group())

#############
# if you want regex object for text dinner?
# in this case 'dinner' is not optional, we looking
# for question mark.
dinnerRegex = re.compile(r'dinner\?')
mo = dinnerRegex.search('coming to dinner?')
print(mo.group())

#############
# *-- 0 or more
# to skip * enter \*
batRegex3 = re.compile(r'Bat(wo)*man')
mo4 = batRegex3.search('welcome Batwowowoman')
print(mo4.group())

#############
# +-- 1 or more
# to skip + enter \+
batRegex5 = re.compile(r'Bat(wo)+man')
mo5 = batRegex5.search('welcome Batwoman')
mo6 = batRegex5.search('welcome Batman')
mo7 = batRegex3.search('welcome Batwowowoman')
print(mo5.group())
print(mo6 == None)
print(mo7.group())

################
# To escape special characters
regex = re.compile(r'\?\*\+')
mo8 = regex.search('i learned about ?*+ syntax')
print(mo8.group())

regex2 = re.compile(r'(\?\*\+)+')
mo9 = regex2.search('i learned about ?*+?*+?*+?*+ syntax')
print(mo9.group())

# match specific repetitions of group
haregex = re.compile(r'(ha){3}')
mo9 = haregex.search('he said "hahaha"')
print(mo9.group())

# match specific range of group, min3 max5
haregex = re.compile(r'(ha){3,5}')
mo9 = haregex.search('he said "hahahahaha"')
print(mo9.group())

# greedy match with max
haregex = re.compile(r'(\d){3,5}')
mo9 = haregex.search('he said 95939582747')
print(mo9.group())

# non greedy match using ?
haregex = re.compile(r'(\d){3,5}?')
mo9 = haregex.search('he said 95939582747')
print(mo9.group())
