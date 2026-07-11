# 1.
def f(arr,n,k):
    c=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for l in range(i,j+1):
                s+=arr[l]
            if s==k:
                c+=1
    print(c)
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
f(arr,n,k)

# 2.
def f(arr,n,k):
    s=arr[0]
    c=0
    left=0
    right=0
    while right<n:
        while left<=right and s>k:   
            s-=arr[left]
            left+=1
        if s==k:
            c+=1
        right+=1
        if right<n:
            s+=arr[right]
    print(c)
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
f(arr,n,k)

# 3.
def f(arr,n,k):
    s=0
    c=0
    left=0
    for i in range(n):
        s+=arr[i]
        while s>k:
            s-=arr[left]
            left+=1
        if s==k:
            c+=1
    print(c)
    
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
f(arr,n,k)
