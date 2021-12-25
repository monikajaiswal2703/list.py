# a=[2,6,5,4,3,8,7]
# i=0
# mult=1
# while i<len(a):
#     mult*=a[i]
#     i+=1
#     print(mult)

a=[[1,2,3,4],[7,6,5,4],[2,3,4,5]]
i=0
while i<len(a):
    multy=1
    j=0
    while j<len(a[i]):
        multy*=a[0][j]
        j+=1
    i+=1
print(multy)

