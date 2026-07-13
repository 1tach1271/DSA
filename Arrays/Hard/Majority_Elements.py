# 1. O(n^2)
def f(arr,n):
    a=[]
    for i in range(n):
        if len(a)==0 or a[0]!=arr[i]:
            c=0
            for j in range(n):
                if arr[j]==arr[i]:
                    c+=1
            if c>n//3:
                a.append(arr[i])
        if len(a)==2:
            break
    print(a)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)

# 2. O(n)*O(logn)
from collections import defaultdict
def f(arr,n):
    a=[]
    h=defaultdict(int)
    for i in range(n):
        h[arr[i]]+=1
        if h[arr[i]]>n//3:
            a.append(arr[i])
    print(a)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)

# 3.
def f(arr,n):
    c=0
    c1=0
    e=-1
    e1=-1
    for i in range(n):
        if c==0 and arr[i]!=e1:
            c=1
            e=arr[i]
        elif c1==0 and arr[i]!=e:
            c1=1
            e1=arr[i]
        elif e ==arr[i]:
            c+=1
        elif e1 ==arr[i]:
            c1+=1
        else:
            c-=1
            c1-=1
    c=0
    c1=0
    for i in range(n):
        if e==arr[i]:
            c+=1
        if e1==arr[i]:
            c1+=1
    a = n//3
    b=[]
    if c>a :
        b.append(e)
    if c1>a:
        b.append(e1)
    print(sorted(b))
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)