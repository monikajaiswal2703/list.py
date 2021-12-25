a=[[1,2],[3,4],[4,6],[7,8],[9,5]]
# print(a[0]+a[1]+a[2]+a[3]+a[4])
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
print(b)
