import random


def check_win_lose(chosen):
    win = random.randint(1, 30)
    return chosen == win
