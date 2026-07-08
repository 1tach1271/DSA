# 1. 
def f(arr,n):
    a=[]
    for i in range(n):
        leader = True
        for j in range(i+1,n):
            if arr[j]>=arr[i]:
                leader = False
                break
        if leader:
            a.append(arr[i])
    return a

arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))

# 2.
def f(arr,n):
    a= float('-inf')
    b=[]
    for i in range(n-1,-1,-1):
         
        if arr[i]>a:
            a=arr[i]
            b.append(a)
    b[:]=b[::-1]
    print(b)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)