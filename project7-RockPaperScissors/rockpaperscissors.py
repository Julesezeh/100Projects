import time
import random

def main():
    print()
    print("______________________________ROCK, PAPER, SCISSORS___________________________")
    print()
    print( " By Jules Okoye-ezeh")
    time.sleep(1)
    print("""
THE RULES ARE SIMPLE...
- Rock crushes scissors.\n
- Paper covers rock.\n
- Scissors shred paper. 
    """)
    time.sleep(3)

    print("\n   PRESS CTRL+C TO END THE GAME AT ANY TIME..\n")
    user_scores={'wins':0,'losses':0,'draws':0,}
    time.sleep(2)
    print(" Have Fun:)\n")
    time.sleep(2)
    while True:    
        #Getting a valid number of rounds from the user
        while True:
            rounds = input(' How many times should we go? ')
            try:
                rounds = int(rounds)
                time.sleep(1)
                print(f"\n COOL!, best {(rounds//2)+1} out of {rounds} ;)\n")
                break
            except:
                print(" Invalid Input. Please enter a valid number")
                print()

        moves = ['R','P','S']

        for x in range(rounds):
            
            time.sleep(2)
            print(f"       Round {x+1}")

            #Get the player's move
            print("\n Your Move: Rock(R),Paper(P), or Scissors(S) ")
            while True:
                move = input(":> ").upper()
                if move not in moves:
                    print("\n Please enter a valid choice (rock (R),paper (P) or scissors (S))")
                else:
                    break

            #Get the computer's move after the little delay
            time.sleep(0.5)
            computers_move = random.choice(moves)
            match computers_move:
                case 'P':
                    print(f"\n I choose Paper")
                case 'R':
                    print(f"\n I choose Rock")
                case 'S':
                    print(f"\n I choose Scissors")
                    
            if (move == 'P' and computers_move == 'R') or (move=='R' and computers_move == 'S') or (move=='S' and computers_move=='P'):
                user_scores['wins']+=1
                print('\n You win this round !!')
            elif move==computers_move:
                user_scores['draws']+=1
                print("\n That's a drawwww")
            else:
                user_scores['losses']+=1
                print('\n You lose this round :(')
        print("\n\n   FINAL SCORES")
        print(f"    YOU WON: {user_scores['wins']} TIMES\n   YOU LOST: {user_scores['losses']} TIMES\n    WE DREW: {user_scores['draws']} TIMES")
        
        ask = input("\n Want to play again (Y) or (N) ?")
        if ask.upper()=='N':
            break

if __name__ == "__main__":
    main()