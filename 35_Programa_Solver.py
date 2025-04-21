import pulp as p 
Lp_prob = p.LpProblem('Problem1',p.LpMaximize)

# Decision Variables
x1 = p.LpVariable("X1", lowBound = 0) #Create a variable X1 >= 0
x2 = p.LpVariable("X2", lowBound = 0) #Create a variable X2 >= 0
x3 = p.LpVariable("X3", lowBound = 0) #Create a variable X3 >= 0

# Objective function
Lp_prob += 1600 * x1 + 1300 * x2 + 600 * x3

#Constraints
Lp_prob += 2 * x1 + 1.5 * x2 + x3 <= 20 #Create constrains a variable X1
Lp_prob += 2 * x1 + x2 + 1.5 * x3 <= 24 #Create constrains a variable X2
Lp_prob += x1 + 2 * x2 + 0.5 * x3 <= 20 #Create constrains a variable X3

print(Lp_prob)

#Solving the linear programming problem

status = Lp_prob.solve()
print(p.LpStatus[status]) 

#Solution
p.solve(x1)
    #4.0
