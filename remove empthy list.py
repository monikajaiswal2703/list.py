
# l = ['A', 'B', '', 'C', '', 'D']
# l= list(filter(len, l))
# print(l) 

#    
# l = ['A', 'B', '', 'C', '', 'D']
# l = [s for s in l if s]
# print(l)  
 
list_1 = ["", 'A', "red", 3, ""]
while ("" in list_1):
    list_1.remove("")
print("After removing spaces: ",list_1)

