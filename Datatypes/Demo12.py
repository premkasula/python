
d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}
print(d1)
d1.clear() # Removing all pairs from dict
print(d1)

print("------------------------")

d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

value = d1.get("name")
print(value) # Ravi
value = d1.get("status")
print(value) # None

print("------------------------")

d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

val = d1.items()
print(val) # a list of tuple's
val1 = d1.keys()
print(val1) # a list of keys
val2 = d1.values()
print(val2) # a list of values

print("------------------------")

d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

print(d1)
value = d1.pop("name")
print(value)
print(d1)


print("------------------------")

d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

print(d1)
d1.popitem()
print(d1)

print("------------------------")

d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

print(d1)
val = d1.setdefault("name")
print(val) # Ravi
val = d1.setdefault("status")
print(val) # None
print(d1)


