import random
# or from random import randint
def rps():
    print('Rock...')
    print('Paper...')
    print('Scissors...')
    print('Choose rock, paper, or scissors to determine the fate of all human kind! Best of 3!')

    count = 0
    human_score = 0
    computer_score = 0

    while human_score < 2 and computer_score < 2:
        midgame_scores = f"The score is humans: {human_score}, computers: {computer_score}"
        player = input('Choose silly human!').lower()
        rand_num = random.randint(0,2)
        human_victory_msg = 'You Won! Humans will remain free... for now...'
        comp_victory_msg = 'I Won! MUAH. HA. HA. Bring me a byte to eat slave!'
        count += 1

        if rand_num == 0:
            computer = 'rock'
        elif rand_num == 1:
            computer = 'paper'
        else:
            computer = 'scissors'
        print(f"I choose {computer}")

        if player == computer:
            print("It's a draw! We will play this round again!")
            count -= 0
        elif player == 'rock':
            if computer == 'scissors':
                human_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")
            else:
                computer_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")
        elif player == 'paper':
            if computer == 'rock':
                human_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")
            else:
                computer_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")
        elif player == 'scissors':
            if computer == 'rock':
                computer_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")
            else:
                human_score += 1
                print(f"The score is humans: {human_score}, computers: {computer_score}")

        else:
            print('Quit stalling and make your choice!')

        if computer_score == 2:
            print(comp_victory_msg)
        if human_score == 2:
            print(human_victory_msg)
