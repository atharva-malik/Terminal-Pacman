from pacman import *
from os import system, name
import keyboard, time

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

board = Board()
while True:
    clear()
    print(board)
    if keyboard.is_pressed("w"):
        board.pac.direction = 2
        keyboard.press_and_release("backspace")
    if keyboard.is_pressed("a"):
        board.pac.direction = 4
        keyboard.press_and_release("backspace")
    if keyboard.is_pressed("s"):
        board.pac.direction = 1
        keyboard.press_and_release("backspace")
    if keyboard.is_pressed("d"):
        board.pac.direction = 3
        keyboard.press_and_release("backspace")
    board.update()
    time.sleep(0.1)