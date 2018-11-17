
fname = input("File Name : ")
f = open(fname,"a")
text = input("Enter Text : ")
f.write(text)
f.close()
print("Text Written to File")

