# a=[[1,2,3],[5,6,7],[4,5,1],[4,5,9]]
# for i in range (len(a)):
#     max=0
#     for j in range(len(a[i])):
#         if a[i][j]>max:
#            max=a[i][j]
#     print(max)

# a=[[1,2,3],[5,6,7],[4,5,1],[4,5,9],[7,8,10]]
# i=0
# while i<len(a):
#     max=0
#     j=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#         j+=1
#     i+=1
# print(max)
    # i=0
    # while i<len(a):
    #     max1=0
    #     j=0
    #     while j<len(a[i]):
    #         if a[i][j]>max1:
    #             if a[i][j]!=max:
    #                 max1=a[i][j]
    #         j+=1
    #     i+=1
    #     print(max1)
# a=[[1,2,3,4],[5,6],[3,4,5]]
# i=0
# d=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         d.append(a[i][0]+a[i][1]+a[i][2])
#         break
#     i+=1
# print(d)
# i=0
# while i<len(a):
#     j=0
#     l=0
#     while j<len(a[i]):
#         if a[i][j]>l:
#             l=a[i][j]
#         j+=1
#     i+=1
#     print(l)


# a=[[1,2,3,4],[5,6],[3,4,5]]
# i=0
# c=1
# max=a[i]
# while i<len(a):
#     if len(max)<len(a[i]):
#         max=a[i]
            # length=len(a[i])
#         c=c+1
#     i+=1
# print(max,c)
# i=0
# while i<len(a):
#     m=1
#     j=0
#     while j<len(a[i]):
#         m=m*a[0][j]
#         j+=1
#     i+=1
#     print(m)
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum+=a[i][0]
#         j+=1
#     i+=1
# print(sum)



"interview question, max,length,sum,multiply"

a=[[1,2,3,4],[5,6],[3,4,5],[8]]
sum=0
mul=1
i=0
while i<len(a):
    max=len(a[i])
    j=0
    while j<len(a):
        if len(a[j])>max:
            max=len(a[j])
        j+=1
    if len(a[i])==max:
        print(a[i],max)
    i+=1
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a[i])==max:
            sum=sum+a[i][j]
            mul*=a[i][j]
        j+=1
    i+=1
print(sum)
print(mul)
    
    
        
        

    



    