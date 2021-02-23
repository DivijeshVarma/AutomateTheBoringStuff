import pprint
# Dictionary Datatype
# like lists Dictionary is collection of many values

mycat = {'size': 'thin', 'color': 'gray', 'name': 'dicy'}
print(f" my cat has {mycat['color']} fur")

spam = {123: 'combination', 42: 'answer'}
print(spam)

# Dictionary have no order

mycat = {'size': 'thin', 'color': 'gray', 'name': 'dicy'}
yourcat = {'name': 'dicy', 'size': 'thin', 'color': 'gray'}
print(mycat == yourcat)
print('name' in mycat)
print('name' not in mycat)

# dictionaries are mutable like lists, variables hold references
# to dictionaries values not directly values itself

print(mycat.keys())
print(list(mycat.keys()))
print(list(mycat.values()))
# items returns key, value tuples
print(list(mycat.items()))

######################
mycat = {'size': 'thin', 'color': 'gray', 'name': 'dicy'}

for k, v in mycat.items():
    print(k, v)

for i in mycat.items():
    print(k, v)

print('gray' in mycat.values())

# return empty string if no key present

print(mycat.get('species', ''))

picnic_items = {'cups': 2, 'spoons': 6}
print(f"i am bringing {picnic_items.get('napkins', 0)} napkins to picnic")

# to set default key value if not present

mycat = {'size': 'thin', 'color': 'gray', 'name': 'dicy'}

mycat.setdefault('height', 'normal')
print(mycat)

####################
# count no of characters appears

message = """The greatest glory in living lies not in never falling,
             but in rising every time we fall."""
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] += 1

# print(count)
# pretty print function can display dicts values cleanly
# pformat function returns string value of this o/p
pprint.pprint(count)

text = pprint.pformat(count)
print(text)

print(type(43))
print(type(4.3))
print(type('hello'))
print(type(count))
