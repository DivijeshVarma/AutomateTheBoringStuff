spam = list(range(0, 100, 2))
print(spam)


office = ['pens', 'books', 'flames', 'boards']

for i in range(len(office)):
    print(f"index position {i} is {office[i]}")


cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
sound = cat[2]

# Same as above
size, color, sound = cat

# swapping variables

a = 'AAA'
b = 'BBB'

a, b = b, a

# methods

cat = ['fat', 'orange', 'loud']
cat.index('loud')
cat.append('short')
cat.insert(1, 'tail')
cat.remove('orange')

del cat[1]

cat.sort()
cat.sort(reverse=True)

spam = ['A', 'Z', 'a', 'z']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)

list('hello')

name = 'divijesh'

name[0]
name[1:3]
name[-1]
# vi in name

for letter in name:
    print(letter)

# lists and string are different in important way
# list value is mutable data type added, removed, changed
# string value is immutable cannot be changed

# proper way to modify string, create new strings from slices
name = 'zophie a cat'
new_name = f"{name[0:7]} the {name[8:12]}"
print(new_name)

# When you assign List to a variable, actually assigning list reference to a
# variable, cheese copies reference of spam

spam = [1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello'
print(cheese)
print(spam)
