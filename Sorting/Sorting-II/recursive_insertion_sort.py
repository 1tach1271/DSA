def insertion_srot(arr,n,i):
    if i==n:
        return
    j = i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    insertion_srot(arr,n,i+1)
arr  = list(map(int,input("Enter the array: ").split()))
n = len(arr)
insertion_srot(arr,n,0)
print(arr)