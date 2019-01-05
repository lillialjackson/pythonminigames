import random
import sys

def guess_game ():
    rand_low = 1
    rand_high = 10
    rand_num = random.randint(rand_low,rand_high)
    win_count = 0

    while True:
        player_guess = int(input(f"Guess a number between {rand_low} and {rand_high}: "))
        if player_guess < rand_low or player_guess > rand_high:
            print("What's the matter with you? Do you not know the numbers?...humans...I said...")
        elif player_guess > rand_num:
            print("Too high!")
        elif player_guess < rand_num:
            print("Too lowowow!!!")

        else:
            print("Damn you! You guessed it! Who taught you binary search?!")
            win_count += 1
            play_response = input("Try again puny minded human?(y/n) ").lower()

            if play_response == 'y':
                print(win_count)
                if win_count < 2:
                    rand_high = 20
                elif win_count < 3:
                    rand_high = 35
                elif win_count < 4:
                    rand_high = 50
                elif win_count < 5:
                    rand_high = 75
                else:
                    rand_high = 100
                rand_num = random.randint(rand_low,rand_high)
            else:
                    sys.exit("I know we'll be seeing each other again!")
