def pattern(arr,n):
    a = arr[0]
    for i in range(0,n):
        if a <arr[i]:
            a = arr[i]
    print(a)
arr = list(map(int,input("enter the array ").split()))
pattern(arr,len(arr))