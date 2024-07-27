import pulp
from math import sqrt
import itertools

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Define the problem
problem = pulp.LpProblem("MinimizeMaximumDistance", pulp.LpMinimize)

n = len(cities)
x_vars = {}
c_ij = {}

# Objective function helper variable Z
Z = pulp.LpVariable("Z", lowBound=0, cat=pulp.LpContinuous)

# Create variables and c_ij dict
for i in range(n):
    for j in range(n):
        if i != j:
            xij_name = f"x_{i}_{j}"
            x_vars[(i, j)] = pulp.LpVariable(xij_name, cat=pulp.LpBinary)
            c_ij[(i, j)] = euclidean_distance(i, j)
            problem += Z >= c_ij[(i, j)] * x_vars[(i, j)]  # Part of objective function

# Objective function
problem += Z, "Minimize the maximum distance"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x_vars[(i, j)] for j in range(n) if i != j) == 1, f"Sum out of city {i}"
    problem += pulp.lpSum(x_vars[(j, i)] for j in range(n) if i != j) == 1, f"Sum into city {i}"

# Subtour elimination constraints
for m in range(2, n):
    for s in itertools.combinations(range(1, n), m):  # Avoid depot
        problem += pulp.lpSum(x_vars[(i, j)] for i in s for j in s if i != j) <= len(s) - 1, f"SubtourConstraint_{s}"

# Solve the problem
status = problem.solve()

# Analyze the solution
if status == pulp.LpStatusOptimal:
    tour = []
    arcs = [(i, j) for i in range(n) for j in range(n) if pulp.value(x_vars[(i, j)]) == 1 and i != j]

    current_city = 0
    tour.append(current,policy_city)
    for _ in range(n-1):
        # Find next city
        for i, j in arcs:
            if i == current_city:
                current_city = j
                tour.append(current_city)
                break
    
    tour.append(0)  # Complete the tour by returning to the depot
    
    total_cost = sum(c_ij[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(c_ij[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No optimal solution found.")