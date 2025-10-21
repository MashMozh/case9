import turtle
import math
import time
import webcolors

# ======== Цвета для эмодзи меню ========
available_colors_1 = [
    ('\U0001F48B Красный', 'red'),
    ('\U0001F499 Синий', 'blue'),
    ('\U0001F49A Зелёный', 'green'),
    ('\U0001F49B Жёлтый', 'yellow'),
    ('\U0001F49C Фиолетовый', 'purple'),
    ('\U0001F4A6 Голубой', 'cyan')
]
available_colors_2 = [
    ('\U0001F5A4 Чёрный', 'black'),
    ('\U0001F47D Серый', 'gray'),
    ('\U0001F495 Розовый', 'pink'),
    ('\U0001F9E1 Оранжевый', 'orange'),
    ('\U0001F90E Коричневый', 'brown'),
    ('\U0001F916 Свой цвет (HEX/английское имя)', None)
]

# ======== Выбор цвета ========
def get_valid_color_from_user(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input.startswith('#'):
            if len(user_input) in (4, 7):
                return user_input
            else:
                print("Ошибка: неправильный формат HEX. Пример #ff0000 или #f00")
        else:
            try:
                webcolors.name_to_hex(user_input)
                return user_input
            except ValueError:
                print("Ошибка: неизвестное название цвета. Попробуйте снова.")

def get_color_choice():
    print("Доступные цвета:\n")
    max_width = max(len(c[0]) for c in available_colors_1) + 3
    for i, (c1, c2) in enumerate(zip(available_colors_1, available_colors_2), start=1):
        left_num = i
        right_num = i + len(available_colors_1)
        print(f"{left_num:>2}. {c1[0]:<{max_width}} {right_num:>2}. {c2[0]}")

    def choose_color(prompt: str) -> str:
        while True:
            try:
                num = int(input(prompt))
                if 1 <= num <= 12:
                    if num <= 6:
                        return available_colors_1[num-1][1]
                    elif num < 12:
                        return available_colors_2[num-7][1]
                    else:
                        return get_valid_color_from_user("Введите цвет (HEX или английское имя): ")
                else:
                    print("Номер должен быть от 1 до 12")
            except ValueError:
                print("Введите число от 1 до 12")

    first = choose_color("Введите номер первого цвета (1–12): ")
    second = choose_color("Введите номер второго цвета (1–12): ")
    return first, second

# ======== Настройки границы и тени ========
def border_thickness():
    options = {'тонкий':1, 'средний':3, 'толстый':5}
    print("Толщина границы: тонкий, средний, толстый")
    while True:
        choice = input("Выберите толщину границы: ").strip().lower()
        if choice in options: return options[choice]
        print("Ошибка ввода")

def border_color():
    options = ['красный','оранжевый','желтый','зеленый','синий','фиолетовый',
               'розовый','черный','серый','белый']
    print("Цвет границы: " + ", ".join(options))
    while True:
        choice = input("Выберите цвет границы: ").strip().lower()
        if choice in options: return choice
        print("Ошибка ввода")

def shadow_brightness():
    options = {'нет':0, 'слабый':5, 'средний':8, 'сильный':12}
    print("Интенсивность тени: нет, слабый, средний, сильный")
    while True:
        choice = input("Выберите интенсивность тени: ").strip().lower()
        if choice in options: return options[choice]
        print("Ошибка ввода")

# ======== Ввод количества шестиугольников ========
def get_num_hexagons():
    while True:
        val = input("Введите количество шестиугольников в ряду (4-20): ").strip()
        if val.isdigit() and 4 <= int(val) <= 20:
            return int(val)
        print("Ошибка: введите число от 4 до 20.")

# ======== Вычисление координат ========
def calculate_side_length(number, size):
    return size/(number+0.5)

def calculate_hexagon_centers(number, size):
    side = calculate_side_length(number, size)
    width_hex = math.sqrt(3) * side
    total_width = width_hex * number
    total_height = side * 1.5 * number
    start_x = -total_width / 2 + width_hex / 2
    start_y = total_height / 2 - side / 2
    centers = []
    for row in range(number):
        y = start_y - row * side * 1.5
        for col in range(number):
            x = start_x + col * width_hex
            if row % 2 == 1: x += width_hex / 2
            centers.append((x, y))
    return centers, side


# ======== Предпросмотр цветов ========
def preview_colors(color1, color2):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.bgcolor("white")

    def draw_square(x, y, color, label):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x + 50, y - 30)
        turtle.color("black")
        turtle.write(label, align="center", font=("Arial", 14, "normal"))

    draw_square(-150, 50, color1, f"Цвет 1: {color1}")
    draw_square(50, 50, color2, f"Цвет 2: {color2}")
    turtle.penup()
    turtle.goto(0, -100)
    turtle.write("Нажмите Enter в консоли, чтобы начать рисование",
                 align="center", font=("Arial", 14, "italic"))
    input("\nНажмите Enter, чтобы начать рисование...")


