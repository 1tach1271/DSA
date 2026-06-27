def  pattern(arr,n):
    if n ==1:
        return
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    pattern(arr,n-1)
arr  = list(list(map(int,input("Enter the array: ").split())))
n = len(arr)
pattern(arr,n)
print(arr)