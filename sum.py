def sum_of_digits(num: int) -> int:
    total = 0
    while num > 0:
        digit = num % 10      # extract last digit
        total += digit        # add to sum
        num //= 10            # remove last digit
    return total

num=int(input("Give the number to add:"))
print(sum_of_digits(num))    