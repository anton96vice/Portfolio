# Optimization Problems and their solutions:
![problem1](https://github.com/anton96vice/Portfolio/blob/main/Projects/Mathematics/Optimization/Problems/Screen%20Shot%202021-02-24%20at%203.17.34%20AM.png)
### Solution:
 [solution](https://github.com/anton96vice/Portfolio/blob/main/Projects/Mathematics/Optimization/Problems/Warehouse-Mall/optimize_1.py)
  import cvxpy
  c = np.array([[2,5,3],[7,7,6]])
  y = cvxpy.Variable(shape=(2,3), integer = True)
  constraint = [cvxpy.sum(y[0]) <= 180, 
              cvxpy.sum(y[1]) <= 220, 
              cvxpy.sum(y[:, 0]) == 110, 
              cvxpy.sum(y[:, 1]) == 150, 
              cvxpy.sum(y[:, 2]) == 140, 
              y >= 0]
  total_value = cvxpy.sum(cvxpy.multiply(y,c))
  problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=constraint)
  print(problem.solve(), y.value)
