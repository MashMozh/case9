import webcolors

print('=== Гексагональный арт-генератор ===\n')

def get_color_choice() -> str:


    def is_valid_color_name(color_name: str) -> bool:
        """Проверяет, существует ли цвет с таким названием в стандарте CSS"""
        try:
            webcolors.name_to_hex(color_name)
            return True
        except ValueError:
            return False


    def get_valid_color(x) -> str:
        while True:
            user_input = input("Введите название цвета на английском: ").strip().lower()

            if is_valid_color_name(user_input):
                return user_input
            else:
                print(f"Ошибка: цвета '{user_input}' не существует в стандарте CSS!")
                print("Примеры правильных названий: red, blue, green, cyan, magenta, etc.")
                print("Попробуйте еще раз.\n")


    print('Доступные цвета:\n')

    # Цвета первой и второй колонок с эмодзи через Unicode
    available_colors_1 = [
        '\U0001F48B Красный',
        '\U0001F499 Синий',
        '\U0001F49A Зелёный',
        '\U0001F49B Жёлтый',
        '\U0001F49C Фиолетовый',
        '\U0001F4A6 Голубой'
        ]

    available_colors_2 = [
        '\U0001F5A4 Черный',
        '\U0001F47D Серый',
        '\U0001F495 Розовый',
        '\U0001F9E1 Оранжевый',
        '\U0001F90E Коричневый',
        '\U0001F916 Свой цвет (HEX) или название (на английском)'
        ]

    # Определяем ширину первой колонки по самому длинному элементу
    max_width = max(len(color) for color in available_colors_1) + 3

    # Печатаем в два столбца с нумерацией
    for i, (col1, col2) in enumerate(zip(available_colors_1, available_colors_2), start=1):
        left_num = i
        right_num = i + len(available_colors_1)
        print(f"{left_num:>2}. {col1:<{max_width}} {right_num:>2}. {col2}")

    color = int(input('\nВаш выбор (введите порядковый номер цвета): '))

    if color == 12:
        get_valid_color(color)


def get_num_hexagons() -> int:
    """Функция для ввода количества шестиугольников с валидацией"""
    while True:
        try:
            quantity = int(input('Введите количество шестиугольников '
                                 'в ряду (от 4 до 20): '))
            if 4 <= quantity <= 20:
                return quantity
            else:
                print('Число шестиугольников должно быть в '
                      'диапазоне от 4 до 20.')
        except ValueError:
            print('Пожалуйста, введите числовое значение от 4 до 20.')
    pass


get_num_hexagons()
get_color_choice()
