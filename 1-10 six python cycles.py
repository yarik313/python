#Задание 1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]

for name in names:
   print(f"Hello {name}!")
    
#Задание 2
phrase = "I'm learning cycles."
for x in range(10+1):
    print(phrase) 

#Задание 3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for station in stations:
  print(f"Поезд на станции: {station}")
  if station == stations[-1]:

     print("Конечная! Звягино")

#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]

for item in shop:
    if item == "Laptop":
        print("I'm buying this.")
    else:
        print("I don't need it.")

#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате", "Подготовить отчёт"]
for i, task in enumerate(tasks,start=1):
    if ("Важная") in task:
        print(f"{i}!: {task.replace( '(Важная)','')}")
    else:
            print(f"{i}: {task}")
            
#Задание 6
n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    numbers += [number] 
print("Список всех введённых чисел:", numbers)
print("Сумма всех чисел:", sum(numbers))

#Задание 7
count = 0
while count < 10:
    print(f"Цикл сработал {count} раз")
    count += 1

#Задание 8
while True:
    command = input("Введите команду (w, a, s, d, stop): ") #stop - если хочешь остановить это безумие!!!
     
    if command == "w":
        print("Персонаж идёт вперёд")
    elif command == "a":
        print("Персонаж идёт влево")
    elif command == "s":
        print("Персонаж идёт назад")
    elif command == "d":
        print("Персонаж идёт вправо")
    elif command == "stop":
        print("Программа завершена")
        break
    else:
        print("Неверная команда. Попробуйте ещё раз.")
#Задание 9
while True:
    number = int(input("Введите число от 1 до 9: "))
    if 1 <= number <= 9:
        print(f"Таблица умножения для числа {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")
        break
    else:
        print("Число вне диапазона. Попробуйте ещё раз.")
#Задание 10
riddle = "Что можно увидеть с закрытыми глазами?"
correct_answer = "сон"
attempts = 3

while attempts > 0:
    answer = input("Что можно увидеть с закрытыми глазами? ")

    if answer.lower() == correct_answer:
        print("Поздравляю! Вы угадали.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неправильно. Осталось попыток: {attempts}")
        else:
            print("К сожалению, попытки закончились. Правильный ответ: сон.")

            


