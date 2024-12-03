#ЗАДАНИЕ-1
def create_car(brand, color, max_speed):
    return f"Марка: {brand} Цвет: {color} Максимальная скорость: {max_speed} км/ч"

car_description = create_car("Toyota", "красный", 180)
print(car_description)

#ЗАДАНИЕ-2
def switch_check(switch):
    if switch is True:
        print("True работает")
    elif switch is False:
        print("False не работает")
    else:
        print(f"{switch} сломан.")

switch_1 = True # работающий переключатель
switch_2 = False # неработающий переключатель
switch_3 = None # переключатель сломан

# Проверка каждого переключателя
switch_check(switch_1)
switch_check(switch_2)
switch_check(switch_3)

#ЗАДАНИЕ-3
def triangle_properties():
    a, b, c = 15, 10, 15 # Длины сторон треугольника
    
    print(f"Длина сторон треугольника: {a}, {b}, {c}")
    
    # Проверка, можно ли построить треугольник
    if a + b > c and a + c > b and b + c > a:
        # Определение типа треугольника
        if a == b == c:
            triangle_type = "равносторонний треугольник"
        elif a == b or a == c or b == c:
            triangle_type = "равнобедренный треугольник"
        else:
            triangle_type = "разносторонний треугольник"
        
        print(f"Информация: {triangle_type}")
        
        # Вычисление периметра
        p = a + b + c
        print(f"Периметр: {p}")
        
        # Вычисление площади по формуле Герона
        s = p / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"Площадь: {area:.2f}")
    else:
        print("Информация: некорректные стороны. Невозможно построить треугольник.")

# Вызов функции с заданными сторонами
triangle_properties()

#ЗАДАНИЕ-4
def number_change(input_number, output_number):
    steps = 0 # Счётчик шагов
    
    # Пока input_number не равно output_number, продолжаем менять input_number
    while input_number != output_number:
        if input_number < output_number:
            input_number += 1 # Увеличиваем на 1
        else:
            input_number -= 1 # Уменьшаем на 1
        steps += 1 # Увеличиваем счётчик шагов
    
    return (steps, input_number, output_number)

# Пример использования функции
print(number_change(2, 10)) # (8, 10, 10)
print(number_change(5, 1)) # (4, 1, 1)
print(number_change(3, 3)) # (0, 3, 3)

#ЗАДАНИЕ-5
# Глобальная переменная
player = 0

# Функция для отображения текущего пробега игрока
def info_player():
    global player
    print(f"Игрок пробежал {player} км.")

# Функция для добавления пробега
def run_player(km):
    global player
    player += km / 2 # Добавляем половину пробега

# Проверка работы программы
info_player() # Вывод начального значения
run_player(30) # Игрок пробежал 30 км (учитывается 15 км)
run_player(12.5) # Игрок пробежал 12.5 км (учитывается 6.25 км)
info_player() # Вывод итогового значения

#ЗАДАНИЕ-6

def analyze_number(number: float) -> str:

    if not isinstance(number, (int, float)):
        return "Ошибка: входное значение не является числом."

    is_positive = number > 0
    is_integer = isinstance(number, int) or number.is_integer() # Проверка целостности числа
    square = number ** 2

    return (f"Число: {number}\n"
            f"Положительное: {is_positive}\n"
            f"Целое: {is_integer}\n"
            f"Квадрат: {square}")

# Пример использования:
print(analyze_number(-3)) # Анализ отрицательного числа
print(analyze_number.__doc__) # Вывод документации функции
print(analyze_number(5.5)) # Анализ положительного числа
print(analyze_number("текст")) # Ошибка при передаче строки