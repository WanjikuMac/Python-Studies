#this one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#that args is pointless we can actually do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one arguement

def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguement
def print_none():
    print("I got nothin'.")

print_two("Wanjiku", "Macharia")
print_two_again("Wanjiku", "Macharia")
print_one("First!")
print_none()