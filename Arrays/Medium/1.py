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