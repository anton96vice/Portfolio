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
