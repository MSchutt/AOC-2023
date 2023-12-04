from typing import List, Dict

with open("input.txt", "r") as file:
    data = file.read().strip().splitlines()

data = [row.strip() for row in data]   

# Additional dictionaries to cache results
# row_id -> number of winning scratchcards
winning_cards_cache: Dict[str, int] = {}
# row_id -> total score (including copy scratchcards)
process_scratchcard_cache: Dict[str, int] = {}


def get_number_of_winning_cards(row_id: int, row: str) -> int:
    """ Returns the number of winning scratchcards for a given row

    Args:
        row (str): Input row

    Returns:
        int: number of winning scratchcards
    """    
    
    # Check if already seen (= in cache)
    if row_id in winning_cards_cache:
        return winning_cards_cache[row_id]
    
    # Get rid of the game counter (not needed)
    _, inp = row.split(":")
    inp = inp.strip()
    
    # Split into winning_number (left) and my picks (right)
    winning_numbers, my_picks = inp.split("|")
    
    winning_set = set([int(x) for x in winning_numbers.split()])
    
    # Iterate through my_picks and add 1 if found in the winning_set
    winning = 0
    for my_pick in my_picks.split():
        my_pick = int(my_pick)
        if my_pick in winning_set:
            winning += 1
            
    # Store the value in the cache
    winning_cards_cache[row_id] = winning
    
    return winning          


def process_scratchcards(start_idx: int, winning: int, data: List[str]) -> int:
    """ Recursively processes the scratchcards and returns the total score for that particular scratchcard

    Args:
        start_idx (int): start index
        winning (int): number of winning cards
        data (List[str]): input data

    Returns:
        int: total score
    """    
    # Check for cache
    if start_idx in process_scratchcard_cache:
        return process_scratchcard_cache[start_idx]
    
    total_score = 0
    for i in range(start_idx, start_idx + winning):
        winning2 = get_number_of_winning_cards(i, data[i])
        total_score += 1
        total_score += process_scratchcards(i + 1, winning2, data)
    
    process_scratchcard_cache[start_idx] = total_score
    return total_score
                
                
total_score = 0

for row_id, row in enumerate(data):
    winning = get_number_of_winning_cards(row_id, row)
    # Ensure that every scratchcard is counted, even if it is not winning
    total_score += 1
    
    if winning > 0:
        i = row_id + 1
        total_score += process_scratchcards(i, winning, data)

# 11787590
print(total_score)