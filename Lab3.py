from array import *
import random
import numpy as num

#----------------- zad2
def zad2():
    tab = array('u', [])
    liczba = int(input('Ilość znaków: '))
    liczba1 = 0

    while liczba1 < liczba:
        tab.append(input('Proszę podać jakiś znak: '))
        liczba1 += 1

    for i in reversed(tab):
        print(i)

#zad2()
#----------------- zad2

#----------------- zad3
def zad3():
    tab = []
    liczba = int(input('Podaj ilość znaków wprowadzanych'))
    liczba1 = 0

    while liczba1 < liczba:
        tab.append(random.randrange(-5, 5))
        liczba1 += 1

    file = open('rozwiazanie_3.txt', 'w')
    file.write(tab.__str__())

#zad3()
#----------------- zad3

#----------------- zad4
def zad4():

    tab = num.array([[2, 3, 4, 5, 6],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]], dtype=num.float)

    for i in range(1, 5):
        for j in range(5):
            tab[i][j] = tab[i - 1][j] * tab[i - 1][j]

    print(tab)

#zad4()
#----------------- zad4

#----------------- zad5
def zad5():
    nazwa = input("Proszę podać nazwę pliku: ")
    file = open(nazwa+'.txt')
    histogram = {}

    while True:
        znak = file.read(1)
        if not znak:
            break
        if znak in histogram:
            x = histogram.get(znak)
            histogram[znak] = x + 1
        else:
            histogram[znak] = 1

    file.close()
    print(histogram)

#zad5()
#----------------- zad5

#----------------- zad6
def zad6():
    def deck():
        deck = [('2', 'c'), ('2', 'd'), ('2', 'h'), ('2', 's'), ('3', 'c'), ('3', 'd'), ('3', 'h'), ('3', 's'),
                ('4', 'c'), ('4', 'd'), ('4', 'h'), ('4', 's'), ('5', 'c'), ('5', 'd'), ('5', 'h'), ('5', 's'),
                ('6', 'c'), ('6', 'd'), ('6', 'h'), ('6', 's'), ('7', 'c'), ('7', 'd'), ('7', 'h'), ('7', 's'),
                ('8', 'c'), ('8', 'd'), ('8', 'h'), ('8', 's'), ('9', 'c'), ('9', 'd'), ('9', 'h'), ('9', 's'),
                ('10', 'c'), ('10', 'd'), ('10', 'h'), ('10', 's'), ('J', 'c'), ('J', 'd'), ('J', 'h'), ('J', 's'),
                ('D', 'c'), ('D', 'd'), ('D', 'h'), ('D', 's'), ('K', 'c'), ('K', 'd'), ('K', 'h'), ('K', 's'),
                ('A', 'c'), ('A', 'd'), ('A', 'h'), ('A', 's')]
        return deck

    def shuffle_deck(deck):
        random.shuffle(deck)
        return deck

    def deal(deck, n):
        table = []
        for i in range(0, n):
            table.append(random.sample(deck, 5))
        return table

    deckTemp = shuffle_deck(deck())
    ilosc = int(input('Podaj ilość graczy przy stole: '))
    rozdanie = deal(deckTemp, ilosc)
    print(rozdanie)


zad6()
#----------------- zad6
