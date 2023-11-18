import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate and return the total value of a hand of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack (ace + 10-value card)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert ace from 11 to 1
    return sum(cards)

def compare(player_score, dealer_score):
    """Compare the player's and dealer's scores and determine the winner."""
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack!"
    elif player_score == 0:
        return "You win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        player_cards = [deal_card() for _ in range(2)]
        dealer_cards = [deal_card() for _ in range(2)]
        is_game_over = False

        while not is_game_over:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")

            if player_score == 0 or dealer_score == 0 or player_score > 21:
                is_game_over = True
            else:
                should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
                while should_continue not in ['y', 'n']:
                    should_continue = input("Invalid input. Type 'y' to get another card, 'n' to pass: ").lower()
                if should_continue == 'y':
                    player_cards.append(deal_card())
                else:
                    is_game_over = True

        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print(compare(player_score, dealer_score))

        play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("Invalid input. Type 'y' for yes, 'n' for no: ").lower()
        if play_again != 'y':
            break

# Run the game
play_game()
