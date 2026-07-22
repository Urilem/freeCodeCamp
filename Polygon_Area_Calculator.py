class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, width: int) -> None:
        self.width = width
    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height
    def get_perimeter(self) -> float:
        return 2*(self.width + self.height)
    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5
    def get_picture(self) -> str:
        shape = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        for i in range(self.height):
            for j in range(self.width):
                shape += '*'
            shape += '\n'
        return shape
    def get_amount_inside(self, shape) -> int:
        horizontal = self.width // shape.width
        vertical = self.height // shape.height

        return horizontal * vertical

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.side = side

    def set_side(self, side: float) -> None:
        self.side = side
        self.width = side
        self.height = side
    def set_width(self, side: float) -> None:
        self.set_side(side)
    def set_height(self, side: float) -> None:
        self.set_side(side)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(side={self.side})'

#Example usage:
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))