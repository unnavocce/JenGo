"""
JENGA CALCULATOR by unnavocce
"""
from colorama import *
import texts
import numpy as np


init(autoreset=True)


def calculate(t):
    print("Calculation...\n")
    for row_id, row in enumerate(t):
        for col_id, column in enumerate(row):
            tower[row_id][col_id] += sum(tower[row_id-1]) / len(tower[row_id])

    print(tower)
    print(" ")
    start()


def delete():
        index = input("\nWrite index of element to delete like\n1 0\n").split(" ")
        print(" ")
        w = np.delete(tower, 0, 1)
        calculate(w)


def create_tower():
    row = 1
    letter = 0
    for i in range(width):
        row += 1
    for i in range(int(height/2)):
        letter += 1
    global tower
    tower = np.empty((height,width), dtype=int)
    for row_id, row in enumerate(tower):
        for col_id, column in enumerate(row):
            tower[row_id][col_id] = 1
    calculate(tower)


def check(n, func):
    if n > 0 and n < 50:
        pass
    else:
        print("\nInvalid values")
        return func()


def start():
    print(texts.start_message)
    print(f"{Fore.RED}1{Style.RESET_ALL} - Delete element")
    print(f"{Fore.RED}2{Style.RESET_ALL} - Create new tower")
    choise = int(input(""))
    if choise == 1:
        delete()
    elif choise == 2:
        print(texts.width_text)
        global width
        width = int(input(f'Numer of {Fore.RED + "blocks"}{Style.RESET_ALL}: '))
        check(width, start)
        print(texts.height_text)
        global height
        height = int(input(f'Numer of {Fore.RED + "blocks"}{Style.RESET_ALL}: '))
        check(height,start)
        create_tower()
    else:
        start()


if __name__ == "__main__":
    start()