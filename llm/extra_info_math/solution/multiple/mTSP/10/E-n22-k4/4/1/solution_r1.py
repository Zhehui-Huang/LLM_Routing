import pulp
import math

# Define the cities coordinates
cities = {
    0: (145, 215),
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

n = len(cities)  # total number of nodes including the depot
m = 4  # number of vehicles

# Function to compute Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Setup the problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat="Binary")

# Objective function: minimize the total travel cost
problem += pulp.lpSum(x[i, j, k] * distance(i, j) for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints

# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation - each vehicle enters and leaves each city
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Each vehicle must leave from and return to the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(n) if j != 0) == 1
    problem += pulp.lpMakerSum(x[j, 0, k] for j in youngsters if j != 0) == 1

# Subtour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat="Continuous")
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
problem.solve()

# Output the results
for k in range(m):
    tour = [0]
    while len(tour) < n/m + 1:
        i = tour[-1]
        next_city = [j for j in range(n) if j!= i and x[i, j, k].value() == 1]
        if next_city:
            tour.append(next_city[0])
    tour.append(0)
    cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

# Overall cost calculation
overall_cost = sum(distance(tour[i], tour[i+1]) for k in range(m) for tour in tours for i in range(len(tour)-1))
print(f"Overall Total Travel Cost: {overall_cost}")