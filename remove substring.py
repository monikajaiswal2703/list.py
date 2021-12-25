mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b=mainStr.split()
subStr = "over"
a=0
sub_len=len(b)

for i in range(len(mainStr)):
    if (mainStr[i:i+sub_len]==b):
     a+=1
print(subStr,sub_len,i)




# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# a=mainStr.split()
# c='over'
# i=0
# b=[]
# while i<len(a):
#     if a[i]==c:
#         pass
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# a="over"
# c="on"
# str1=mainStr.replace(a,c)
# print(str1)
