
# a=input("enter the string:-")
# b=a[::-1]
# if a==b:
#     print("palindrom hai")
# else:
#     print("not palindrom")


# a=input("enter the string:-")
# i=0
# while i<len(a):
#     b=a[-i-1]
#     i=i+1
#     print(b,"palindrom")

a=input("enter the string:-")
i=0
rev=a[-1::-1]
while i<len(a):
    if rev==a:
        print("palindrom",rev)
        break
    else:
        print("not palindrom",rev)
        break