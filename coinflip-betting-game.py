logo="""
░█████╗░░█████╗░██╗███╗░░██╗███████╗██╗░░░░░██╗██████╗░
██╔══██╗██╔══██╗██║████╗░██║██╔════╝██║░░░░░██║██╔══██╗
██║░░╚═╝██║░░██║██║██╔██╗██║█████╗░░██║░░░░░██║██████╔╝
██║░░██╗██║░░██║██║██║╚████║██╔══╝░░██║░░░░░██║██╔═══╝░
╚█████╔╝╚█████╔╝██║██║░╚███║██║░░░░░███████╗██║██║░░░░░
░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░"""
print(logo)
import random

# Set the initial number of coins
num_coins = 1000

print("Welcome to the coin betting game! You have", num_coins, "coins to start.")

while num_coins > 0:
    bet = input("Enter your bet (or 'quit' to end the game): ")
    if bet.lower() == 'quit':
        break
    elif not bet.isdigit():
        print("Invalid input! Please enter a positive integer bet.")
    else:
        bet = int(bet)
        if bet > num_coins:
            print("You do not have enough coins to make that bet! You have", num_coins, "coins left.")
        else:
            coin = random.randint(0, 1)
            if coin == 0:
                print("You lost! The coin came up tails.")
                num_coins -= bet
            else:
                print("You won! The coin came up heads.")
                num_coins -= bet
                num_coins += bet * 2
            print("You now have", num_coins, "coins.")

print("Game over! You ended with", num_coins, "coins.")
