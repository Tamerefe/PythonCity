def hipo(a, b, c):
	if a**2 + b**2 == c**2:
		return "One angle of this triangle is 90 degrees!"
	else:
		return "No angle of this triangle is 90 degrees!"

def triangle_type(a, b, c):
	if a == b == c:
		return "This is an equilateral triangle."
	elif a == b or b == c or a == c:
		return "This is an isosceles triangle."
	else:
		return "This is a scalene triangle."

def perimeter(a, b, c):
	return a + b + c

a = int(input('Enter the first side: '))
b = int(input('Enter the second side: '))
c = int(input('Enter the third side: '))

print(hipo(a, b, c))
print(triangle_type(a, b, c))
print(f"The perimeter of the triangle is: {perimeter(a, b, c)}")