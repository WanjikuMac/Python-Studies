from sys import argv
#can you read a file in a different directory from
#this python script
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())