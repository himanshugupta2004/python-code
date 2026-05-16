arr = [1,2,3,4]

target = 5

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Subarray with target sum found at indices", i, "and", j)