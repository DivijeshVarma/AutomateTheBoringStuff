def PhoneNum(text):  # 9495767232
    if len(text) != 10:
        return False
    for i in range(10):
        if not text[i].isdecimal():
            return False
    return True


# print(PhoneNum('9493675436'))

message = "call me at 9493675436 or another 949576723"

found = False

for i in range(len(message)):
    chunk = message[i:i+10]
    if PhoneNum(chunk):
        print(f"Phone Number Found: {chunk}")
        found = True


if not found:
    print("Number not found")
