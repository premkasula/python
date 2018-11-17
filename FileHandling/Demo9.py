
import os.path as pa
fname = input("File Name : ")
if pa.exists(fname):
    for x in open(fname,"r"):
        print(x)
else:
    print("File not Found")