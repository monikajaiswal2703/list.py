# marks=[[78,76,94,86,88],
#        [91,71,98,65,76],
#        [95,45,78,52,49]]
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         avg=sum//5
#         j+=1
#     print("average of year",avg)
#     sum=sum-sum
#     i+=1


marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j+=1
        avg=sum//len(marks[i])
    print("average of year",avg)
    sum=sum-sum
    i+=1
    