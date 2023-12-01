
ALL_NUMBERS = "123456789"

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    
    total_sum = 0
    
    
    # Iterate over all rows
    for row in data:
        # Replace the words with numbers
        first_digit = 0
        last_digit = 0
        for char in row:
            if char in ALL_NUMBERS:
                if first_digit == 0:
                    first_digit = char
                    last_digit = char
                else:
                    last_digit = char
        total_sum += int(f'{first_digit}{last_digit}')
            
    print(total_sum)