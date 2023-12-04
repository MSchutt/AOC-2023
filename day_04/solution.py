with open("input.txt", "r") as file:
    data = file.read().strip().splitlines()
    

total_score = 0


for row in data:
    row = row.strip()
    
    # Get rid of the game counter (not needed)
    _, inp = row.split(":")
    inp = inp.strip()
    
    winning_numbers, my_picks = inp.split("|")
    
    winning_set = set([int(x) for x in winning_numbers.split()])
    
    score = 0
    for my_pick in my_picks.split():
        my_pick = int(my_pick)
        if my_pick in winning_set:
            if score == 0:
                score = 1
            else:
                score *= 2
    total_score += score

# 18519
print(total_score)
