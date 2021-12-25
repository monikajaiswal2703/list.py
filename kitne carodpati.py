kitna_paisa_hai = [3000, 600000, 324990909,
 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
k=0
l=0
d=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000: 
        k+=1
    elif kitna_paisa_hai[i]>=100000: 
        l+=1
    else:
        d+=1
    i+=1
print("carorpati",k)
print("lakhpati",l)
print("dilwale",d)