list = [1, 3, 4, 1, 3, 4, 5, 6, 5, 3, 4, 6, 6, 2, 4]
i=0
d=[]
while i<len(list):
    j=0
    n=[]
    count=0
    while j<len(list):
        if list[i] in list:
            if list[i]==list[j]:
                count+=1
        j+=1
    n.append(list[i])
    n.append(count)
    if n not in d:
        d.append(n)
    i+=1
print(d)