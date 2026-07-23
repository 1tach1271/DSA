# 1.
# def f(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print(" "*(2*(n-i)),end="")
#         for j in range(i,0,-1):
#             print(j,end="")
#         print()
# n=int(input())
# f(n)

# 2.
# def f(n,m):
#     while n>0 and m>0:
#         if n>m:
#             n=n-m
#         else:
#             m=m-n
#     if n==0:
#         print(m)
#     else:
#         print(n)
# n=int(input())
# m=int(input())
# f(n,m)

# 3.
# def f(a,n):
#     b=a[::-1]
#     if a==b:
#         return "True"
#     else:
#         return "False"
# a=input()
# n=len(a)
# print(f(a,n))

# 4.
# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     for a,b in h.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 5.
# def s(arr,n):
#     for i in range(0,n-1):
#         a=i
#         for j in range(i+1,n):
#             if arr[j]<arr[a]:
#                 a=j
#         arr[i],arr[a]=arr[a],arr[i]
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# s(arr,n)

# 6.
# def f(arr,n):
#     a=[0]*n 
#     j=0
#     for i in range(n):
#         if arr[i]!=0:
#             a[j]=arr[i]
#             j+=1
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 7.
