from random import shuffle


def calculate_p(deck: list):
    p = 0
    past_card = -1
    for card in deck:
        if card == past_card:
            p += 1
        past_card = card

    return p


if __name__ == '__main__':
    M = 4
    N = 13
    default_cards = list(range(M)) * N  # The numbers are suit_ids
    shuffle(default_cards)
    print("P for a random normal deck is:", calculate_p(default_cards))
