import random

playing = True

# Label 
print("###############################################")
print("#           ROCK, PAPER AND SCISSOR           #")
print("###############################################")

#computer choice
options = ("rock", "paper", "scissors")


while playing:
    computer_choice = random.choice(options)
    while True:
        user_choice = input("Enter your choice (rock, paper and scissors): ").lower()
        if(options.count(user_choice) == 0):
            print("You have to choose rock, paper, scissors!!!")
        else:
            break

    # Game decision
    if(computer_choice==user_choice):
        print("Draw!!")
    elif(computer_choice=="rock" and user_choice=="scissors"):
        print("You Loss")
    elif(computer_choice=="scissors" and user_choice=="paper"):
        print("You Loss!!")
    elif(computer_choice=="paper" and user_choice=="rock"):
        print("You Loss!!")
    else:
        print("You Win!!")
        
        
    while True:
        play = input("Do You want to play (y for yes or n for no)?:").lower()
        if (play=="y"):
            playing=True
            break
        elif (play=="n"):
            playing=False
            break
        else: 
            pass
    
    
    
    
