

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
    total_row_sum = 0
        
    for numbers in lines:
        numbers = [int(number.strip()) for number in numbers.split()]
        
        # Build out the whole table
        rows = [numbers]
        while True:
            row = []
            for i in range(0, len(numbers) - 1):
                row.append(numbers[i + 1] - numbers[i])
            rows.append(row)
            numbers = row
            
            # Check if all of the rows are zero -> stop
            if all(row_elem == 0 for row_elem in row):
                break
        
        prev = 0
        
        for row in reversed(rows):
            row.insert(0, row[0] - prev)
            prev = row[0]
            
        total_row_sum += rows[0][0]
        
    print(total_row_sum)


if __name__ == '__main__':
    main()
