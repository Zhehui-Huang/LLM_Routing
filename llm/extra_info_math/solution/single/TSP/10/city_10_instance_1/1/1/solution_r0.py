import pulp
import numpy as np

# Define city coordinates (0-based index where index 0 is the depot)
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities including the depot
n = len(cities)

# Euclidean distance calculator
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Computing cost matrix
cost = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost[(i, j)] = euclidean distance(cities[i], cities[j])
        else:
            cost[(i, j)] = 0

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", cost.keys(), cat=pulp.LpBinary)

# Objective function: minimize the total travel cost
problem += pulp.lpSum(cost[i, j] * x[i, j] for i, j in cost.keys()), "Total Travel Cost"

# Constraints
# Each city is left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"

# Each city is entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"Enter_city_{j}"

# Subtour elimination constraints using additional variables and constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Interpret the results
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(current_city)
    current_city = next_city
tour.append(0)  # return to the depot

total_cost = pulp.value(problem.objective)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)