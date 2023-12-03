

from typing import List

DIGITS = "0123456789"

def extract_number(matrix: List[List[str]], x: int, y: int) -> int:
    """ Search both the right and to the left to extract the number.

    Args:
        matrix (List[List[str]]): Matrix
        x (int): row index
        y (int): column index

    Returns:
        int: Extracted number
    """    
    found_number = ""
    

    y_left = y
    # Search to the left
    while y_left >= 0 and matrix[x][y_left] in DIGITS:
        # Prepend
        found_number = str(matrix[x][y_left]) + found_number
        y_left -= 1
    
    # y case already handled by search to the left
    y_right = y + 1
    # Search to the right
    while y_right < len(matrix[x]) and matrix[x][y_right] in DIGITS:
        # append
        found_number += str(matrix[x][y_right])
        y_right += 1
        
    return int(found_number)

def check_if_gear(matrix: List[List[str]], x: int, y: int):
    """ Check if the current position is a gear

    Args:
        matrix (List[List[str]]): Matrix to check
        x (int): row index
        y (int): column index

    Returns:
        bool: True if the current position is a gear (= exactly two numbers found), False otherwise
    """    
    
    # Additional logic to not double count some gears.
    top_found = False
    bottom_found = False
    
    numbers = []
    
    # Check to the left
    if y - 1 >= 0 and matrix[x][y - 1] in DIGITS:
        numbers.append(extract_number(matrix, x, y - 1))
        
        
    # Check to the right
    if y + 1 < len(matrix[x]) and matrix[x][y + 1] in DIGITS:
        numbers.append(extract_number(matrix, x, y + 1))
        
    # Check to the top
    if x - 1 >= 0 and matrix[x - 1][y] in DIGITS:
        numbers.append(extract_number(matrix, x - 1, y))
        top_found = True
        
    # Check to the bottom
    if x + 1 < len(matrix) and matrix[x + 1][y] in DIGITS:
        bottom_found = True
        numbers.append(extract_number(matrix, x + 1, y))
        
    # Check to the top left
    if x - 1 >= 0 and y - 1 >= 0 and matrix[x - 1][y - 1] in DIGITS:
        # If top has already been found then we don't want to add this number, as this is 100% just a continuation of the top number
        # Same is valid for top right, bottom left and bottom right (just with the bottom variable)
        if not top_found:
            numbers.append(extract_number(matrix, x - 1, y - 1))
            
        
    # Check to the top right
    if x - 1 >= 0 and y + 1 < len(matrix[x]) and matrix[x - 1][y + 1] in DIGITS:
        if not top_found:
            numbers.append(extract_number(matrix, x - 1, y + 1))
        top_found = True
        
    # Check to the bottom left
    if x + 1 < len(matrix) and y - 1 >= 0 and matrix[x + 1][y - 1] in DIGITS:
        if not bottom_found:
            numbers.append(extract_number(matrix, x + 1, y - 1))
        
    # Check to the bottom right
    if x + 1 < len(matrix) and y + 1 < len(matrix[x]) and matrix[x + 1][y + 1] in DIGITS:
        if not bottom_found:
            numbers.append(extract_number(matrix, x + 1, y + 1))
    
    return numbers



with open("input.txt", "r") as f:
    data = f.read().strip().splitlines()

# Create a matrix
matrix = []
for row in data:
    matrix.append(list(row.strip()))
    
max_rows = len(matrix)
max_cols = len(matrix[0])#

current_number = ""

total_sum = 0


for x in range(max_rows):
    for y in range(max_cols):
        if matrix[x][y] == "*":
            numbers = check_if_gear(matrix, x, y)
            if len(numbers) == 2:
                total_sum += (numbers[0] * numbers[1])

# 84883664
print(total_sum)