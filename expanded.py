# num=input("enter the number:")
# i=0
# add=""
# while i<len(num):
#     add+=num[i]
#     j=1
#     while j<=(len(num)-(i+1)):
#         add+="0"
#         j+=1
#     if i==(len(num)-1):
#         pass
#     else:
#         add+="+"
#     i+=1
# print(add)

a=input("enter the number")
i=0
add=""
while i<len(a):
    add+=a[i]
    j=1
    while j<=(len(a)-(i+1)):
        add+="0"
        j+=1
    if i==(len(a)-1):
        pass
    else:
        add+="+"
    i+=1
print(add)