mydict = {"name": "Fidelis", "age": 21, "city": "Beni Mellal"}
print(mydict)

mydict["email"] = "fidelis@gmail.com"

mydict2 = dict(name="Mary", age=27, city="Diapaga")
print(mydict["name"])

mydict.pop("city")  # we can also use popitem()
print(mydict)

try:
    print(mydict["lastname"])
except:
    print("Error")

for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(f"{key}: {value}")
