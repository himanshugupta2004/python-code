from numpy import *

#array =  array([1,2,3,4,5])
#using numpy hetroarray = array([1,2.5,'hello']) is posssible different type of elements
#agar type convert karke array banana hai to - array = array([1,2,3,4,5] , float)  to iska output 1.0 , 2.0 3.0... is type ka aaayga

#array1 = linspace(10,20,11) #11 parts me divide hogaya and aaray me store hogaya
#array2 = arange(10,20,2) #10 se start hoke 20 se pehle tak 2 ke step me jayega
#array3 = zeros(5) #5 zero ka array banayega
#array4 = ones(5)  #5 one ka array banayega
#array5 = logspace(1,40,5) #1 se 40 tak 5 parts me divide karke 10^x ka array banayega
#array6 = full(10 , 5) #10 size ka array banayega jisme sab jagah 5 hoga

array2d = array([[1,2,3] , [6,7,8]]) #2d array banayega
print(array2d)

#for x in array:
 #   print(x, end=" ")

array3d = array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10,11,12]]]) #3d array banayega
print(array3d)
print("\n")