# 1.

def p(arr,n):
    m = float('-inf')
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            m = max(m,s)
    print(m)
arr=list(map(int,input().split()))
n=len(arr)
p(arr,n)

# 2.
def p(arr,n):
    m = float('-inf')
    s=0
    for i in range(n):
        s+=arr[i]
        if s>m:
            m=s
        if s<0:
            s=0
    print(m)
arr=list(map(int,input().split()))
n=len(arr)
p(arr,n)