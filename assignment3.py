
# Find if a triangle is right angled
x = float(input("Enter side x: "))
y = float(input("Enter side y: "))
z = float(input("Enter side z: "))
def right_angled_triangle(x, y, z):
if x*x + y*y == z*z:
return True
else:
return False
if right_angled_triangle(x, y, z):
print("The triangle is right angled")
else:
print("The triangle is not right angled")
