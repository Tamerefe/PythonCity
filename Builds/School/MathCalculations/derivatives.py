import sympy as sym 

x = sym.Symbol('x')

f = input("Enter a function in terms of x: ")

derivative = sym.diff(f, x)
print(derivative)