q = {
    2: +1,
    3: +1,
    4: +1,
    5: +1,
    6: +1,
    7: 0,
    8: 0,
    9: 0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1,
        }
curent_hand = [2, 3, "K", 10, 10, 4]
cards_sym = []
for x in curent_hand:
    i = q[x]
    cards_sym.append(i)

print(sum(cards_sym))








