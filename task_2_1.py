# "Крестики-нолики"


import copy
import numbers
from random import randint
from tabnanny import check
from time import sleep, time


field = [[' ', '|', ' ', '|', ' '], ['–', '+', '–', '+', '–'], [' ', '|', ' ', '|', ' '],
         ['–', '+', '–', '+', '–'], [' ', '|', ' ', '|', ' ']]


def playingField(fieldUser: list):
    for i in range(len(fieldUser)):
        string = ''
        for j in range(len(fieldUser[i])):
            string += fieldUser[i][j]
        print(string)

def fieldCls(fieldUser: list):
    for i in range(len(fieldUser)):
        for j in range(len(fieldUser[i])):
            if fieldUser[i][j] == '*' or  fieldUser[i][j]== 'x':
                fieldUser[i][j] = ' '

def playersMove(cellNumber, symbol='*'):
    bool = False
    if cellNumber == 1:
        if field[0][0] == ' ':
            field[0][0] = symbol
            bool = True
    elif cellNumber == 2:
        if field[0][2] == ' ':
            field[0][2] = symbol
            bool = True
    elif cellNumber == 3:
        if field[0][4] == ' ':
            field[0][4] = symbol
            bool = True
    elif cellNumber == 4:
        if field[2][0] == ' ':
            field[2][0] = symbol
            bool = True
    elif cellNumber == 5:
        if field[2][2] == ' ':
            field[2][2] = symbol
            bool = True
    elif cellNumber == 6:
        if field[2][4] == ' ':
            field[2][4] = symbol
            bool = True
    elif cellNumber == 7:
        if field[4][0] == ' ':
            field[4][0] = symbol
            bool = True
    elif cellNumber == 8:
        if field[4][2] == ' ':
            field[4][2] = symbol
            bool = True
    elif cellNumber == 9:
        if field[4][4] == ' ':
            field[4][4] = symbol
            bool = True
    return bool

def computerMove():
    check = False
    while(check == False):
        cell = randint(1, 9)
        check = playersMove(cell, symbol='x')

def winUser(text, symbol='*'):
    check = False
    if field[0][0] == symbol and field[0][2] == symbol and field[0][4] == symbol:
        print(text)
        check = True
    elif field[2][0] == symbol and field[2][2] == symbol and field[2][4] == symbol:
        print(text)
        check = True
    elif field[4][0] == symbol and field[4][2] == symbol and field[4][4] == symbol:
        print(text)
        check = True
    elif field[0][0] == symbol and field[2][0] == symbol and field[4][0] == symbol:
        print(text)
        check = True
    elif field[0][2] == symbol and field[2][2] == symbol and field[4][2] == symbol:
        print(text)
        check = True
    elif field[0][4] == symbol and field[2][4] == symbol and field[4][4] == symbol:
        print(text)
        check = True
    elif field[0][0] == symbol and field[2][2] == symbol and field[4][4] == symbol:
        print(text)
        check = True
    elif field[0][4] == symbol and field[2][2] == symbol and field[4][0] == symbol:
        print(text)
        check = True
    return check

def winPc(text, symbol='x'):
    check = winUser(text, symbol)
    return check

def game(fieldUser):
    print('Готов начать игру?')
    strUser = input()
    count = 9
    while(count > 0):
        print("Введите номер клетки от 1 до 9:...")
        playersMove(int(input()))
        playingField(fieldUser)
        check = winUser("Win!\nНачать заново?\n/break\n/exit")
        if check:
            strUser += input()
            break
        count -= 1
        if count == 0:
            print("Ходов больше не осталось!\nНачать заново?\n/break\n/exit")
            strUser += input()
        print("Ход ПК:...")
        sleep(2)
        computerMove()
        playingField(fieldUser)
        check = winPc("False!\nНачать заново?\n/break\n/exit")
        if check:
            strUser += input()
            break
        count -= 1
        if count == 0:
            print("Ходов больше не осталось!\nНачать заново?\n/break\n/exit")
            strUser += input()
    return strUser

def gg(fieldUser):
    fieldCls(fieldUser) 
    strUser = game(fieldUser)
    if strUser == '/break':
        gg(fieldUser)
    if strUser == '/exit':
        print('Игра окончена')


gg(field)

