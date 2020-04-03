from random import shuffle
import statistics

BIG_N = 10 ** 5


def create_p_pool(M, N):
    card_deck = list(range(M)) * N  # The numbers are suit_ids
    p_pool = []
    for _ in range(BIG_N):
        shuffle(card_deck)
        p_pool.append(calculate_p(card_deck))
    return p_pool


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
    p_pool = create_p_pool(M, N)
    p_bar = statistics.mean(p_pool)
    print("Mean of P:", p_bar)
    print("STdev of P:", statistics.stdev(p_pool, p_bar))
