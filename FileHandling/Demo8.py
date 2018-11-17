
import os.path as pa
fname = input("File Name with Ext : ")
res = pa.exists(fname)
if res:
    f = open(fname)
    s = f.read()
    print(s)
    f.close()
else:
    print("File Not Available")