# ======== Рисование шестиугольников ========
color_map = {
    'красный': 'red', 'оранжевый': 'orange', 'желтый': 'yellow', 'зеленый': 'green',
    'синий': 'blue', 'фиолетовый': 'purple', 'розовый': 'pink', 'черный': 'black',
    'серый': 'gray', 'белый': 'white', 'коричневый': 'brown'
}


def draw_shadow(x, y, side, shadow_intensity):
    if shadow_intensity == 0: return
    shadow_x = x + shadow_intensity
    shadow_y = y - shadow_intensity
    turtle.penup()
    turtle.goto(shadow_x, shadow_y)
    turtle.pendown()
    turtle.fillcolor("#686868")
    turtle.begin_fill()
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.end_fill()
    turtle.setheading(0)


def draw_hexagon(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.end_fill()
    turtle.setheading(0)


def draw_hexagon_border(x, y, side, thickness, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color_map.get(color, "black"))
    turtle.pensize(thickness)
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.setheading(0)
    turtle.pensize(1)


# ======== Шаблоны заливки ========
def chess_pattern(N: int, color_first: str, color_second: str):
    colors = []
    for row in range(N):
        color = color_first if row % 2 == 0 else color_second
        for col in range(N):
            colors.append(color)
            color = color_second if color == color_first else color_first
    return colors


def alternation(N: int, type: str, color_first: str, color_second: str):
    colors = []
    if type == "по строкам":
        for i in range(N):
            for col in range(N):
                colors.append(color_first if i % 2 == 0 else color_second)
    else:
        for col in range(N ** 2):
            colors.append(color_first if col % 2 == 0 else color_second)
    return colors


def chose_pattern_check():
    patterns = ['шахматный', 'чередование цветов']
    print('Варианты заливки: шахматный, чередование цветов')
    while True:
        pattern = input('Выберите вариант заливки:').strip().lower()
        if pattern in patterns: return pattern
        print('Ошибка ввода.')


def chose_type_check():
    types = ['по строкам', 'по столбцам']
    print('Варианты заливки: по строкам, по столбцам')
    while True:
        type = input('Выберите вариант заливки:').strip().lower()
        if type in types: return type
        print('Ошибка ввода.')

def pattern_colors(N: int, color_first: str, color_second: str, pattern: str, type: str):
    if pattern == 'шахматный':
        return chess_pattern(N, color_first, color_second)
    if pattern == 'чередование цветов':
        return alternation(N, type, color_first, color_second)

# ======== Анимация ========
def animate_drawing(centers: list, colors: list, side: float,
                    thickness_width: int, color_bord: str, shadow_intensity: int):
    turtle.tracer(0, 0)
    for i in range(len(centers)):
        x, y = centers[i]
        color = colors[i]
        if shadow_intensity > 0: draw_shadow(x, y, side, shadow_intensity)
        draw_hexagon(x, y, side, color)
        draw_hexagon_border(x, y, side, thickness_width, color_bord)
        turtle.update()
        time.sleep(0.05)
    turtle.tracer(1, 10)

# ======== Главная функция ========
def main():
    turtle.setup(800, 800)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    N = get_num_hexagons()
    color_first, color_second = get_color_choice()
    preview_colors(color_first, color_second)
    thickness_width = border_thickness()
    color_bord = border_color()
    shadow_intensity = shadow_brightness()
    size = 500

    centers, side = calculate_hexagon_centers(N, size)

    pattern = chose_pattern_check()
    if pattern == 'чередование цветов':
        type = chose_type_check()
    else:
        type = ""
    colors = pattern_colors(N, color_first, color_second, pattern, type)

    animate_drawing(centers, colors, side, thickness_width, color_bord, shadow_intensity)
    turtle.done()


if __name__ == '__main__':
    main()

