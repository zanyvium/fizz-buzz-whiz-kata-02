from src.kata.code import (
    NUMBERS_UP_TO,
    all_numbers,
    fizz_buzz_whiz,
    numbers_div_by_three_and_five,
    primes_up_to_100,
)

print(NUMBERS_UP_TO)


def test_primes():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == "Whiz"


def test_div_by_three_and_five():
    for number in numbers_div_by_three_and_five:
        assert fizz_buzz_whiz(number) == "FizzBuzz"


def test_div_by_five():
    numbers = all_numbers - primes_up_to_100 - numbers_div_by_three_and_five
    for number in numbers:
        assert fizz_buzz_whiz(number) == "Buzz"
