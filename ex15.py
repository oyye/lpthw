from sys import argv

script, file_name = argv

txt = open(file_name)
print(f"Here is your file name: {file_name}")
print(txt.read())

print("File name again: ")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())