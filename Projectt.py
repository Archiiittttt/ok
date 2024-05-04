import random

def multiplayer_cricket():
    print("Welcome to the Multiplayer Cricket Game!")
    
    num_players = int(input("Enter the number of participants: "))
    
    players = []
    for i in range(1, num_players + 1):
        player_name = input(f"Enter name for player {i}: ")
        players.append((player_name, 0))

    for i, (player_name, _) in enumerate(players):
        print(f"\n{player_name}, get ready to bat!")
        while True:
            user_input = int(input(f"Your turn: Enter your number between 0 and 6: "))
            if user_input < 0 or user_input > 6:
                print("Invalid number! Please enter a number between 0 and 6.")
                continue
            
            comp_input = random.randint(0, 6)
            print(f"Computer's number: {comp_input}")
            
            if user_input == comp_input:
                print("You're out!")
                break
            else:
                players[i] = (player_name, players[i][1] + user_input)
                print(f"Your current score: {players[i][1]}")

    print("\nGame Over!")
    print("Final Scores:")
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    for i, (player_name, player_score) in enumerate(sorted_players):
        print(f"{i+1}. {player_name}: {player_score}")
    
    print(f"\nWinner: {sorted_players[0][0]}")

def player_vs_computer_cricket():
    print("Welcome to the Player vs Computer Cricket Game!")

    import random

    def toss():
        user_choice = input("Do you want to choose odd or even? ").lower()
        while user_choice not in ['odd', 'even']:
            print("Invalid choice! Please choose 'odd' or 'even'.")
            user_choice = input("Do you want to choose odd or even? ").lower()
        
        user_number = int(input("Enter your number between 0 and 6: "))
        while user_number < 0 or user_number > 6:
            print("Invalid number! Please enter a number between 0 and 6.")
            user_number = int(input("Enter your number between 0 and 6: "))

        comp_number = random.randint(0, 6)
        print(f"Computer chose {comp_number}.")
        
        total = user_number + comp_number
        print(f"Total: {total}")

        if (total % 2 == 0 and user_choice == 'even') or (total % 2 != 0 and user_choice == 'odd'):
            print("You won the toss!")
            return "user"
        else:
            print("Computer won the toss!")
            return "computer"

    def cricket_game(decision):
        if decision == "user":
            print("\nYou won the toss!")
            bat_or_bowl = input("Do you want to bat or bowl? (bat/bowl): ")
        else:
            print("\nComputer won the toss!")
            bat_or_bowl = random.choice(["bat", "bowl"])
            print(f"Computer chose to {bat_or_bowl}.")

        while True:
            comp_score = 0
            you_score = 0
            chasing = False

            if bat_or_bowl == "bat":
                print("\nYou are batting...")
                while True:
                    user_input = int(input("Your turn: Enter your number (0-6): "))
                    comp_input = random.randint(0, 6)
                    print(f"Computer's number: {comp_input}")
                    if user_input == comp_input:
                        print("You're out!")
                        break
                    else:
                        you_score += user_input
                        print(f"Your current score: {you_score}")
                        if chasing and you_score > comp_score:
                            print("Your score surpassed the computer's score!")
                            print("You win!")
                            return

                print(f"\nYour final score: {you_score}")
                print(f"Computer's target: {you_score + 1}")

                print("\nComputer is batting...")
                while True:
                    comp_input = random.randint(0, 6)
                    user_input = int(input("Your turn: Enter your number (0-6): "))
                    print(f"Computer's number: {comp_input}")
                    if user_input == comp_input:
                        print("Computer is out!")
                        break
                    else:
                        comp_score += comp_input
                        print(f"Computer's current score: {comp_score}")
                        if comp_score > you_score:
                            print("Computer's score surpassed your score!")
                            print("Computer wins!")
                            return

                print(f"\nComputer's final score: {comp_score}")

            else:
                print("\nComputer is batting...")
                while True:
                    comp_input = random.randint(0, 6)
                    user_input = int(input("Your turn: Enter your number (0-6): "))
                    print(f"Computer's number: {comp_input}")
                    if user_input == comp_input:
                        print("Computer is out!")
                        break
                    else:
                        comp_score += comp_input
                        print(f"Computer's current score: {comp_score}")
                        if chasing and comp_score > you_score:
                            print("Computer's score surpassed your score!")
                            print("Computer wins!")
                            return

                print(f"\nComputer's final score: {comp_score}")
                print(f"Your target: {comp_score + 1}")

                print("\nYou are batting...")
                while True:
                    user_input = int(input("Your turn: Enter your number (0-6): "))
                    comp_input = random.randint(0, 6)
                    print(f"Computer's number: {comp_input}")
                    if user_input == comp_input:
                        print("You're out!")
                        break
                    else:
                        you_score += user_input
                        print(f"Your current score: {you_score}")
                        if you_score > comp_score:
                            print("Your score surpassed the computer's score!")
                            print("You win!")
                            return

                print(f"\nYour final score: {you_score}")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                print("Thanks for playing. Goodbye!")
                break

    print("Welcome to the Cricket game!")

    while True:
        decision = toss()
        cricket_game(decision)
        quit_game = input("Do you want to quit the game? (yes/no): ")
        if quit_game.lower() == 'yes':
            break


def main():
    while True:
        print("\nMenu:")
        print("1. Multiplayer Cricket")
        print("2. Player vs Computer Cricket")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            multiplayer_cricket()
        elif choice == '2':
            player_vs_computer_cricket()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
