# 1 Brute Force for Finding at nth row and mth column
def f(n,r,c):
    a= 1
    for i in range(1,r):
        a=a*i
    b=1
    for i in range(1,c):
        b=b*i
    d = 1
    for i in range(1,r-c+1):
        d=d*i
    print(a//(b*d))
n=int(input())
r=int(input())
c=int(input())
f(n,r,c)

# 2 Better Approcah
def f(n,r,c):
    r=r-1
    c=c-1
    a=1
    for i in range(c):
        a=a*(r-i)
        a=a//(i+1)
    print(a)
n=int(input())
r=int(input())
c=int(input())
f(n,r,c)

# 3. For nth row and nth and mth element
def f(r,c):
    r=r-1
    c=c-1
    a=1
    for i in range(c):
        a=a*(r-i)
        a=a//(i+1)
    return a
def fg(r):
    for c in range(1,r+1):
        print(f(r,c),end=" ")
#n=int(input())
r=int(input())
c=int(input())
fg(r)
print()
print(f(r,c))

# 4 For nth row
def fg(r):
    a=1
    print(a,end= " ")
    for c in range(1,r):
        a=a*(r-c)
        a= a//c
        print(a,end=" ")
r=int(input())
fg(r)

# 5.
def fg(r):
    a=1
    b=[]
    b.append(a)
    for c in range(1,r):
        a=a*(r-c)
        a= a//c
        b.append(a)
    print(b)
def f(n):
    a=[]
    for i in range(1,n+1):
        a.append(fg(i))
    return a    
n=int(input())
f(n)