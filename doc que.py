
# "list items divisible by 5"
# num_list=[5,6,7,10,15,35,56,65]
# i=0
# a=[]
# while i<len(num_list):
#     if num_list[i]%5==0:
#         m=num_list[i]
#         a.append(m)
#     i+=1
# print(a)


# "duplicate items"
# num=[2,3,2,4,5,4,5,6,5,67,7,8,5,44]
# b=[]
# for i in num:
#     if i not in b:
#       b.append(i)
# print(b)
# non_dup=set(b)
# print(non_dup)

# a=[1,1,2,2,3,3,4,4,5,5,6,6,6,9,]
# s=set(a)
# a=list(s)
# print(a)



# i=700
# while i<=800:
#     a=i-699
#     i+=1
#     if i==721:
#        break
#     print(a)


# "10,user input again 1 user input and cheak in first list"
# i=0
# a=[]
# while i<10:
#     num=int(input("enter the number"))
#     i+=1
#     a.append(num)
# print(a)
# num1=int(input("enter the number"))
# if num1 in a:
#     print(num1, "is present a" )
# else:
#     print(num1,"not present a")



# a=[1,24,34,65,76,98]
# print("smallest number in list",min(a))
# print("largest number in list",max(a))


# 15,"removing even number"
# list = [1,2,3,4,5,6,7,8,9,10,12,21,13,31,14,41,15,51,61,16,72]
# i=0
# while i<len(list):
#     if i%2!=0:
#      print(i,end=" ")
#     else:
#         pass
#     i+=1
     



# "last digit reverse"
# a=[1,2,3,4,5]
# print(a[-1:]+a[:-1])



# "square list"
a_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=0
c=[]
new=[]
while i<5:
    b= a_list[i]**2
    c.append(b)
    j=-1
    e=[]
    while j>=-5:
            d=a_list[j]**2
            e.append(d)
            j-=1
    i+=1
i=0
while i<len(c):
        new.append(c[i])
        i+=1
i=0
while i<len(e):
        new.append(e[i])
        i+=1
print(new)   


# "characters into a string"  
# a_list=["p","y","t","h","o","n"]
# b_string="".join(a_list)          
# print(b_string) 

# "flatten a shellow lisyt"
# a=[[1,2,3],[4,5,6],[7,8,9]]
# flat_list=sum(a,[])
# print("orignal list",a)
# print ("transformed list",flat_list)

# "extend nested list"
# list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
# sub_list=["h","i","j"]
# list1.extend(sub_list)
# print(list1)

# "implement matrix addition"
# x=[[8,5,1],
# [9,3,2],
# [4.,6,3]]
# y=[[8,5,3],
# [9,5,7],
# [9,4,1]]
# c=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0,3):
#     for j in range(0,3):
#         c[i][j]=x[i][j]+y[i][j]
# print ("matrix -c is")
# for i in range(0,3):
#     for i in range(0,3):
#         print(c[i][j],end=" ")



# a="My name is Monika"
# b=a.split()
# i=0
# while i<len(b):
#     c=b[-i-1]
#     i+=1
#     print(c,end=" ") 
