
Mylist = [1,"hello","20","Pune",5655565]
print(Mylist)

#inserting in list 
Mylist.append("addhogya")
print(Mylist)

#inserting at specific location .insert(index,value)
Mylist.insert(1,"aagyahumain")
print(Mylist)

#remove from list last element
Mylist.pop()
print(Mylist)

#remove from specific index
Mylist.pop(3)
print(Mylist)

#deleting specific value
Mylist.remove("hello")
print(Mylist)

#search in list output in boolean
print("Pune" in Mylist)

#finding index of specific data in list
print(Mylist.index("Pune"))