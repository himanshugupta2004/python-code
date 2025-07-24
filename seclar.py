def calSecLar(arr,n):
    n = len(arr)
    first = -1
    sec = -1

    for i in range(n):
        if (arr[i]>first):
            sec = first
            first = arr[i]
        elif(arr[i]<first and arr[i]>sec):
            sec = arr[i]
    return sec


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    n = int(input())
    print(calSecLar(arr,n))