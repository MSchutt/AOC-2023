from typing import List

SYMBOLS = "."
DIGITS = "0123456789"
SYMBOLS_DIGIT = "." + DIGITS


def check_direction(arr: List[List[str]], x: int, y: int, max_rows: int, max_cols: int) -> bool:
    """ Check the direction of the current position in the matrix

    Args:
        arr (List[List[str]]): Matrix to check
        x (int): x index (row)
        y (int): y index (column)
        
    Returns:
        bool: True if the current position is valid, False otherwise
    """    
    
    # Check to the right
    if y + 1 < max_cols and arr[x][y + 1] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the left
    if y - 1 >= 0 and arr[x][y - 1] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the top
    if x - 1 >= 0 and arr[x - 1][y] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the bottom
    if x + 1 < max_rows and arr[x + 1][y] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the top left
    if x - 1 >= 0 and y - 1 >= 0 and arr[x - 1][y - 1] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the top right
    if x - 1 >= 0 and y + 1 < max_cols and arr[x - 1][y + 1] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the bottom left
    if x + 1 < max_rows and y - 1 >= 0 and arr[x + 1][y - 1] not in SYMBOLS_DIGIT:
        return True
    
    # Check to the bottom right
    if x + 1 < max_rows and y + 1 < max_cols and arr[x + 1][y + 1] not in SYMBOLS_DIGIT:
        return True
    
    return False
    

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    
# Create a matrix
matrix = []
for row in data:
    matrix.append(list(row))
    
# Get the dimensions of the matrix
max_rows = len(matrix)
max_cols = len(matrix[0])

current_number = ""

total_sum = 0

is_number = False
is_valid = False
    
for x in range(max_rows):
    for y in range(max_cols):
        if matrix[x][y] in DIGITS:
            is_number = True
            current_number += str(matrix[x][y])
            # Check if the current position is valid
            if check_direction(matrix, x, y, max_rows, max_cols):
                is_valid = True
        # Number was previously seen, but is no longer seen now (number complete -> parse, check conditions and reset the flags)
        elif is_number:
            if is_valid and len(current_number) > 0:
                total_sum += int(current_number)
            current_number = ""
            # Reset flags back to default
            is_number = False
            is_valid = False
# 537732
print(total_sum)
