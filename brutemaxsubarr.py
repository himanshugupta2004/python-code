arr = [1,2,3,4,5]

maxsum = 0

for i in range (len(arr)):
    sum = 0
    for j in range (i , len(arr)):
        sum = arr[i]+ arr[j]
        if maxsum < sum:
            maxsum = sum
print("Maximum sum of subarray is", maxsum)


