"count of even and odd"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
while i<len(elements):
    if (elements[i]%2)==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print("even",even_count)
print("odd",odd_count)



"sum of even and odd"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
while i<len(elements):
    if (elements[i]%2)==0:
        even_count+=elements[i]
    else:
        odd_count+=elements[i]
    i+=1
print("even",even_count)
print("odd",odd_count)



"average of even and odd"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
while i<len(elements):
    if (elements[i]%2)==0:
        even_count+=elements[i]
        avg=even_count// 4
    else:
        odd_count+=elements[i]
        avg1=odd_count//7
    i+=1
print("even averag",avg)
print("odd",avg1)
