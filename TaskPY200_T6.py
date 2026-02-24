def find_smallest_number(N: int) -> int:
    """
    Find smallest number in range 1..N such that:
    - Sum of digits divisible by 7
    - Contains exactly two '3's
    - Does not contain digit '0'
    """

    # Loop from 1 to N
    for x in range(1, N + 1):

        digit_sum = 0
        count_3 = 0
        has_zero = False

        num = x

        # Extract digits manually (First Principle)
        while num > 0:
            digit = num % 10

            # Condition: no zero allowed
            if digit == 0:
                has_zero = True

            # Count number of 3s
            if digit == 3:
                count_3 += 1

            digit_sum += digit
            num = num // 10

        # Final checks
        if (not has_zero) and (count_3 == 2) and (digit_sum % 7 == 0):
            return x  # smallest mil gaya

    return -1