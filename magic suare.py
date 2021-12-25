# a=[[1,2,3,4],
#   [5,6,7,8,],
#   [44,55,77,88],
#   [9,8,7,6,]]
# primary_daigonal=0
# for i in range (len(a)):
#     for j in range (len(a[i])):
#         if j==i:
#             print(a[i][j])
#             primary_daigonal=primary_daigonal+(a[i][j])
# print(primary_daigonal)

a=[[1,2,9,4],
  [4,3,5,1],
  [4,7,4,3],
  [5,6,1,2]]
i=0
while i<len(a):
  j=0
  sum=0
  while j<len(a):
    sum=sum+a[i][j]
    j+=1
  i+=1
  print(sum)
i=0
while i<len(a):
  j=0
  sum2=0
  while j<len(a[i]):    
    sum2+=a[i][j]  
    j+=1
  i+=1
  print(sum2)  


