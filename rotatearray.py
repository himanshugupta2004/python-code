arr = [10,20,30,50]

last =  arr[-1] #last value ko declare kiya ki isko shift karna hai 

for i in range(len(arr)-1 , 0 , -1):  #loop for trvaerse
    arr[i] = arr[i-1]   #shifting

arr[0] = last     #pahli wali ko override karna

print(arr)