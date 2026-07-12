# def f(r,c):
#     r=r-1
#     c=c-1
#     a=1
#     for i in range(c):
#         a=a*(r-i)
#         a=a//(i+1)
#     return a
def fg(r):
    a=1
    print(a,end= " ")
    for c in range(1,r):
        a=a*(r-c)
        a= a//c
        print(a,end=" ")
#n=int(input())
r=int(input())
# c=int(input())
fg(r)
# print()
# print(f(r,c))