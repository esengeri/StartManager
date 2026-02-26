from colorama import Fore, Style, init
init()
def main():
    print(Fore.CYAN + "============================")
    print(Fore.RED + "SMART MANAGER НАЧАЛ РАБОТАТЬ")
    print(Fore.CYAN + "============================"+Style.RESET_ALL)
    user_name = input("user name:")
    print(f"\n HELLO,"+Fore.GREEN+user_name+Style.RESET_ALL+"!")
    print(Fore.MAGENTA + "Labaratoring work complate"+Style.RESET_ALL)

if __name__=="__main__":
    main()