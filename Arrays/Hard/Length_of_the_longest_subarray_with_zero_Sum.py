# 1.
def f(arr,n):
    s=0
    l=0
    a={}
    for i in range(n):
        s+=arr[i]
        if s==0:
            l=i+1
        elif s in a:
            l = max(l,i-a[s])
        else:
            a[s]=i 
    print(l)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)

# 2.
from collections import defaultdict
def f(arr,n):
    s=0
    m=0
    h=defaultdict(int)
    for i in range(n):
        s+=arr[i]
        if s==0:
            m=i+1
        if s!=0:
            if s in h:
                m=max(m,i-h[s])
            else:
                h[s]=i
    print(m)           
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)