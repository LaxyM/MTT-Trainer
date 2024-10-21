"""
# Function that generates random Hold'em starting hand.
"""

# def deal_hand():
#     import random
    
#     suit_dict = {0: 's', 1:'c', 2:'h', 3:'d'}
#     value_dict = {10:'T', 11:'J', 12:'Q', 13:'K', 14:'A'}
    
#     def match_card(num):
#         try:
#             value = value_dict[num % 13 + 2]
#         except KeyError:
#             value = num % 13 + 2
#         suit = suit_dict[num // 13]     
#         return f'{value}{suit}'

#     num1 = random.randint(0,51)
#     while True:
#         num2 = random.randint(0,51)
#         if num1 != num2: break
#     card1 = match_card(num1)
#     card2 = match_card(num2)
    
#     if num2 % 13 > num1 % 13:
#         return f'{card2}{card1}'
#     return f'{card1}{card2}'




#!  актуальная версия стартеров которые будут раздаваться
import random

def deal_hand():
    suit_dict = {0: 's', 1:'c', 2:'h', 3:'d'}
    value_dict = {10:'T', 11:'J', 12:'Q', 13:'K', 14:'A'}
    
    # Преобразование номера карты в её значение и масть
    def match_card(num):
        try:
            value = value_dict[num % 13 + 2]
        except KeyError:
            value = num % 13 + 2
        suit = suit_dict[num // 13]     
        return f'{value}{suit}'

    #  комбинации карт (45,6%)
    valid_hands = [
    'AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22',
    'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
    'AKo', 'AQo', 'AJo', 'ATo', 'A9o', 'A8o', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o',
    'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
    'KQo', 'KJo', 'KTo', 'K9o', 'K8o', 'K7o', 'K6o', 'K5o', 'K4o', 'K3o', 'K2o',
    'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s',
    'QJo', 'QTo', 'Q9o', 'Q8o',
    'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s',
    'JTo', 'J9o', 'J8o',
    'T9s', 'T8s', 'T7s', 'T6s',
    'T9o', 'T8o',
    '98s', '97s', '96s',
    '98o',
    '87s', '86s', 
    '76s', '75s', 
    '65s',
]


    # Проверка, входит ли пара карт в диапазон
    def is_valid_hand(card1, card2):
        hand = f'{card1[0]}{card2[0]}'
        if card1[0] == card2[0]:  # Для пар (AA, KK и т.д.)
            return hand in valid_hands
        elif card1[1] == card2[1]:  # Одномастные комбинации
            return f'{hand}s' in valid_hands
        else:  # Разномастные комбинации
            return f'{hand}o' in valid_hands

    # Генерация двух карт
    while True:
        num1 = random.randint(0, 51)
        num2 = random.randint(0, 51)
        if num1 != num2:
            card1 = match_card(num1)
            card2 = match_card(num2)

            # Проверяем, подходит ли рука под диапазон
            if is_valid_hand(card1, card2):
                if num2 % 13 > num1 % 13:
                    return f'{card2}{card1}'
                return f'{card1}{card2}'





"""
# Function that randomly selects both the positions and game-tree position of two players.
"""

def deal_pos():
    import random  
    
    positions_dict = {0: "EP", 1: "MP", 2: "CO", 3: "BN", 4: "SB", 5: "BB"}
    tree_dict = {0: "Open", 1: "Facing Open", 2: "Facing 3Bet", 3: "Facing 4Bet"}
    


    #! Изменение позиции
    pos1 = random.randint(4,4)
    while True:
        pos2 = random.randint(5,5)
        if pos1 != pos2: break
    tree = random.randint(0,3)
    

    if tree in [0, 2]:
        if pos1 > pos2:
            return (tree, positions_dict[pos2], positions_dict[pos1], tree_dict[tree])
    else:
        if pos1 < pos2:
            return (tree, positions_dict[pos2], positions_dict[pos1], tree_dict[tree])
    return (tree, positions_dict[pos1], positions_dict[pos2], tree_dict[tree])

"""
# Function that determines whether a given hand is within a given hand range.
"""

def in_range(hand, handrange):
    
    if len(handrange) < 2:
        return False   
    
    if hand[1] == hand[3]:
        hand = f'{hand[0]}{hand[2]}s'
    else:
        hand = f'{hand[0]}{hand[2]}'
        
    hand_list = handrange.split(",")
    
    for entry in hand_list:  
        if entry.split(':')[0] == hand:
            return True
    return False