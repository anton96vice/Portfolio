#minimization function utilizing Lagrange method
# Problem:
#НFind square distance from point (2,1) to straight line x+y=1  with lagrange
import sympy as sp

#min((x-2)^2+(y-1)^2) with x+y-1=0


x,y,z = sp.symbols('x y z')
L = (x-2)**2 + (y-1)**2 +z*(x+y-1)
derivatives = list()
for i in symbols:
  derivatives.append(sp.diff(L,i))
solution = sp.solve([x for x in derivatives], symbols)
f = sp.lambdify([x,y,z],L)
f(1,0,2)
# Out: 2
