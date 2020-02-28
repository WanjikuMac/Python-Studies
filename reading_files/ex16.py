from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")
print("And write theses to the file.")
target.write(input("line 1: "))
target.write("\n")
target.write(input("line 2: "))
target.write("\n")
target.write(input("line 3: "))
target.write("\n")

print("And finally, we close it")
target.close()