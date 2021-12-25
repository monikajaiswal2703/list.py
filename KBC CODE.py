question_list = [
"1)How many continents are there?", 
"2)What is the capital of India?", 
"3)NG mei kaun se course padhaya jaata hai?",
"4)who is first PM of india?",
"5)which is the national vegetable of india?" ]

options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["softwear enginiring💻","counsling", "Tourism", "Agriculture"],
["jawaharlal nehru","rajiv gandhi","gulzarilal nanda","narendra modi"],
["potato","pumpkin","tomato🍅","lady finger"],
]
ops50_50=[["1)four","3)seven"],
["2)bhopal","4) new delhi"],
["1)softwear enginiring💻","2)counsling"],
["1)jawaharlal nehru","3)gulzarilal nanda"],
["4)lady finger","2)pumpkin"]]
ans_list = [3, 4, 1,1,2] 
print("welcome to KBC 🙏💰")
print("lets start the game👍 ")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    if c==0:
        life_line=input("do you want life line🤔? :=")
        if life_line=="yes":
            c+=1
            
            print(ops50_50[i])
            
            s+=10000
    Ans=int(input("enter your option:="))
    if ans_list[i]==Ans:
        print("congrats your answer is correct,you won🤗🥳 ",s,"💰rupees")
        s+=20000
        
    else:
        print(" sadly your answer is wrong😟 ")
        break
    i+=1

