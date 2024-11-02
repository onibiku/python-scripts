import math

l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle with length {l} and width {w} is: {l*w}")

r = float(input("Enter the radius of the circle: "))
area = round(r**2 * math.pi, 2)
print(f"The area of the circle with radius {r} is: {area}")

b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
print(f"The area of the triangle with base {b} and height {h} is: {b*h/2}")

