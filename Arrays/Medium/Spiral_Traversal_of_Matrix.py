def f(matrix,r,c):
    top=0
    bottom = r-1
    left = 0
    right = c-1
    while top<=bottom and left<= right:
        for i in range(top,right+1):
            print(matrix[top][i],end=" ")
        top+=1
        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
            bottom-=1
        if left <=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")
            left+=1
r=int(input("Enter the number of total rows: "))
c=int(input("Enter the number of total columns: "))
matrix=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    matrix.append(row)
f(matrix,r,c)