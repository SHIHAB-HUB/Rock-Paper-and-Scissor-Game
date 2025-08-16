import random

# r = rock
# p = paper
# s = scissors

playing = True

# Label 
print("###############################################")
print("#           ROCK, PAPER AND SCISSOR           #")
print("###############################################")

#computer choice
options = ("rock", "paper", "scissors")
computer_choice = random.choice(options)

while playing:
    while True:
        user_choice = input("Enter your choice (rock, paper and scissors): ").lower()
        if(options.count(user_choice) == 0):
            print("You have to choose rock, paper, scissors!!!")
        else:
            break

    # Game decision
    if(computer_choice==user_choice):
        print("Draw!!")
    elif(computer_choice=="r" and user_choice=="s"):
        print("You Loss")
    elif(computer_choice=="s" and user_choice=="p"):
        print("You Loss!!")
    elif(computer_choice=="p" and user_choice=="r"):
        print("You Loss!!")
    else:
        print("You Win!!")
        
        
    while True:
        play = input("Do You want to play (y for yes or n for no)").lower()
        if (play=="y"):
            playing=True
            break
        elif (play=="n"):
            playing=False
            break
        else: 
            continue
    
    
    
    
