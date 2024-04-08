import random

def roll():
    roll = random.randint(1,6)
    return roll

player1_name = input("Player 1 Name: ")
player1_bet = float(input(f"Player 1 Bet: "))

player2_name = input("Player 2 Name: ")
player2_bet = float(input(f"player 2 Bet: "))

player1_win = 0
player2_win = 0

for round_no in range(1,4):
    print(f"\nRound#{round_no}")
    player1_val = roll()
    player2_val = roll()
    
    print(f"{player1_name} rolled: {player1_val}")
    print(f"{player2_name} rolled: {player2_val}")

    if player1_val > player2_val:
        player1_win += 1
    elif player2_val > player1_val:
        player2_win += 1
    else:
        print("It's a Tie") 
        
        
if player1_win > player2_win:
    print(f"**********\n{player1_name} WINS")               
elif player2_win > player1_win:
    print(f"**********\n{player2_name} WINS")               
else:
    print("\n**********\nTIE GAME")               