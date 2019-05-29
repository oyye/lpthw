from sys import argv

script, filename = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_one_line(line_num, f):
    print(line_num, f.readline(), end="")

print(f"First print all content in file {filename}.")
cur_file = open(filename)
print_all(cur_file)
print("Now rewind to position 0")
rewind(cur_file)

print("Finally print two lines: ")
line = 1
print_one_line(line, cur_file)
line += 1
print_one_line(line, cur_file)

cur_file.close()