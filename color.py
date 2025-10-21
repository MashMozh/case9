print('Доступные цвета: красный, оранжевый, желтый, '
      'зеленый, синий, фиолетовый, розовый, черный, серый, белый')


def get_color_choice(color):
    available_colors = ['красный', 'оранжевый', 'желтый', 'зеленый',
                        'синий', 'фиолетовый', 'розовый', 'черный',
                        'серый', 'белый']
    while color not in available_colors:
        color = input('Ошибка ввода цвета. Пожалуйста, повторите попытку: ')
    return color


color_first = input('Выберите первый цвет из предложенных выше: ')
color_first = get_color_choice(color_first)

color_second = input('Выберите второй цвет из предложенных выше: ')
color_second = get_color_choice(color_second)






color_second = input('Выберите второй цвет из предложенных выше: ')
color_second = get_color_choice(color_second)





