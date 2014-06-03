def romanize(tal):
    Romerskt_tal = ''
    tal_list_list = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                     ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]

    if tal == 0:
        raise ValueError('can not encode zero')
    if tal < 0:
        raise ValueError('can not encode negative number')


    for list in tal_list_list:
        while tal - list[1] >= 0:
            tal = tal - list[1]
            Romerskt_tal += list[0]

    return Romerskt_tal

print(romanize(44))