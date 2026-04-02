from src.kata.code import NUMBERS_UP_TO, fizz_buzz_whiz, primes_up_to_100

print(NUMBERS_UP_TO)


def test_primes():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == "Whiz"
