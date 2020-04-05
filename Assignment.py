import itertools
import random


arr = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'KH', 'JH', 'QH',
       'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'KD', 'JD', 'QD',
       'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'KS', 'JS', 'QS',
       'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'KC', 'JC', 'QC']

arrA = []
arrB = []
arrC = []
arrD = []


carddeck = list(itertools.product(range(1, 12), arr))


def player1(n):
    for i in range(n):
        random.shuffle(carddeck)
        arrA.append(carddeck[i][1])
        carddeck.remove(carddeck[i])


def player2(n):
    for j in range(n):
        random.shuffle(carddeck)
        arrB.append(carddeck[j][1])
        carddeck.remove(carddeck[j])


def player3(n):
    for f in range(n):
        random.shuffle(carddeck)
        arrC.append(carddeck[f][1])
        carddeck.remove(carddeck[f])


def player4(n):
    for g in range(n):
        random.shuffle(carddeck)
        arrD.append(carddeck[g][1])
        carddeck.remove(carddeck[g])


player1(13)
player2(13)
player3(13)
player4(13)


print('player A:', arrA)
print('player B:', arrB)
print('player C:', arrC)
print('player D:', arrD)
