import math
class Polygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def calculate_area(self):
        apothem = self.length / (2 * math.tan(math.pi / self.sides))
        perimeter = self.sides * self.length
        area_value = 0.5 * apothem * perimeter
        return area_value

while True:
    sides = int(input("Enter the number of sides in your polygon: "))
    if sides < 3:
        print("A Polygon must have at least 3 sides.")
        continue
    else:
        break

while True:
    length = float(input("Enter the length of a side: "))
    if length <= 0:
        print("Length must be greater than 0.")
        continue
    else:
        break

poly = Polygon(sides, length)
result = poly.calculate_area()
perimeter = sides * length

print(f"The area of your polygon is: {result:.1f}")
print(f"\nThe perimeter of your polygon is {perimeter}")