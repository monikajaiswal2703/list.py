# str1= [1,2,3,4,5,]
# a=str1[-4]
# print (a)

# a="18"
# b="02"
# c="2020"
# print  (a+"/",b+"/",c)

list1 = [1,2,3,4,5,6]

list2 = [2,3,1,0,6,7]
# print(list1[3:5],"missing is list2", list2)
i=0
a=[]
while i<len(list1):
    h=list1[i]
    if h not in list2:
        a.append(h)
    i+=1
print(a)