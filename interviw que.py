# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# c=0
# e=[]
# while c<len(a):
#     d= [a[c],(b[-c])]
#     e.append(d)
#     c+=1
# print(e)

# a=[[1,2,3,],[3,4,5],[5,6,7]]
# i=0
# while i<len(a):
#     j=0
#     max=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#           max=a[i][j]
#         j+=1
#     i+=1
#     print(max)

# a=[[1,2,3,],[3,4,5],[5,6,7]]
# i=0
# while i<len(a):
#     j=1
#     while j<=len(a):
#         if a[i]>a[j]:
#           b=a[i][j]
#         j+=1
#     i+=1
#     print(b)

# Given the start and end of a range, write a Python program to print all negative numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# for i in range(-4,5,1):
#     print(i,end=" ")
#     if i==-1:
#         break

# for i in range(-3,4,1):
#     print(i,end=" ")
#     if i==-1:
#         break

# Given start and end of a range, write a Python program to print all positive numbers in given range.
# Example:
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 

# for i in range(-4,5):
#     print(i,end=" ")
#     if i==1:
#         break
# i=0
# while i<=5:
#     print(i,end=" ")
#     i+=1


# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0
# while i<len(a):
#    b= a[i]%a
#    i+=1
# print(b)

"koi bhi number enter kare to string me letter de"

# a=["zero","one","two","three","four","five","six","eleven"]
# num=input("enter the number")
# i=0
# while i<len(num):
#     k=int(num[i])
#     print(a[k])
#     i+=1

# n=int(input("enter the number:-"))
# if n!=1 and n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 or n==2 or n==3 or n==5 or n==7:
#     print(n,"prime number")
# else:
#     print("not prime number")


# a="monika jaiswal"
# b="shivani mehta"
# # c=a+b
# # print([c])
# print(a,b)
# print("",a+"",b)
   

# "last digit reverse"
# a=[1,2,3,4,5,6,7,8]
# num=int(input("enter the number"))
# print(a[-num:]+a[:-num])

# a=[1,2,"true",3.0,5+2j,34]
# a[2]="apple"
# print(a)




# "remove 000 in list"
# a=[10,22000,13000,447000,100,1230000]
# i=0
# c=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             c.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(c)
        

    



# c=[1,2,3]
# for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 if (i!=j and j!=k and i!=k):
#                     print(c[i], c[j], c[k])

# c=[1,2,3]
# i=0
# while i<len(c):
#     j=0
#     while j<len(c):
#         k=0
#         while k<len(c):
#             if (i!=j and j!=k and i!=k):
#                     print(c[i], c[j], c[k])
#             k+=1
#         j+=1
#     i+=1

# "diffrence between elsement"
# j=[2,45,56,78,98,65,9]
# i=1
# a=[]
# k=0
# while i<len(j):
#     c=j[i]-j[k]
#     a.append(c)
#     i+=1
#     k+=1
# print(a)


# a=[1,2,2,3,4,4]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=1
#     while j<len(a):
#         if a[i]==a[j] and i!=j:
#             c+=1
#         j+=1
#     if c>=2:
#        pass
#     else:
#         b.append(a[i])
#     i+=1
# print(b)



# "without len function"
# a=[1,2,3,4,5,4,8]
# count=0
# for i in a:
#     count+=1
# print(count)

# a=[1,2,3,4,5,6,7,8,9,8]
# i=0
# count=1
# while i<len(a):
#     if a[i]==count and a[i]!=count:
#         count+=1
#     count==4
#     i+=1
# print(count)

# a=[1,2,3,4,5]
# print(a[2:6])
# print(a[:])
# print(a[:6])
# print(a[2:])
# print(a[-4:-2])
# print(a[-1:])
# print(a[:-3])
# print(a[-4:])
# print(a[:-1])
# print(a[:9])


# "list constructor in python"

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# MONA=list((1,2,3,4,5,6))
# print(MONA)


# a=[1,2,3,4.0,0.5,6,"mona"]
# b=[2,3,4,5,6,7]
# a.extend(b)
# print(a)

# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i],a[j],a[k])
#             k+=1
    #     j+=1
    # i+=1
# a=[1,2,2,3,5,5,6]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)

"interview question, max,length,sum,multiply"

# a=[[1,2,3,4],[5,6],[3,4,5],[1,2,3,4,5,6,7,5,6],[6,4,5],[8]]
# sum=0
# mul=1
# i=0
# while i<len(a):
#     min=len(a[i])
#     j=0
#     while j<len(a):
#         if len(a[j])<min:
#             min=len(a[j])
#         j+=1
#     if len(a[i])==min:
#         print(a[i],"min len",min)
#     i+=1
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if len(a[i])==min:
#             sum=sum+a[i][j]
#             mul*=a[i][j]
#         j+=1
#     i+=1
# print("minimum list sum",sum)
# print("minimum list multiply",mul)
# i=0
# while i<len(a):
#     max=len(a[i])
#     j=0
#     while j<len(a):
#         if len(a[j])>max:
#             max=len(a[j])
#         j+=1
#     if len(a[i])==max:
#         print(a[i],max)
#     i+=1   
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if len(a[i])==max:
#             sum=sum+a[i][j]
#             mul*=a[i][j]
#         j+=1
#     i+=1
# print("maximum list sum",sum)
# print("minimum list multiply",mul)

"show zero in last"
a=[0,2,0,3,4,0,0,9,0]
i=0
b=[]
c=0
while i<len(a):
    if a[i]>0:
        b.append(a[i])
    elif a[i]<=0:
        c+=1
    i+=1
b.append(c)
j=0
while j<c:
    b.append(0)
    j+=1
print(b)

# "negative number ki jgh par zero"
# a=[-2,8,6,-4,8,-2,-3,8,7,-4]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)

# "her 4th index per 20 chahiye"
# a=[1,2,3,4,5,6,5,43,32,2,1,]
# i=0
# b=[]
# while i<len(a):
#     if i%4==0:
#         b.append(20)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)

# "nested list sum"
# a=[1,2,[3,4,5],[6,7,8]]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#                 sum+=a[i][j]
#                 j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)
# a=["eleven","twelve","thirteen","fourteen"]
# num=input("enter the number")
# i=0
# while i<len(num):
#     k=int(num[i])
#     print(a[k])
#     i+=1


# a="my name is monika"
# c=[]
# b=""
# m=0
# for i in a:
#     if i==" ":
#         c.append(b)
#     else:
#         m+=1
# c.append(m)
# count=0
# for i in c:
#     count+=1
# print(count)
    
    

a=[1,2,3,4,5]


