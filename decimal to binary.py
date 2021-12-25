# decimal=int(input("enter decimal number"))
# num=''
# while decimal >0:
#     num=str(decimal%2)+num
#     decimal//=2
# print(num)




# binary_number = (input("enter the bin. number"))
# i=0
# sum=0
# while i<len(binary_number):
#     a=binary_number[-i-1]
#     sum=sum+(2**i)
#     i=i+1
# print(sum)


binary_number=[1,0,0,1,1,0,1,1]
i=0
sum=0
while i<len(binary_number):
    a=binary_number[-i-1]
    sum=sum+a*(2**i)
    i=i+1
print(sum)