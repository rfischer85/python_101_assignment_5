from random import randint

''' The Blackjack Program.
draw cards and obtain the highest total not exceeding 21.
'''
#Declaing variables.
dash = '-'
player_card_1 = 0
player_card_2 = 0
player_total = 0
dealer_card_1 = 0
dealer_card_2 = 0
dealer_total = 0
hit_stand = 'h'
hit_total = 0
game_over = False


# defining a function to pick a random card between 1 and 10
def random_card_picker():
    random_card = randint(1, 10)
    return random_card

# defining a function to pick the current players cards and calculate their total
def game_step_1():
    card_1 = random_card_picker()
    card_2 = random_card_picker()
    total = card_1 + card_2
    return card_1, card_2, total

# defining a function that runs if the player hits.
def hit(hit_total):
    card = random_card_picker()
    hit_total += card
    if busted(hit_total):
        print(f'Hit! You draw the {card} card. Your new total is {hit_total}.\n')
        return hit_total, 'h', False
    else:
        print(f'''\nYou draw the {card} card. Your new total is {hit_total}, you bust.
Game over.''')
        return hit_total, 's', True

# defining a function that runs during the dealers turn
def dealer_turn(hit_total):
    card = random_card_picker()
    hit_total += card
    if busted(hit_total):
        print(f'\nThe dealer hits and draws the {card} card. The dealers total is {hit_total}.')
        return hit_total
    else:
        print(f"\nThe dealer draws the {card} card and it's total is {hit_total}.")
        return hit_total

# defining a function to check if the player has busted.
def busted(total):
    if total <= 21:
        return True
    else:
        return False

# defining a function to determine the winner
def winner(dealer, player):
    if dealer >= player:
        return False
    else:
        return True


# Main program logic
print(f'\nWelcom to Blackjack!')
print(f'{dash:-^50}')

# main while loop.
while True:
    play = input(f'Would you like to start a new game? (y/n): ')
    hit_stand = 'h'
    if play == 'n':
        print(f'Thanks anyways. Goodbye.')
        break
    elif play =='y':
        player_card_1, player_card_2, player_total = game_step_1()
        dealer_card_1, dealer_card_2, dealer_total = game_step_1()
        print(f'\nYou are dealt the {player_card_1} and {player_card_2} cards. Your total is {player_total}.\n')
        print(f'The dealer draws a {dealer_card_1} card and a hidden card.\n')
        while hit_stand == 'h':
            hit_stand = input(f'Would you like to hit or stand? (h/s): ')
            if hit_stand =='s':
                print(f'You Stand.\n')
                continue
            elif hit_stand == 'h':
                player_total, hit_stand, game_over = hit(player_total)
        if game_over:
            break
        print(f'The dealers hidden card is {dealer_card_2} and its total is {dealer_total}.')
        while not game_over:
            if dealer_total >= 17 and dealer_total <= 21:
                print(f'The dealer stands.')
                break
            elif dealer_total < 17:
                dealer_total = dealer_turn(dealer_total)
                continue
            elif dealer_total >= 22:
                print(f'The dealer busts. You win!')
                break
            game_over = winner( dealer_total, player_total)

    else:
        print(f'\nPlease enter "y" to start a new game, or "n" to quit.')
        continue
