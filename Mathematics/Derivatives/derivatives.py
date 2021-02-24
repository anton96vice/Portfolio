#Importing sympy
from matplotlib import pyplot as plt
import math #needed for definition of pi
import sympy as sp
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# create a "symbol" called x
x = sp.Symbol('x')
y = sp.Symbol('y')
#Define function
f = x**2
 
#Calculating Derivative
derivative_f = f.diff(x)
 
derivative_f
#find derivative at point x1
def solve_eqv(eq, x1):
  f1 = sp.lambdify(x, sp.diff(eq))
  answer = f1(x1)
  return print("derivative of ", eq, "is ", answer, "at point ", x1)

#find a y1 given x0, x1, equation
def solve_eq(x0,y0,x1, eq, x_der = None):
  der = sp.diff(eq)
  deltaX = x1-x0
  f = y0 + (der * deltaX)
  lamb = sp.lambdify(x, f)
  y1 = lamb(x1)
  try:
    f = sp.lambdify(x, der)
    func = f(x_der)
    print(f"derivative at x_der = {func}")
  except:
    print("derivative at x_der not selected")
  print(f"x0 = {x0},\n  x1 = {x1}, \n y0 = {y0},\n y1 ={y1}, \n derivative of function {eq} is {der}, \n deltaX = {deltaX}")
  
  
  #Graph
  def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()
