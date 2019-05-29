from sys import argv

script, filename = argv
print(f"We're going to erase file {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want, just hit return.")

input("?")

print("Operning file:")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Please enter three lines ")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Start to write file now.")
target.write(line1)
target.write("\n")
target.write(line2 + "\n")
target.write(line3 + '\n')

print("Closing file now.")
target.close()