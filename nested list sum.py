# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<=i-i:
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
# print(sum)

a=[[1,2,3],[2,3,4],[3,4,5]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][0]+a[i][1])
        break
    i+=1
print(b)

# a=[[1,2,3],[2,3,4],[3,4,5]]
# b=[]
# for i in (a):
#     b.append(i[0]+i[1])
#     print(b)

# a=[1,2,3,[6,8],[7,8,9,10],8]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum+=a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)

# a=[1,2,3,[6,8],[7,[1,2],8,9,10],8]
# i = 0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j = 0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k = 0
#                 while k<len(a[i][j]):
#                     sum+=a[i][j][k]
#                     k+=1
#             else:
#                 sum+=a[i][j]
#             j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)


# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# i=0
# sum=0
# while i<len(a):
#     sum+=a[i]
#     i+=1
# j=0
# sum1=0
# while j<len(b):
#     sum1+=b[j]
#     j+=1
# # print(sum1)
# print(sum+sum1)

a=[1,2,3,4,5]
b=[4,5,6,7,8]
d=[7,6,5,4,9]
i=0
c=[]
while i<len(a):
    s=(a[i]+ b[i]+d[i])
    c.append(s)
    i+=1
print(c)