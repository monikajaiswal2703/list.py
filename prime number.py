# b=[]
# mylist=[5,6,3,8,13,15,17,19]
# a=len(mylist)
# for i in range(0,a):
#     c=0
#     for j in range (2,mylist[i]):
#         if mylist[i]%j==0:
#             c=1
#     if c==0:
#         b. append(mylist)
#         print(mylist[i],"is prime number")
#     else:
        # print(mylist[i],"is not prime number")

# s=int(input("enter the start no."))
# e=int(input("enter the end no."))
# for i in range (s,e,+1):
#     a=0
#     for j in range (2,i):
#         if(i%j==0):
#             a=1
#     if (a==0):
#         print(i,end="  ")
# print("prime number in range",s, "to",e)
prime_num=[]
num = 1
while(num <= 100):
    count = 0
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            count = count + 1
        i = i + 1
    if (count == 0 and num!= 1):
     prime_num.append(num)
    num+=1
print(prime_num)
    

