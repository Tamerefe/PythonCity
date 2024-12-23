import sympy as sp 

x = sp.symbols('x')
f = sp.log(x, 2)
h = sp.integrate(f, x)

print(h) # x*log(x) - x