import random

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "J": 10,
    "Q": 10,
    "K": 10
}

game_on = True


def black_jack():
    global sum_player
    global sum_computer
    sum_player = 0
    sum_computer = 0
    count = 0
    choices = list(cards.keys())
    player_card = random.choice(choices)
    print(player_card)
    if count <= 0:
        player_card2 = random.choice(choices)
        print(player_card2)
        sum_player = cards[player_card] + cards[player_card2]
        count = 1
    else:
        sum_player += cards[player_card]
    computer_card = random.choice(choices)
    sum_computer = cards[computer_card]

    return f'Your total is {sum_player} and the dealer has {sum_computer}'


while game_on:
    print(black_jack())
    cont = input("Y or N for continuing or stoping")
    if cont == "Y":
        black_jack()
        if sum_player > 21:
            print("Player LOST")
        elif sum_player == 21:
            print("BlackJack player wins")
        elif sum_player > sum_computer:
            print("Players wins")
        else:
            print(sum_computer)
            print('Dealer wins')
    else:
        game_on = False
        computer_card = random.choice(list(cards.keys()))
        sum_computer += cards[computer_card]
        if sum_computer > 21:
            print("Dealer LOST")
        elif sum_computer == 21:
            print("BlackJack dealer wins")
        elif sum_player > sum_computer:
            print("Players wins")
        else:
            print(sum_computer)
            print('Dealer wins')


