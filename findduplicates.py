arr = [10,20,10 ,30,40,30]

dup = set()

for i in arr:
    if i in dup:
        print("Duplicate element is ", i)
    else:
        dup.add(i)

