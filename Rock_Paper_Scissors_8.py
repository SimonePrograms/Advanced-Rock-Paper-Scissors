# Using Parsers

import sys #for sys.exit instead of print
import random
from enum import Enum

def rps(name):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum): #assigning numbers to words
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, or\n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice) # cast string to integer

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}."
              )
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
              )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == computer:
                return"🤝 You Tie!\n"
            else:
                python_wins += 1
                return f" 🐍Python wins!\n Sorry, {name}..."
        
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nN for No to quit.\n\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "Y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit(f"\nBye {name}!")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Gives a personalised game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors() #ready to be imported into a different file