# l=[[1,2,3],[2,3,4],[4,5,6]]
# l1=l[0]
# print(l1[0:3:1])
# print(l1)
# print(l[2][2])

# print(l[0][0]:l[0][2]:1)

# print(l2[0:3:1])


# l=[[1,2,3],[2,3,4],[4,5,6]]
# # print(l[0][0:2+1])
# for i in l:
#     for j in i:
#         print(j)
#     print(i)

l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    sum=0
    for j in range(len(l[i])):
        sum+=l[i][j]
    print(sum)