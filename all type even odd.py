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
print(" count of even number",even_count)
print(" count of odd number",odd_count)

"count of all number"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
while i<len(elements):
    count+=1
    i+=1
print("count of all numbers",count)

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
print("sum of even number",even_count)
print("sum of odd number",odd_count)
"sum of all numbers"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
while i<len(elements):
    sum+=elements[i]
    i+=1
print("sum of all numbers",sum)

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
print("averag of even number",avg)
print(" averag of odd number",avg1)


"averag of all numbers"
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
while i<len(elements):
    sum+=elements[i]
    avg=sum//11
    i+=1
print("averag of even number",avg)


