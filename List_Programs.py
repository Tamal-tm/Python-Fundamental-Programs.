# List with different data types.

mylist1=["Blair",1,4.2,"Project","Demon",3.187493]
print(mylist1)

print(mylist1[2])

mylist1[2]="Hulk"
print(mylist1)

del mylist1[-1]
print(mylist1)

mylist1.remove(1)
print(mylist1)

print(mylist1[0:3])

for list in mylist1:
    print(list)

mylist1.append("Witch")
print(mylist1)

mylist1.insert(4, "Movie")
print(mylist1)

if "Blair" in mylist1:
        print("Got it.")

mylist2=[600,60,70]
mylist1.extend(mylist2)
print(mylist1)

print(max(mylist2))

mylist3=mylist1.copy()
print(mylist3)

mylist2.sort()
print(mylist2)

