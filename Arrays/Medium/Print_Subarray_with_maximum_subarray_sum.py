def p(arr,n):
    m = float('-inf')
    s=0
    a=0
    b=-1
    c=-1
    for i in range(n):
        if s==0:
            a=i
        s+=arr[i]
        if s>m:
            m=s
            b = a 
            c=i
        if s<0:
            s=0
    print(m)
    for i in range(b,c+1):
        print(arr[i],end=" ")
arr=list(map(int,input().split()))
n=len(arr)
p(arr,n)