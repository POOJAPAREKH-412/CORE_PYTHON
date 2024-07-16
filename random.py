import random

#print(random. randint(1,100))
#l=[1,2,10,20,"tops","tech","python",true,false,100,200]
#print(random.choice(l))

num=random.randint(1,20)

while True:
    guess=int(input("guess a number between 1 to 20: "))
    if guess==num:
        print("you guess a correct number.")
        break
    elif guess>num:
        print("you guess a greater number.")
    elif guess<num:
        print("you guess a smaller number.")
