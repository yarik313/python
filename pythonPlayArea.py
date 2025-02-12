class Shape:
    """Базовый класс для всех геометрических фигур."""
    def __init__(self, side):
        # Храним сторону фигуры
        self.side = side

    def area(self):
        """Метод для вычисления площади фигуры."""
        return self.side * self.side

class Square(Shape):
    """Подкласс для квадрата."""
    pass

class Circle(Shape):
    """Подкласс для круга."""
    def __init__(self, radius):
        # Вызываем конструктор базового класса с радиусом
        super().__init__(radius)
        # Храним радиус круга
        self.radius = radius

    def area(self):
        """Метод для вычисления площади круга."""
        return 3.14159 * self.radius ** 2
        
# Создание объектов геометрических фигур
shape_square = Square(5)
shape_circle = Circle(5)

# Вывод площадей
print(f"Площадь квадрата со стороной {shape_square.side}: {shape_square.area():.2f}")
print(f"Площадь круга с радиусом {shape_circle.radius}: {shape_circle.area():.2f}")



class Guitar:
    """Класс для игры на гитаре."""
    def __init__(self, method):
        # Храним метод воспроизведения
        self.method = method

    def play(self):
        """Метод для воспроизведения звука."""
        print("Проигрываем мелодию")
        if self.method == 'A':
            print("Мелодия A")
        elif self.method == 'B':
            print("Мелодия B")
        else:
            raise ValueError('Неизвестный метод воспроизведения')

class Piano:
    """Класс для игры на фортепиано."""
    def __init__(self, method):
        # Храним метод воспроизведения
        self.method = method

    def play(self):
        """Метод для воспроизведения звука."""
        print("Проигрываем мелодию")
        if self.method == 'C':
            print("Мелодия C")
        elif self.method == 'D':
            print("Мелодия D")
        else:
            raise ValueError('Неизвестный метод воспроизведения')
            
# Создание объектов музыкальных инструментов
guitar = Guitar('A')
piano = Piano('C')

# Воспроизведение звуков
guitar.play()
piano.play()