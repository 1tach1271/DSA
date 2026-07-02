1.

def a(arr,n,k):
    l=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for a in range(i,j+1):
                s+=arr[a]
            if s==k:
                l=max(l,j-i+1)
    print(l)
arr = list(map(int,input().split()))
n = len(arr)
k=int(input())
a(arr,n,k)

2.

 
def s(arr,n,k):
    l=0
    left=0
    right=0
    sum=arr[0]
    while right<n:
        while left<= right and sum>k:
            sum-=arr[left]
            left+=1
        if sum==k:
            l =max(l,right-left+1)
        right+=1
        if right<n:
            sum+= arr[right]
    print(l)
arr=list(map(int, input().split()))
n=len(arr)
k=int(input())
s(arr,n,k)