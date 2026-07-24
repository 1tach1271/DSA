# 1.
def f(arr,n,k):
    c=0
    for i in range(n):
        x=0
        for j in range(i,n):
            x^=arr[j]
            if x==k:
                c+=1
    print(c)
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
f(arr,n,k)

# 2.
from collections import defaultdict
def f(arr,n,k):
    c=0
    h=defaultdict(int)
    x=0
    for i in range(n):
        x^=arr[i]
        if x==k:
            c+=1
        s=x^k 
        if s in h:
            c+=h[s]
        h[x]+=1
    print(c)
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
f(arr,n,k)