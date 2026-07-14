# 1.
# def f(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(chr(65+j),end=" ")
#         print()
# n=int(input())
# f(n)

# 2.
# def p(n):
#     c=0
#     for i in range(1,int(n**(0.5))+1):
#         if n%i==0:
#             c+=1
#             if n//i!=i:
#                 c+=1
#     if c<=2:
#         print("Prime")
#     else:
#         print("Not Prime")
# n=int(input())
# p(n)

# 3.
# def p(i,n):
#     if i>=len(n)//2:
#         return True
#     if n[i]!=n[len(n)-i-1]:
#         return False
#     return p(i+1,n)
# n=input()
# print(p(0,n))

#4.
# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     mac=0
#     mic=n
#     mae=-1
#     mie=-1
#     for a,b in h.items():
#         if b>mac:
#             mac=b
#             mae=a
#         if b<mic:
#             mic=b
#             mie = a 
#     print(mae)
#     print(mie)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 5.
# def s(arr,n):
#     for i in range(0,n-1):
#         a = i
#         for j in range(i+1,n):
#             if arr[a]>arr[j]:
#                 a=j
#         arr[i],arr[a]=arr[a],arr[i]
#     print(arr)
# arr = list(map(int,input().split()))
# n=len(arr)
# s(arr,n)

# 6.
# def f(arr,n,k):
#     m=0
#     left =0
#     right=0
#     s=arr[0]
#     while right<n:
#         while left<=right and s>k:
#             s-=arr[left]
#             left+=1
#         if s==k:
#             m=max(m,right-left+1)
#         right+=1
#         if right<n:
#             s+=arr[right]
#     print(m)
# arr=list(map(int,input().split()))
# n=len(arr)
# k=int(input())
# f(arr,n,k)

# 7.
# def f(arr,n):
#     a=[]
#     m=arr[-1]
#     a.append(arr[-1])
#     for i in range(n-2,-1,-1):
#         if arr[i]>m:
#             a.append(arr[i])
#             m=arr[i]
#     a.reverse()
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)