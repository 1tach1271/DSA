# 1.
def s(arr,n):
    a=0
    b=0
    c=0
    for i in range(n):
        if arr[i]==0:
            a+=1
        elif arr[i]==1:
            b+=1
        else:
            c+=1
    i =0
    for _ in range(a):
        arr[i]=0
        i+=1
    for _ in range(b):
        arr[i]=1
        i+=1
    for _ in range(c):
        arr[i]=2
        i+=1
    print(arr)
arr=list(map(int,input("Enter the array: ").split()))
n = len(arr)
s(arr,n)

# 2.
def s(arr,n):
    low, mid, high =0,0, n-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)
arr=list(map(int,input("Enter the array: ").split()))
n = len(arr)
s(arr,n)