def main():
    a = int(input("ваш рост:"))
    m = int(input("ваш вес:"))
    r = a/(m*m)
    if r < 18.5:
        print("Дифицит массы тела")
    elif r >=18.6 and r <= 24.9:
        print("Норма")
    elif r>=25 and r<30:
        print("Избыточный вес")
    else:
        print("ожирение")


if __name__ == "__main__":
    main()
