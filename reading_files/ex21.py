def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a -b

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a*b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a/b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")
what = add(age,subtract(height, multiply(weight, divide(iq,5))))

print("That becomes: ", what, "can you do it by hand?")

#ADDING A FORMULA
print("Enter a number:")
val1 = int(input())
val2 = int(input())
formula = divide(add(val1,34), subtract(100,val2))
print("Result: ", formula)