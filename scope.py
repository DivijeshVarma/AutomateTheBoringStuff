# when the function is called and destroyed when the function returns. 
# Local variables cannot be used in the global scope.

# def spam():
#     ggs = 89
# 
# spam()
# print(ggs)


# code in one function local scope cannot use variables in another function's local scope

def spam():
    ggs = 89
    tofu()
    print(ggs)


def tofu():
    beans = 77
    ggs = 0


spam()


# Code in a local scope can access global variable

def tofu():
    print(beans)

beans = 77
tofu()

# if you want to assign a new value to a global variable from inside of a function.
# You have to add a global statement to the top of the function.

def tofu():
    global beans
    beans = 'kidney'
    print(beans)

beans = 77
tofu()
