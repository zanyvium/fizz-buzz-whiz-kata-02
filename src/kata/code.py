NUMBERS_UP_TO = 100
all_numbers = set(range(1, NUMBERS_UP_TO + 1, 1))
numbers_div_by_three = set(range(3, NUMBERS_UP_TO + 1, 3))
numbers_div_by_five = set(range(5, NUMBERS_UP_TO + 1, 5))
numbers_div_by_three_and_five = numbers_div_by_three & numbers_div_by_five

# fmt: off
primes_up_to_100 = {
    2, 3, 5, 7,
    11, 13, 17, 19,
    23, 29,
    31, 37,
    41, 43, 47,
    53, 59,
    61, 67,
    71, 73, 79,
    83, 89,
    97
}
# fmt: on


def fizz_buzz_whiz(number: int) -> str:
    if number in primes_up_to_100:
        return "Whiz"
    elif number in numbers_div_by_three_and_five:
        return "FizzBuzz"
    elif number in numbers_div_by_five:
        return "Buzz"
