# 1.
def f(arr,r,c):
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                for s in range(c):
                    if arr[i][s]!=0:
                        arr[i][s]=-1
                for y in range(r):
                    if arr[y][j]!=0:
                        arr[y][j]=-1
    for i in range(r):
        for j in range(c):
            if arr[i][j]==-1:
                arr[i][j]=0
    print(arr)
arr=[[1,1,1],[1,0,1],[1,1,1]]
r=len(arr)
c=len(arr[0])
f(arr,r,c)

# 2.
def f(arr,r,c):
    a=[]
    b=[]
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                a.append(i)
                b.append(j)
    for i in a:
        arr[i]=[0]*c
    for j in b:
        for i in range(r):
            arr[i][j]=0
    print(arr)
arr=[[1,1,1],[1,0,1],[1,1,1]]
r=len(arr)
c=len(arr[0])
f(arr,r,c)

# 3.
def f(arr,r,c):
    a=1
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                arr[i][0]=0
                if j!=0:
                    arr[0][j]=0
                else:
                    a=0
    for i in range(1,r):
        for j in range(1,c):
            if arr[i][j]!=0:
                if arr[0][j]==0 or arr[i][0]==0:
                    arr[i][j]=0
    if arr[0][0]==0:
        for j in range(c):
            arr[0][j]=0
    if a==0:
        for i in range(r):
            arr[i][0]=0
    print(arr)
arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r=len(arr)
c=len(arr[0])
f(arr,r,c)