from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, hpw?

indata = read.(open(from_file))

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file esist? {exists(indata)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(in_file)

print("Alright, all done.")

out_file.close
in_file.close
