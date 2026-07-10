# 1.
def f(arr,r,c):
    a=[[0] *r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            a[j][r-1-i]=arr[i][j]
    print(a)
arr=[[0,1,2],[3,4,5],[1,3,1]]
r=len(arr)
c=len(arr[0])
f(arr,r,c)

# 2.
