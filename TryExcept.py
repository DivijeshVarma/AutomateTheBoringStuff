def divide42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('divide by zero')


# Function that return without return statement return None value
print(divide42by(10))
print(divide42by(2))
print(divide42by(0))
print(divide42by(4))


while True:
    catnum = input('how many cats do you have? Enter negative value to exit')
    try:
        if int(catnum) < 0:
            print("Don't enter negative value")
            break
        elif int(catnum) >= 4:
            print('lot of cats you have')
        else:
            print('not a lot of cats you have')
    except ValueError:
        print('Enter value not string')
