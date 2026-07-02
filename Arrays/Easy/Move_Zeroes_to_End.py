def m(arr,n):
    a=0
    for i in range(n):
        if arr[i]!=0:
            arr[a],arr[i]=arr[i],arr[a]
            a+=1

    print(arr)
arr=list(map(int,input("Enter the array: ").split()))
n =len(arr)
m(arr,n)