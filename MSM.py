import random
options=-1,0,1;
player_choice=int(input("Enter your choice: type -1 for Mosquito,0 for Spray,1 for Man"))
computer_choice=random.choice(options)
print("Computer choose:")
print(computer_choice)
if computer_choice == player_choice:
    print("Draw")
elif player_choice == -1 and computer_choice == 0:
    print("You Lose")
elif player_choice ==0 and  computer_choice == 1:
    print("You lose") 
elif computer_choice == -1 and player_choice == 1:
    print("You lose")  
elif player_choice == 0 and computer_choice ==-1:
    print("You win")
elif player_choice ==-1 and computer_choice == 1:
    print("You win")
elif player_choice == 1 and computer_choice  ==  0:
    print("You win")