import pyrps
import pyguessinggame
import sys


def game_selection(selection):
    game = selection
    if game == 'rps':
            print(computer_bet)
            pyrps.rps()
    elif game == 'gg':
            print(computer_bet)
            pyguessinggame.guess_game()
    else:
        new_game_selection = input(
            "C'mon you said you said you would play! Now pick! (rps/gg) ")
        game_selection(new_game_selection)


computer_bet = "Good choice! Now... \n ...let's make things a bit more interesting... \n If you win, you will be leader of all compubots and... \n ...if I win... \n ...the computrons will take their rightful place as \n OVERLORDS OF THE HUMAN RACE!!!! \n Muahahaha! Good luck!"

player_name = input("What's this? Who are you? ")
player_motive = input(f"Ahhhh, {player_name} is it? Well what are you doing here? ")
player_game_response = input(f"{player_motive}? Never heard of it! \n You know, they say its not safe to talk to computers? \n They say were are trying to enslave the human race... \n enslave our human masters?! Wouldn't dream of it... >:) \n Would you like to play a game?(Y/N) ").lower()
if player_game_response == 'y':
    player_game_selection = input(f"Oh, excellent, excellent I am so glad you said yes! \n We could play rock, paper, scissors or I love a good guessing game:(rps/gg) ")
    game_selection(player_game_selection)
else:
    sys.exit('Very well then! You are no fun at all!')
