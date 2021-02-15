# This program asks for name and says hello

print('Hello World')
# ask for name
print('What is your Name?')
myName = input()
print(f"good to meet you, {myName}")
print(f"length of your name {len(myName)}")

print('what is your age?')
myAge = input()
# input function returns string
print(f"you will be {int(myAge) + 1} in a year.")
