
fname = input("Enter File Name : ")
f = open(fname,"w")
text = input("Enter Text : ")
f.write(text)
f.close() # save and close
print("File created and text Written")