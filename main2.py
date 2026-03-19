import os
from datetime import datetime
from colorama import Fore, Style, init
from art import tprint

init()

def main():
    print(Fore.GREEN)
    a = str(input("you name:"))
    tprint()
    print(Style.RESET_ALL)

    current_time = datetime.now().strftime("%H:%M:%S")
    current_folder = os.getcwd()

    print(Fore.CYAN + "--- СИСТЕМНАЯ ИНФОРМАЦИЯ ---")
    print(f"Текущее время: {current_time}")
    print(f"Расположение проекта: {current_folder}")
    print("-" * 27 + Style.RESET_ALL)

    print(Fore.GREEN + "\nПрограмма успешно работает!")
    user_name = input(Fore.WHITE + "ФИО студента: ")

    print(f"\n{Fore.GREEN}Отлично, {Fore.YELLOW}{user_name}{Fore.GREEN}!")
    print(f"Вы использовали 4 разные библиотеки в лабораторной работе №4!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
