
THRESHOLDS = {
    "green": 13,
    "blue": 14,
    "red": 12
}

def sol1():
    with open('input.txt', "r") as f:
        data = f.read().splitlines()
        
    
    possible_game_sum = 0
    
    for row in data:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        row = row.strip()
        
        # Split input: Game 1 & 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game, other = row.strip().split(":")
        # Extract game id
        game_id = int(game.split(" ")[1])
        
        # Assume that game is possible; if we find out once that it is not, we set this to False and break
        is_possible_game = True
        
        # other => 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        # seperate the games
        for round in other.split(";"):
            # round_row now contains all the cubes from the round (i.e. 3 blue, 4 red)
            for round_row in round.strip().split(","):
                # Turn stats now contains: ("3", "blue")
                turn_stats = round_row.strip().split()
                
                # Parse out amount & color
                amount = int(turn_stats[0])
                color = turn_stats[1]
                
                # Check if the game is possible (1 error => not possible anymore; can break)
                if THRESHOLDS[color] < amount:
                    is_possible_game = False
                    break
                    
        if is_possible_game:
            possible_game_sum += game_id
                        
    
    print(possible_game_sum)
    
    
    
if __name__ == "__main__":
    sol1()