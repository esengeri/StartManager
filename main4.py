import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def get_user_age():
    logging.info("Запущена функция запроса возраста.")
    try:
        age_input = input("Введите ваш возраст: ")
        age = int(age_input)
        logging.info(f"Пользователь ввел возраст: {age}")
        print(f"Спасибо! Ваш возраст: {age}")
    except ValueError:
        logging.error("Ошибка! Пользователь ввел нечисловые данные.")
        print("Пожалуйста, вводите только числа!")

if __name__ == "__main__":
    logging.info("Программа запущена.")
    get_user_age()
    logging.info("Программа успешно завершена.")