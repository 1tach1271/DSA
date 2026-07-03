# 1.

def t(arr,n,k):
    s=0
    for i in range(n):
        for j in range(n):
            s=arr[i]+arr[j]
            if s==k:
                print("Yes")
                print(i,j)
                return
    print("NO")
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
t(arr,n,k)

# 2.
from collections import defaultdict
def t(arr,n,k):
    a =0
    m={}
    for i, num in enumerate(arr):
        a=k-num
        if a in m:
            return "Yes"
        else:
            m[num]=i
    return "NO"
def s(arr,n,k):
    m={}
    for i, num in enumerate(arr):
        a=k-num
        if a in m:
            return [m[a],i]
        m[num]=i
    return [-1,-1]
arr=list(map(int,input().split()))
n=len(arr)
k = int(input())
print(t(arr,n,k))
print(s(arr,n,k))

# 3.

def p(arr,n,k):
    a=sorted(arr)
    left =0
    right = n-1
    while left<right:
        if a[left]+a[right] >k:
            right-=1
        elif a[left]+a[right]<k:
            left+=1
        elif a[left]+a[right]==k:
            return "Yes"
    return "NO"
def m(arr,n,k):
    a={}
    for i , num in enumerate(arr):
        x=k-num
        if x in a:
            return [a[x],i]
        a[num]=i 
    return [-1,-1]
arr=list(map(int,input("Enter the array: ").split()))
n = len(arr)
k=int(input("Enter the number sum: "))
print(m(arr,n,k))
print(p(arr,n,k))