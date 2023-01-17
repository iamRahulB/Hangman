import random
word_list=["Dog","Monkey","Farmer","Man","Rahul"]

choice=random.choice(word_list).lower()
word_random=choice
print(choice)
hypen=[]
word_length=len(choice)
game_end=False
for leng in range(word_length):
        hypen.append("_")

while game_end==False:
    
    
    user_choice=input("Input a letter you want to Guess\n").lower()
    
    
    for position in range(word_length):
        letter=word_random[position]
        if letter==user_choice:
            hypen[position]=letter
    print(hypen)
    if "_" not in hypen:
       game_end=True
       print("won")

