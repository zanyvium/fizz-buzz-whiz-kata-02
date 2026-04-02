from src.kata.code import NUMBERS_UP_TO, fizz_buzz_whiz, primes_up_to_100

numbers_div_by_three = set(range(3, NUMBERS_UP_TO + 1, 3))
numbers_div_by_five = set(range(5, NUMBERS_UP_TO + 1, 5))
numbers_div_by_three_and_five = numbers_div_by_three & numbers_div_by_five

print(NUMBERS_UP_TO)


def test_primes():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == "Whiz"


def test_div_by_three_and_five():
    for number in numbers_div_by_three_and_five:
        assert fizz_buzz_whiz(number) == "FizzBuzz"
