arr = [10,20,30,40,50]

x = 30

start = 0
end = len(arr)-1

for i in range (len(arr)):
    arr.sort()
    mid = (start + end)//2
    if arr[mid] == x:
        print("Element is present at index", mid)
        break
    elif arr[mid] < x:
        start = mid + 1     
    else:
        end = mid - 1
else:    print("Element is not present in array")

