# Slot Machine 🎰
# Codédex
import random

def play():
    symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
    while True:
        results = random.choices(symbols, k=3)
        print(f'{results[0]} | {results[1]} | {results[2]}')
        
        if results[0] == results[1] == results[2]:
            print("YOU WIN A JACKPOT BABY, ENJOY!")
        else:
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.upper() == 'N':
                print("shakalaka")
                break

play()
