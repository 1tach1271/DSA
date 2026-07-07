# 1.
def s(arr,n):
    a=[0]*(n//2)
    b=[0]*(n//2)
    c=0
    d=0
    for i in range(n):
        if arr[i]>0:
            a[c]=arr[i]
            c+=1
        else:
            b[d]=arr[i]
            d+=1
    c=0
    d=0
    for i in range(n):
        if i%2==0:
            arr[i]=a[c]
            c+=1
        else:
            arr[i]=b[d]
            d+=1
    print(arr)
arr=list(map(int,input().split()))
n=len(arr)
s(arr,n)

# 2.
def s(arr,n):
    a=0
    b=1
    c=[0]*n
    for i in range(n):
        if arr[i]>0:
            c[a]=arr[i]
            a=a+2
        else:
            c[b]=arr[i]
            b=b+2
    print(c)
    
arr=list(map(int,input().split()))
n=len(arr)
s(arr,n)

3.
def s(arr,n):
    a=[]
    b=[]
    c=0
    d=0
    for i in range(n):
        if arr[i]>0:
            a.append(arr[i])
            c+=1
        else:
            b.append(arr[i])
            d+=1
    if c>d:
        for i in range(d):
            arr[i*2]=a[i]
            arr[i*2 +1]=b[i]
    else:
        for i in range(c):
            arr[i*2]=a[i]
            arr[i*2 +1]=b[i]
    k=d
    for i in range(2*d,n):
        arr[i]=a[k]
        k+=1
    k=c
    for i in range(2*c,n):
        arr[i]=b[k]
        k+=1
    print(arr)
arr=list(map(int,input().split()))
n=len(arr)
s(arr,n)