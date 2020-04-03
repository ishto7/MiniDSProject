import statistics

from numpy import random

BIG_N = 10 ** 5


def create_p_pool(M, N):
    card_deck = list(range(M)) * N  # The numbers are suit_ids
    p_pool = []
    for _ in range(BIG_N):
        random.shuffle(card_deck)
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


def sub_question_1_and_2(p_pool: list):
    p_bar = statistics.mean(p_pool)
    print("SQ1:", p_bar)
    print("SQ2:", statistics.stdev(p_pool, p_bar))


def sub_question_3_and_4(p_pool: list):
    p_bar = statistics.mean(p_pool)
    print("SQ3:", p_bar)
    print("SQ4:", statistics.stdev(p_pool, p_bar))


def sub_question_5_and_6(p_pool: list):
    p_pool.sort(reverse=True)
    try:
        bigger_than_6 = p_pool.index(6)
    except ValueError:
        bigger_than_6 = len(p_pool)
        print("Didn't found 6 in pool, falling back to default. Use bigger BIG_N")
    try:
        bigger_than_12 = p_pool.index(12)
    except ValueError:
        bigger_than_12 = len(p_pool)
        print("Didn't found 12 in pool, falling back to default. Use bigger BIG_N")

    print("Conditional probability:", bigger_than_12 / bigger_than_6)


if __name__ == '__main__':
    pool_2_26 = create_p_pool(2, 26)
    pool_4_52 = create_p_pool(4, 52)
    sub_question_1_and_2(pool_2_26)
    sub_question_3_and_4(pool_4_52)
    sub_question_5_and_6(pool_2_26)
    sub_question_5_and_6(pool_4_52)
