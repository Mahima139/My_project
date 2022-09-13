import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose!", computer, 'covers', player)
            cpu_score+=1
        else:
            print("you win!", player, "smashes", computer)
            player+=1
    elif player == "Paper":
        if computer == "Rock":
            print("you win!", player, "covers", computer)
            player+=1
        else :
            print("you lose!", computer, "cut", player)
            cpu_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("you lose!", computer, "smashes", player)
            cpu_score+=1
        else :
            print("you win!", player, "cut", computer)
            player+=1
    elif player == "End":
        print("Final scores:")
        print(f"CPU:{cpu_score}")
        print(f"PLAYER:{player}")
        break
