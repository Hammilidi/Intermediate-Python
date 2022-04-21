mylist = ["banana", "cherry", "apple"]
print(mylist)

for i in range(len(mylist)):
    print(mylist[i])

if "banana" in mylist:
    print("yes")
else:
    print("no")


mylist.append("lemon")
mylist.insert(1, "blueberry")
item = mylist.pop()
print(item)
mylist.sort()


mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist1[::-1]
print(a)

mylist.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mylist)
