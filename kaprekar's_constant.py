def kaprekar_steps(number):
    seen_numbers = set()
    steps = 0

    while number != 6174:
        if number in seen_numbers:
            print(f"Stuck in a infinite loop. Exiting.")
            break

        seen_numbers.add(number)

        digits = [int(digit) for digit in str(number)]
        while len(digits) < 4:
            digits.insert(0, 0)

        descending = int(''.join(sorted(map(str, digits), reverse=True)))
        ascending = int(''.join(sorted(map(str, digits))))

        number = descending - ascending
        print(f"{descending} - {ascending} = {number}")

        steps += 1

    if number == 6174:
        print(f"Kaprekar's routine achieved in {steps} steps.")

# Example: Starting with a random four-digit number
initial_number = 3524
kaprekar_steps(initial_number)
