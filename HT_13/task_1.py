# 1. Напишіть програму, де клас «геометричні фігури» (Figure)
# містить властивість color з початковим значенням white і метод
# для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
# завдання початкових розмірів об'єктів при їх створенні.

class Figure:
    def __init__(self):
        self._color = 'white'

    @property
    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color


class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def __str__(self):
        return f"Oval - Color: {self.color}, Width: {self.width}, Height: {self.height}"


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def __str__(self):
        return f"Square - Color: {self.color}, Side Length: {self.side_length}"


oval_obj = Oval(5, 10)
square_obj = Square(7)

print(oval_obj)
print(square_obj)

oval_obj.set_color('blue')
square_obj.set_color('red')

print(oval_obj.color)
print(square_obj.color)
