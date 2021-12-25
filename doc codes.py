# i=0
# b=[]
# while i<10:
#     num=int(input("enter the number"))
#     b.append(num)
#     i+=1
# print(b)


# i=0
# b=[]
# while i<10:
#     num=int(input("enter the number"))
#     b.append(num)
#     i+=1
# print(b)
# num1=int(input("enter the number"))
# if num1 in b:
#     print("yes")
# else:
#     print("no")

# ""take 20 user inputTake 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.""
# i = 0
# a = []
# while i<20:
#   num= int(input("Enter number:="))
#   a.append(num)
#   i = i+1
# print(a)
# odd = []
# even = []
# zero = []
# positive = []
# negative = []
# i = 0
# while i<len(a):
#     if a[i]==0:
#       b=a[i]
#       zero.append(b)
#     if a[i] >= 0:
#         c=a[i]
#         positive.append(c)
#     if a[i]%2 == 0:
#       e = a[i]
#       even.append(e)
#     if a[i]%2 !=0:
#         od=a[i]
#         odd.append(od)
#     if a[i]<0:
#        neg=a[i]
#        negative.append(neg)
#     i = i+1
# print ("zero=",zero)
# print("positive number=",positive)
# print("even number",even)
# print("odd number",odd)
# print("negative number", negative)



4.
# Take 10 integer inputs from user and store them in a list. Now, copy all the
#  elements in another list but in reverse order.

# i = 10
# a = []
# while i>0:
#   num=int(input("Enter number:-"))
#   a.append(num)
#   i = i-1
#   b=a
# print(b)
# print (a[::-1])


# Find largest and smallest elements of a list.
# a = [2,312,123,3,12,23,12,12]
# largest = a[0]
# i = 0
# while i<len(a):
#   if a[i]>largest:
#     largest = a[i]
#   i = i+1
# print (largest)


# a = [2,312,123,3,12,23,12,12]
# smalle = a[0]
# i = 0
# while i<len(a):
#   if a[i]<smalle:
#     smalle = a[i]
#   i = i+1
# print (smalle)


# "Write a program to find the product of all elements of a list"
# a=[5,10,15,25,2,33,4,44]
# mlty=1
# i=0
# while i<len(a):
#     mlty*=a[i]
#     print(mlty)
#     i+=1


# "Write a program to check if elements of a list are same or not it read from front or back. E.g.-"
# 2 	3 	15 	15 	3 	2

# a = [1,2,3,3,2,1]
# i = 0
# mid = (len(a))/2
# same = True
# while i<mid:
#   if a[i] == a[len(a)-i-1]:
#      print ("No")
#      same = False
#     # break
#   i = i+1
# if same == True:
#       print ("Yes")


# num = [2, 3, 4], [5, 6, 7]
# num2 = [8, 9, 10], [11, 12, 13]
# num3 = [0, 0, 0], [0, 0, 0]
# for i in range(len(num)):
#     print(num[i])
# for i in range(len(num)):
#     print(num2[i])
# print()
# for i in range (len(num)):
    # for j in range(len(num)+1):
    #     num3[i][j] = num[i][j] + num2[i][j]

# for i in range(len(num3)):
#     print(num3[i])
#     print(num2[i][j])