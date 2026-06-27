def insertion_sort(arr,n):
    for i in range(1,n):
        j =i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    print(arr)
arr = list(map(int,input("Enter the array ").split()))
n = len(arr)
insertion_sort(arr,n)