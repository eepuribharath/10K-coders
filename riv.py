# # print(bool())


# # import keyword 
# # print(keyword.kwlist)

# # a = 10,20,30
# # print(type(a))


# n = (input("Enter a number:"))

# # if(n%2==0):
# #     print(n," is even")
# # else:
# #     print(n,"is Odd")

# if(n>0):
#     print("Positive")
# elif(n==0):
#     print("Constant")
# else:
#     print("Negative")




# n = input()


# if(ord('a')<=ord(n)<=ord('z')):
#     print(ord(n))
#     print("given character is digit")

# elif(ord('0')<=ord(n)<=ord('9')):
#     a=ord(n)+1
#     print(chr(a))
# else:
#     l=[]
#     l.append(n)
#     print(l) 


# ch = ord('A')
# print(ch)




# n= input()

# if(ord('A')<=ord(n)<=ord('Z')):
#     a=ord(n)+32
#     print(chr(a))

# elif(ord('a')<=ord(n)<=ord('z')):
      
#       b=ord(n)-32
#       print(chr(b))
# else:
#     l=[]
#     l.append(n)
#     print(l) 



# packs=6
# cookies=6
# for i in range(1,packs+1,1):
#     for j in range(1,cookies+1):
#         print("cookies produced",j)
#     print(i,"the pack")   


# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()    

# n = 5
# m=2
# z=3
# for i in range(n):
#     for j in range(i):
#         print("*",end="  ")
#     print()
     


n = 3
m = 10
val = 65    
for i in range(n):
    for j in range(m):
        print(chr(val),end="")
        val+=1
    print()



