#Задание 1
# Запрос возраста пользователя
age = int(input("Введите ваш возраст: "))
# Определение категории по возрасту
if age < 18:
    print("Вы несовершеннолетний")
elif 18 <= age <= 65:
    print("Вы трудоспособный человек")
else:
    print("Вы пенсионер")
    
#Задание 2
# Запрос суммы покупки
price = int(input("Введите сумму покупки: "))
# Определение скидки по сумме
if price < 1000:
    print("Скидка не продоставляется")
elif 1000 <= price <= 5000:
    print("Скидка 5%")
if price > 5000:
    print("Скидка 10%")
    
#Задание 3
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль!"
else:
    result = "Неверная операция."
print(result)

#Задание 4
# Ввод числа от пользователя
number = int(input("Введите число: "))
# Проверка условия
if number % 2 == 0 and (number % 10 == 2 or number % 10 == 6):
    print(True)
else:
    print(False)

#Задание 5
# Установленный пароль
correct_password = "123"
# Ввод пароля от пользователя
user_password = input("Введите пароль: ")
# Проверка пароля
if user_password == correct_password:
    print("Доступ разрешен.")
else:
    print("Неверный пароль.")

#Задание 6
#Ввод координат квадрата
squre = str(input("Введите координаты:"))
blue_parrot = ["B1","B3","B7","C4","C8","C1","C5","C6","C9"]
green_parrot = ["B2","B6","B8","B4","C2","C7","C10","C11"]
noone = ["B5","C3","C12"]
#Проверка условия
if squre in blue_parrot:
    print("На этом квадрате сидит синий попугай")
if squre in green_parrot:
    print("На этом квадрате сидит зелёный попугай")
if squre in noone:
    print("На этом квадрате никто не сидит")

#Задание 7
# Ввод чисел n и k от пользователя
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
# Проверка кратности
if k != 0: # Проверяем, чтобы k не было равным 0
    if n % k == 0:
        print(f"{n} кратно {k}.")
    else:
        print(f"{n} не кратно {k}.")
else:
    print("На 0 делить нельзя.")

#Задание 8
# Ввод уровня и здоровья от пользователя
#Используем функцию исключения
try:
    level = int(input("Введите уровень игрока: "))
    health = int(input("Введите состояние здоровья игрока: "))

    # Проверка корректности данных
    if level < 0 or health < 0 or health > 100:
        print("Некорректные данные.")
    else:
        # Проверка уровня игрока
        if level < 5:
            print("Ваш уровень слишком низкий для выполнения миссии.")
        else:
            # Проверка состояния здоровья
            if health > 50:
                print("Вы готовы к миссии!")
            elif 20 <= health <= 50:
                print("Ваше здоровье низкое, будьте осторожны.")
            else: # health < 20
                print("Ваше здоровье слишком низкое для выполнения миссии.")
except ValueError:
    print("Некорректные данные.")
    
#Задание 9
# Изначальный инвентарь игрока
inventory = ["яблоко", "шариковая ручка"]
# Проверка наличия необходимых предметов
has_key = "ключ" in inventory
has_flashlight = "фонарь" in inventory
# Условия проверки
if has_key and has_flashlight:
    print("Вы можете пройти через дверь.")
elif not has_key and not has_flashlight:
    print("У вас нет ни ключа, ни фонаря, вы не можете пройти через дверь.")
elif not has_key:
    print("У вас нет ключа, вы не можете открыть дверь.")
elif not has_flashlight:
    print("У вас нет фонаря, слишком темно, чтобы пройти.")

#Задание 10
# Фразы разных персонажей
king = "Enemies are coming! Are the archers ready?"
warrior = "For the Alliance!"
magician = "The spell is ready."

# Список фраз
phrases = [king, warrior, magician]

# Проверка и вывод результата для каждой фразы
for phrase in phrases:
    if phrase.endswith('?'):
        print(f"Фраза: '{phrase}' заканчивается на '?'.")
    elif phrase.endswith('!'):
        print(f"Фраза: '{phrase}' заканчивается на '!'.")
    else:
        print(f"Фраза: '{phrase}' не заканчивается на '!' или '?'.")
