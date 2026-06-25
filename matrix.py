# l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(l)):
#     for j in range (len(l[i])):
#         print(l[i][j],end=" ")
#     print()

# l=[[1,2,3],[4,5,6],[7,8,9]]
# l1=[[9,8,7],[6,5,4],[3,2,1]]
# for i in range(len(l)):
#     for j in range (len(l[i])):
#         print(l[i][j],end=" ")
#     print()
# print("--------------------------")
# for i in range(len(l1)):
#     for j in range(len(l1[i])):
#         print(l1[i][j],end=" ")
#     print()


# sum of the matrix
# l1=[[1,2,3],[4,5,6],[7,8,9]]
# l2=[[9,8,7],[6,5,4],[3,2,1]]

# l2=[]
# for i in range(len(l)):
#     l3=[]
#     for j in range(len(l[i])):
#         add=l[i][j]+l1[i][j]
#         l3.append(add)
#     l2.append(l3)
# # print(l2,end=" ")
# for i in range (len(l2)):
#     for j in range(len(l2[i])):
#         print(l2[i][j],end=" ")
#     print()

# multiplication matrix  
# l3=[]
# for i in range(len(l1)):
#     l=[]
#     for j in range(len(l1[i])):
#         mul=0
#         for k in range(len(l1[i])):
#             mul+=l1[i][k]*l2[k][j]
#         l.append(mul)
#     l3.append(l)
# for i in range(len(l3)):
#     for j in range(len(l3[i])):
#         print(l3[i][j],end=" ")
#     print()


l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    for j in range (len(l[i])):
        print(l[i][j],end=" ")
    print()
print("< ------------------------------ >")
for i in range(len(l)):
    for j in range (len(l[i])):
        print(l[j][i],end=" ")
    print()