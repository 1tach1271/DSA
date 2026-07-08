# 1.
def f(arr,n):
    m=1
    for i in range(n):
        b=1
        a=arr[i]
        while a+1 in arr:
            b+=1
            a+=1
            m=max(m,b)
    print(m)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)

# 2.
def f(arr):
    a=set(arr)
    m=1
    n=len(a)
    for i in range(n):
        c=1
        b=arr[i]
        while b+1 in a:
            c+=1
            b+=1
        m=max(m,c)
    print(m)
arr=list(map(int,input().split()))
f(arr)

# 3.
def f(arr,n):
    arr=sorted(arr)
    c=0
    l=0
    s=float('-inf')
    for i in range(n):
        if arr[i]-1 ==s :
            c+=1
            s=arr[i]
        elif arr[i]!=s:
            c=1
            s=arr[i]
        l=max(l,c)
    print(l)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)

# 4.

def f(arr,n):
    if n==0:
        return 0
    l=1
    a=set()
    for i in range(n):
        a.add(arr[i])
    for i in a:
        if i-1 not in a:
            c=1
            b=i
            while b+1 in a:
                b+=1
                c+=1
            l=max(l,c)
    print(l)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)