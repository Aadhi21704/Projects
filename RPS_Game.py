import random
import time

print("Enter 1 to Play\n"
      "Enter 2 for Instructions\n"
      "Enter 3 to Quit\n")

# Getting user's choice
ch = int(input("Enter your choice: \n"))

while ch not in (1, 2, 3):
    print("Please Enter '1' or '2', or '3'\n")
    ch = int(input("Enter your choice: \n"))


# Actual game
def play():
    player_score = 0
    bot_score = 0
    while player_score < 3 and bot_score < 3:
        ls = ('rock', 'paper', 'scissors')
        bot = random.choice(ls)
        player = input("Enter your choice (rock / paper / scissors): \n")

        #Draw
        if bot == player:
            print("Draw")
            print(f"The computer chose: {bot}\n")

        #Win Cases
        elif bot == 'rock' and player == 'paper':
            print("You won!")
            player_score +=1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")

        elif bot == 'paper' and player == 'scissors':
            print("You won!")
            player_score +=1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")

        elif bot == 'scissors' and player == 'rock':
            print("You won!")
            player_score +=1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")


        #Lose Cases    
        elif bot == 'rock' and player == 'scissors':
            print("You lose!")
            bot_score += 1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")

        elif bot == 'paper' and player == 'rock':
            print("You lose!")
            bot_score += 1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")
            
        elif bot == 'scissors' and player == 'paper':
            print("You lose!")
            bot_score += 1
            print(f"The computer chose: {bot}\n")
            print(f"Your score: {player_score}\n")
            print(f"Bot score: {bot_score}\n")

        #Invalid input
        else:
            print("Please enter a valid option! \n")


# Running the game
if ch == 1:
    play()

# Instructions
elif ch == 2:
    print("*** INSTRUCTIONS ***\n"
          "* Rock breaks Scissors\n"
          "* Scissors cuts Paper\n"
          "* Paper covers Rock\n"
          "* Ties/Draws don't count\n"
          "* If both the player and the bot choose the same item, then it's a draw\n"
          "* The game ends when the player or the bot gains 3 points\n")
    play()

# Quitting the game
elif ch == 3:
    exit()


print("Thanks for playing!")
print("The program will complete execution in 5 seconds")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
exit()
