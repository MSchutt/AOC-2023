
import functools
from typing import List


CARD_VALUE = {
    **{str(i): i for i in range(2, 10)},
    "T": 10,
    # Set to 0 -> is now the weakest card in direct comparison
    "J": 0,
    "Q": 12,
    "K": 13,
    "A": 14,
}

POSSIBLE_OUTCOMES = {
    "FIVE_KIND": 7,
    "FOUR_KIND": 6,
    "FULL_HOUSE": 5,
    "THREE_KIND": 4,
    "TWO_PAIR": 3,
    "ONE_PAIR": 2,
    "HIGH_CARD": 1
}


class Hand:
    def __init__(self, inp: str):
        values = inp.split()
        self.cards = values[0]
        self.bid = int(values[1])
        self.outcome = None
     
    def _evaluate(self) -> int:
        counter = {}
        for card in self.cards:
            if card not in counter:
                counter[card] = 0
            counter[card] += 1
        
        
        number_of_joker = counter["J"] if "J" in counter else 0
        
        # Add the joker to the class that has the highest number of cards
        if number_of_joker > 0:
            # Find the maximum of other cards
            counter_cp = counter.copy()
            del counter_cp["J"]
            # Special case -> no other card in hand but 5 jokers
            # -> just break and return 5 kind
            # Now we know the most valueable card, add the joker
            if len(counter_cp.keys()) == 0:
                return POSSIBLE_OUTCOMES["FIVE_KIND"]
            max_number = max(counter_cp.values())
            
            
            # Key, Value
            max_tuple = ("", 0)
            # now for all the values that have the max number of cards, find the most valueable one
            for key, value in counter.items():
                # Filter for the max
                if value == max_number and key != "J":
                    converted_value = CARD_VALUE[key]
                    if max_tuple[1] < converted_value:
                        max_tuple = (key, converted_value)

            counter[max_tuple[0]] += number_of_joker
            del counter["J"]
            
        unique_keys = list(counter.keys())
            
        # Just one key -> must be 5 kind
        if len(unique_keys) == 1:
            return POSSIBLE_OUTCOMES["FIVE_KIND"]
        
        # can be 4 kind or full house
        elif len(unique_keys) == 2:
            # If either of the classes contains 4 cards, it must be 4 kind
            if counter[unique_keys[0]] == 4 or counter[unique_keys[1]] == 4:
                return POSSIBLE_OUTCOMES["FOUR_KIND"]
            # otherwise we have a full house for sure
            else:
                return POSSIBLE_OUTCOMES["FULL_HOUSE"]
            
        elif len(unique_keys) == 3:
            # If either of the classes contains 3 cards, it must be 3 kind
            if counter[unique_keys[0]] == 3 or counter[unique_keys[1]] == 3 or counter[unique_keys[2]] == 3:
                return POSSIBLE_OUTCOMES["THREE_KIND"]
            # otherwise we have a two pair for sure
            
            # check for two pairs
            if (counter[unique_keys[0]] == 2 and counter[unique_keys[1]] == 2) or (counter[unique_keys[1]] == 2 and counter[unique_keys[2]] == 2) or (counter[unique_keys[0]] == 2 and counter[unique_keys[2]] == 2):
                return POSSIBLE_OUTCOMES["TWO_PAIR"]
            
        elif len(unique_keys) == 4:
            # If either of the classes contains 2 cards, it must be 2 kind
            if counter[unique_keys[0]] == 2 or counter[unique_keys[1]] == 2 or counter[unique_keys[2]] == 2 or counter[unique_keys[3]] == 2:
                return POSSIBLE_OUTCOMES["ONE_PAIR"]
            
        return POSSIBLE_OUTCOMES["HIGH_CARD"]
    
    def evaluate(self) -> int:
        if self.outcome is None:
            self.outcome = self._evaluate()
        return self.outcome
        
        
 
def evaluate_draw(hand1: Hand, hand2: Hand):
    """
    Compares the cards in hand1 and hand2 and determines the winner.
    This should only be called if the hands have the same score and the winner is determined by the card values.

    Args:
        hand1 (Hand): The first hand to evaluate.
        hand2 (Hand): The second hand to evaluate.

    Returns:
        int: 1 if hand1 wins, -1 if hand2 wins, 0 if it's a draw.
    """
    for i in range(len(hand1.cards)):
        hand1_card = CARD_VALUE[hand1.cards[i]]
        hand2_card = CARD_VALUE[hand2.cards[i]]
        if hand1_card > hand2_card:
            return 1
        elif hand2_card > hand1_card:
            return -1
    return 0

 
def compare_hands(hand1: Hand, hand2: Hand):
    """
    Compare two hands and determine the winner based on their scores.
    
    Args:
        hand1 (Hand): The first hand to compare.
        hand2 (Hand): The second hand to compare.
    
    Returns:
        int: 1 if hand1 wins, -1 if hand2 wins, or the result of evaluate_draw if it's a draw.
    """
    hand1_score = hand1.evaluate()
    hand2_score = hand2.evaluate()
    
    if hand1_score > hand2_score:
        return 1
    elif hand2_score > hand1_score:
        return -1
    else:
        return evaluate_draw(hand1, hand2)



def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        
    hands: List[Hand] = [Hand(line.strip()) for line in lines]
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands), reverse=False)
        
    total = 0
    for rank, hand in enumerate(sorted_hands):
        # print(f"{rank + 1}: {hand.cards} {hand.bid} {hand.evaluate()}")
        total += (rank + 1) * hand.bid

    # 253499763
    print(total)
    


if __name__ == "__main__":
    main()