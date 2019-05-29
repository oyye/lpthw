from sys import argv
from os.path import exists

script, infile, outfile = argv
print(f"Copying file {infile} to {outfile}.")

ifile = open(infile)
indata = ifile.read()

print(f"The input file {infile} contains {len(indata)} bytes.")
print(f"The out file {outfile} exists: {exists(outfile)}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want, just hit return.")
input()

ofile = open(outfile, "w")
ofile.write(indata)

print(f"Closing files : {infile} {outfile}")
ifile.close()
ofile.close()
