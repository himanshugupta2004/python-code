from array import *

val = array("i" , [1,2,3,4,5,6])

for i in val:
    print (i , end= " ")
print("\n")
print(len(val))

print (val.typecode)
print("\n")
val.reverse()
for i in range(0,len(val)):
    print(val[i], end=" ")
print("\n")

val.insert(2,5)
for i in range(0,len(val)):
    print(val[i], end=" ")
print("\n")
val[3] = 100
for i in range(0,len(val)):
    print(val[i], end=" ")
print("\n")
val.append(200)
for i in range(0,len(val)):
    print(val[i], end=" ")
print("\n")

coppyArray = array(val.typecode , (x for x in val))

for i in range(0,len(coppyArray)):
    print(coppyArray[i], end=" ")
print("\n")

coppyArray = array(val.typecode , (x*3 for x in val))

for i in range(0,len(coppyArray)):
    print(coppyArray[i], end=" ")
print("\n")

# Deleting element
coppyArray.pop()
for i in range(0,len(coppyArray)):
    print(coppyArray[i], end=" ")
print("\n")

coppyArray.pop(3)
for i in range(0,len(coppyArray)):
    print(coppyArray[i], end=" ")
print("\n")

coppyArray.remove(9)   #kya data delete karna hai tab use karo
for i in range(0,len(coppyArray)):
    print(coppyArray[i], end=" ")
print("\n")

#slicing

newArray = array("i", [1,2,3,4,5,6,7,8,9])
for i in range(0,len(newArray)):
    print(newArray[i], end=" ")
print("\n")

slicedArray = newArray[1:5] #include 1 exclude 5 indexing
slicedArray2 = newArray[1:-2] #last 2 exclude
#reverse using slicing
slicedArray3 = newArray[::-1]

for i in range(0,len(slicedArray)):
    print(slicedArray[i], end=" ")  
print("\n")

#user input in array
#user_array = array("i",[])

#n = int(input("Enter the size : "))
#for i in range(0,n):
  #  user_array.append(int(input("enter the array element : ")))

#for i in range(0,len(user_array)):
 #   print(user_array[i], end=" ")
#print("\n")


#finding element

array3 = array("i" , [10,20,30,40,50,60,70,80,90])

i = array3.index(50)
print(i)

