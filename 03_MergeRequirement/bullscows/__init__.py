import random
import textdistance


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = textdistance.hamming.similarity(guess, secret)
    cows = int(
        textdistance.overlap.similarity(guess, secret) * min(len(guess), len(secret))
    )
    return bulls, cows


def gameplay(ask: callable, inform: callable, words) -> int:
    secret = random.choice(words)
    cnt = 0
    while 1:
        cnt += 1
        guess = ask("Введите слово: ", words)
        b, c = bullscows(guess=guess, secret=secret)
        if b == len(secret):
            return cnt
        inform("Быки: {}, Коровы: {}", b, c)


def ask(prompt: str, valid=None) -> str:
    guess = input(prompt)
    if valid is not None:
        while guess not in valid:
            guess = ask(prompt, valid)
    return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
