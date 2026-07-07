def s(arr,n):
    profit=0
    m=arr[0]
    b=0
    for j in range(1,n):
        b=arr[j]-m 
        profit = max(profit,b)
        m=min(m,arr[j])
    print(profit)
arr=list(map(int,input().split()))
n=len(arr)
s(arr,n)