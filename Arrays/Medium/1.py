def f(arr,r,c):
    for i in range(1,r):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(r):
        arr[i]=arr[i][::-1]
    print(arr)
arr=[[0,1,2],[3,4,5],[1,3,1]]
r=len(arr)
c=len(arr[0])
f(arr,r,c)