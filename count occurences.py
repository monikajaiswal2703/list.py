# list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# d=[]
# while i<len(list):
#     j=0
#     n=[]
#     count=0
#     while j<len(list):
#         if list[i] in list:
#             if list[i]==list[j]:
#                 count+=1
#         j+=1
#     n.append(list[i])
#     n.append(count)
#     if n not in d:
#         d.append(n)
#     i+=1
# print(d)

list = [1, 3, 4, 1, 3, 4, 5, 6, 5, 3, 4, 6, 6, 2, 4]
i=0
d=[]
while i<len(list):
    j=0
    n=[]
    count=0
    while j<len(list):
        if list[i] in list:
            if list[i]==list[j]:
                count+=1
        j+=1
    n.append(list[i])
    n.append(count)
    if n not in d:
        d.append(n)
    i+=1
print(d)
    
# a=[1, 1, 2, 3, 4, 4, 5, 1]
# i=0
# d=[]
# while i<len(a):
#     j=0
#     n=[]
#     count=0
#     while j<len(a):
#         if a[i] in a:
#             if a[i]==a[j]:
#                 count+=1 
#         j+=1
#     n.append(a[i])
#     n.append(count)
#     if n not in d:
#         d.append(n)
#     i+=1
# print(d)



# n=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# c=1
# max= n[i]
# while i<len(n):
#     if len(max)>len(n[i]):
#         max=n[i]
#         c+=1
#     i=i+1
# print((max,c))

     
