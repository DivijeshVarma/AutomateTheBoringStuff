spam = 0

while spam < 5:
    print(spam)
    spam += 1

# break

name = True

while name:
    ins = input('Enter name: ')
    if ins == '':
        print('Enter name')
    else:
        print(ins)
        break

# continue
# continue jumps back to while loop

spam = 0

while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print(spam)
