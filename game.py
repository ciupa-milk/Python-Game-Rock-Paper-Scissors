import random, time
x =5
print("Chose: rock, paper, scissors")

def your_choice():
    choises = ["rock", "paper", "scissors"]
    time.sleep(0.8)
    player_choice = str(input("Your choice: "))
    computer_choice = str(random.choice(choises))

    while True:
        if player_choice in choises:
            break
        else:
            print("CHOSE ROCK OR SCISSORS OR PAPER")
            player_choice = str(input("Your choice: "))

    #s > p, p > r, r > s
    time.sleep(0.8)
    print(f"Computer choice: {computer_choice}")

    if computer_choice == player_choice:
        print("Tie!")
        exit()
    elif computer_choice == "rock" and player_choice == "paper" or computer_choice == "paper" and player_choice == "scissors" or \
            computer_choice == "scissors" and player_choice == "rock":
        print("U won")
        exit()
    elif player_choice == "rock" and computer_choice == "paper" or player_choice == "paper" and computer_choice == "scissors" or \
        player_choice == "scissors" and computer_choice == "rock":
        print("U nab, computer won")

your_choice()
