import numpy as np

FIND_MAP = [
    *[(f"{i + 1}", i + 1) for i in range(9)],
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9)
]

def process_row(row: str):
    lowest = (np.inf, 0)
    highest = (np.inf, 0)
    
    row_rev = row[::-1]
    for search_key, number in FIND_MAP:
        idx_first = row.find(search_key)
        if idx_first > -1 and idx_first < lowest[0]:
            lowest = (idx_first, number)
            
        idx_last = row_rev.find(search_key[::-1])
        if idx_last > -1 and idx_last < highest[0]:
            highest = (idx_last, number)
            
    return int(f"{lowest[1]}{highest[1]}")


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        
        total_sum = 0
        
        for row in data:
            total_sum += process_row(row)
            
        # 53868
        print(total_sum)

if __name__ == '__main__':
    main()

