from HW_9 import rectangle
from HW_9 import triangle
from HW_9 import circle

def convtoinch(centimeters: float) -> float:
    return centimeters * 0.393701
def convtocm(inches: float) -> float:
    return inches * 2.54
def comparea(area1: float, area2:float) -> None:
    a1greater = True
    if area1 > area2:
        a1greater = True
    else:
        a1greater = False
    return a1greater