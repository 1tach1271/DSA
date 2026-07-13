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
    print(b.sort())
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)