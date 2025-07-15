import random

game_over = True

while game_over:
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    dealer = []
    player = []

    def dealer_draw():
        dealer.append(random.choice(cards))
        wildcard(dealer)

    def player_draw():
        player.append(random.choice(cards))
        wildcard(player)

    def wildcard(name):
        for n in range(len(name)):
            if name[n] == 11 and sum(name) > 21:
                name[n] = 1

    print(logo)
    player_draw()
    player_draw()
    dealer_draw()
    print(f"player hand = {player} = {sum(player)}")
    print(f"dealer hand = {dealer} = {sum(dealer)}")
    if sum(player) == (21):
        n = "n"
        print("Blackjack! You WIN!")
        x = False
    else:
        n = input("Draw Again? 'y' or 'n'\n\n ")
        x = True

    while n == "y":
        player_draw()
        print(f"player hand = {player} = {sum(player)}")
        if sum(player) == (21):
            n = "n"
            print("Blackjack! You WIN!")
            x = False
        if sum(player) > (21):
            n = "n"
            print("Bust!")
        else:
            n = input("Draw Again? 'y' or 'n'\n\n")

    while x:
        if sum(dealer) < (17):
            dealer_draw()
        elif sum(dealer) > (21):
            x = False
        elif sum(dealer) < sum(player) and sum(dealer) < (21):
            if sum(player) > (21):
                if sum(dealer) < (17):
                    dealer_draw()
                else:
                    x = False
            else:
                dealer_draw()
        elif sum(dealer) > sum(player):
            x = False
        else:
            x = False

    print(f"dealer hand = {dealer} = {sum(dealer)}")
    print(f"dealer hand = {sum(dealer)}")

    if sum(player) == (21) and sum(dealer) != int(21):
        print("Win")
    elif sum(dealer) < sum(player) <= (21):
        print("Win")
    elif sum(dealer) == sum(player) <= (21):
        print("Draw")
    elif sum(player) < sum(dealer) <= (21):
        print("Lose")
    elif sum(player) > (21):
        print("Lose")
    elif sum(dealer) > (21):
        print("Win")

    if input("Would you like to play again?: 'y' or 'n' ") == "y":
        game_over = True
    else:
        game_over = False
