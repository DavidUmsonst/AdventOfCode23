

class Hand:

    def __init__(self, cards: str, bid: str, joker_rule: bool = False) -> None:
        self._bid = int(bid)
        self._joker_rule = joker_rule
        self._cards =  cards
        self._card_counter = self.get_card_counter(cards)
        self._card_values = self.get_card_values(cards, joker_rule)
        
        
    def __repr__(self) -> str:
        return f"Cards: {self._cards}, Bid: {self._bid}"
    
    def get_card_counter(self, cards: str) -> dict:
        counter_dict = {} 
        for card in cards:
            if card in counter_dict:
                counter_dict[card] += 1
            else:
                counter_dict[card] = 1

        return counter_dict
    
    def get_card_values(self, cards: str, joker_rule: bool = False):
        card_values = []
        for card in cards:
            if card.isdigit():
                card_values.append(int(card))
            else:
                if card == 'A':
                    card_values.append(14)
                elif card == 'K':
                    card_values.append(13)
                elif card == 'Q':
                    card_values.append(12)
                elif card == 'J':
                    if joker_rule:
                        card_values.append(1)
                    else:
                        card_values.append(11)
                else:
                    card_values.append(10)

        return card_values

    def get_bid(self) -> int:
        return self._bid
    
    def get_hand_value(self, joker_rule: bool = False) -> int:
        """
        Values for different hands: 
        Five of a kind: 7
        Four of a kind: 6
        Full house: 5
        Three of a kind: 4
        Two pairs: 3
        One pair: 2
        High card: 1
        """
        hand_value = 0
        card_counter_values = list(self._card_counter.values())
        if not joker_rule:
            # hand value for the first task
            if 5 in card_counter_values:
                # five of a kind
                hand_value = 7
            elif 4 in card_counter_values:
                # four of a kind
                hand_value = 6
            elif 3 in card_counter_values and 2 in card_counter_values:
                # full house
                hand_value = 5
            elif 3 in card_counter_values:
                # three of a kind
                hand_value = 4
            elif 2 in card_counter_values:
                if card_counter_values.count(2)==2:
                    # two pairs
                    hand_value = 3
                else:
                    # one pair
                    hand_value = 2
            else:
                # high card
                hand_value = 1
        else:
            is_joker_present = 'J' in self._card_counter 
            if 5 in card_counter_values:
                # five of a kind
                hand_value = 7
            elif 4 in card_counter_values:
                # four of a kind
                if is_joker_present and self._card_counter['J'] == 1:
                    # if joker is remaining card, the hand turns into five of a kind
                    hand_value = 7
                else:
                    hand_value = 6
            elif 3 in card_counter_values and 2 in card_counter_values:
                # full house
                if is_joker_present:
                    # if there is a joker the hand turns into a five of a kind
                    hand_value = 7
                else:
                    # otherwise it remains a full house
                    hand_value = 5
            elif 3 in card_counter_values:
                # three of a kind
                if is_joker_present:
                    # if there is a joker it turns into four of a kind, because it is higher than a full house
                    hand_value = 6
                else:
                    hand_value = 4
            elif 2 in card_counter_values:
                if card_counter_values.count(2)==2:
                    # two pairs case
                    if is_joker_present:
                        if self._card_counter['J'] == 2:
                            # if one pair consists of jokers the hand turns into a four of a kind
                            hand_value = 6
                        else:
                            # if the joker is a single card in the two pair hand
                            # the hand turns into a full house
                            hand_value = 5
                            
                    else:
                        # if there is no joker the value is that of two pairs
                        hand_value = 3
                else:
                    # one pair
                    if is_joker_present:
                        hand_value = 4
                    else:
                        hand_value = 2
            else:
                if is_joker_present:
                    # if there is a joker and all cards are different it will turn into one pair
                    hand_value = 2
                else:
                    hand_value = 1
                

        return hand_value
    
    def __lt__(self, other) -> bool:
        if type(other) is Hand:
            if self.get_hand_value(self._joker_rule)<other.get_hand_value(self._joker_rule):
                return True
            elif self.get_hand_value(self._joker_rule)==other.get_hand_value(self._joker_rule):
                # same hand values, so we need to go through the cards
                for i, card_value in enumerate(self._card_values):
                    if card_value<other._card_values[i]:
                        return True
                    elif card_value==other._card_values[i]:
                        continue
                    else:
                        return False
            else:
                return False
        else:
            print("Wrong type, returning false")
            return False
        return True
    
with open('./Day7/input') as file:
    lines = [line.rstrip() for line in file]

joker_rule_from_task_2 = True
hands: list[Hand] = list()
for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards,bid, joker_rule=joker_rule_from_task_2))
    
hands.sort()
solution = 0
for i, hand in enumerate(hands):
    solution += (i+1)*hand.get_bid()

print(f"The solution for the first task is {solution}")

