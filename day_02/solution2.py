
def sol2():
    with open('input.txt', "r") as f:
        data = f.read().splitlines()
    
    game_sum = 0
    
    for row in data:
        row = row.strip()
        
        _, other = row.strip().split(":")
        
        minimum_required_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        # seperate the games
        for round in other.split(";"):
            for round_row in round.strip().split(","):
                turn_stats = round_row.strip().split()
                amount = int(turn_stats[0])
                color = turn_stats[1]
                
                # Find the maximum amount of cubes required for each color
                if amount > minimum_required_cubes[color]:
                    minimum_required_cubes[color] = amount
                    
        game_sum += (minimum_required_cubes["red"] * minimum_required_cubes["green"] * minimum_required_cubes["blue"])
    
    print(game_sum)
    
    
    
if __name__ == "__main__":
    sol2()