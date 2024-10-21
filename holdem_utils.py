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

def expand_range(range_str):
    valid_hands = []
    
    # Обработка пар (например, AA-22)
    if '-' in range_str:
        start, end = range_str.split('-')
        if start == end:  # Обрабатываем одиночную комбинацию (например, AA)
            return [start]
        elif len(start) == 2 and len(end) == 2:  # Диапазон пар (например, AA-22)
            ranks = 'AKQJT98765432'
            start_idx = ranks.index(start[0])
            end_idx = ranks.index(end[0])
            valid_hands.extend([f'{rank}{rank}' for rank in ranks[start_idx:end_idx+1]])
        elif len(start) == 3 and len(end) == 3:  # Диапазон одномастных/разномастных (например, AKs-A2s)
            ranks = 'AKQJT98765432'
            start_idx = ranks.index(start[0])
            end_idx = ranks.index(end[0])
            suit_type = start[2]  # "s" для одномастных, "o" для разномастных
            valid_hands.extend([f'{r1}{r2}{suit_type}' for r1 in ranks[start_idx:end_idx+1] for r2 in ranks[start_idx+1:]])
    else:
        valid_hands.append(range_str)  # Обрабатываем одиночную комбинацию (например, 65s)
    
    return valid_hands

import random

#!  актуальная версия стартеров которые будут раздаваться
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
    range_str = '77-66,ATo,A8o-A7o'
    
    valid_hands = []
    for part in range_str.split(','):
        valid_hands.extend(expand_range(part))
    
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