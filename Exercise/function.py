# working with function


def say_hello(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hello("Suman", 27)
say_hello("Saurav", 29)

# working with function and return statement


def cube(num):
    return num * num * num


result = cube(4)
print(result)
print(cube(3))
