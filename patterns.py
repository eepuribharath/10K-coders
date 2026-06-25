# n=4
# for i in range(1,n):
#     for j in range(1,i+1):
#         print("A",end=" ")
#     print()    
        
# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            



# n=6
# for i in range(n-1,0 ,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    

# n=10
# for i in range (n):
#     for j in range (n):
#         if(j==0 or i==j):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")  
#     print()   
# for i in range (n,0,-1):
#     for j in range (n+1):
#         if(j==0 or j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")  
#     print()     




# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         if(i==0 or j==0 or i==n-1 or j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# s=input("Enter a string: ")
# # n="ab" or "abc"

# # for s in n:
# #     print("true")
# # else:    
# #     print("false")

# if s=="ab" or s=="abc":
#     print("true")   
# else:    print("false")


#factorial of a number
# n=4
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print("Factorial of",n,"is",factorial)


#sum of a factioral is n 
# n=143
# sum_of_factorials=0
# for i in range (1,n+1):
#     fac=1
#     for j in range (1,i+1):
#         fac=fac*j
#     sum_of_factorials+=fac
# print(sum_of_factorials)

# n=int(input("Enter a number: "))
# fac=1
# for i in  range (1,n+1):
#     fac=fac*i
#     print(fac)

# n=143
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig    
#     n=n//10
# # print(dig)
# print(rev)


# n=143
# a=n//100
# print(a)
# b=(n//10)%10
# print(b)
# c=n%10
# print(c)

# fac=1
# fac*=a
# fac*=b  
# fac*=c
# print(fac)
# sum=0
# sum+=a+b+c
# print(sum)


# n=int(input("Enter a number: "))
# a=n*n
# b=a//10
# c=a%10
# d=b+c
# print(d)
# if(d==n):
#     print(n,"neon number")
# else:
#     print(n,"not a neon number")

