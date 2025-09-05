class rectangle: 
    def __init__(self, height: int, width: int):
        self.width = width
        self.height = height

    def area(self) -> int : 
        return self.width * self.height
    
    def discribe(self) -> None:
        print(f"Rectangle {self.width} by {self.height}")
import cmath
class triangle: 
    def __init__(self, tlength: int, twidth: int):
        self.height = twidth
        self.length = tlength
        self.hyp = cmath.sqrt(((twidth * twidth) + (tlength * tlength)))
    def area(self) -> int :
        return 1/2 * (self.height * self.length)
    def hypotenuse(self) -> float :
        return self.hyp
    def discribe(self) -> None:
        print(f"Triangle with length {self.length}, height {self.height}, and hypotenuse {self.hyp}")
class circle: 
    def __init__(self, radius: int):
        self.radius = radius
    def area(self) -> float :
        return cmath.pi * 2 * self.radius
    def discribe(self) -> None :
        print(f"Circle with radius {self.radius} and area {circle.area()}")
