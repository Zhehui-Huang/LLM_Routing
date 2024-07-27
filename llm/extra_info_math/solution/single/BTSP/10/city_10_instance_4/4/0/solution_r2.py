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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Creating the LP problem
problem = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Variables
x_vars = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
          for i in cities for j in cities if i != j}
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective Function
problem += z

# Constraint: Max distance minimization condition
for i, j in x_vars:
    problem += z >= x_vars[i, j] * euclidean_distance(i, j)

# Adding constraints: exactly one exit from each city and one entry to each city
for k in cities:
    problem += pulp.lpSum(x_vars[i, j] for i, j in x_vars if i == k) == 1  # sum of rows = 1
    problem += pulp.lpSum(x_vars[i, j] for i, j in x_vars if j == k) == 1  # sum of cols = 1

# Subtour elimination
for s in range(2, len(cities)):
    for subset in itertools.combinations(cities.keys(), s):
        if 0 in subset:  # include the depot in subsets
            problem += pulp.lpSum(x_vars[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Check if we have an optimal solution
if pulp.LpStatus[problem.status] == "Optimal":
    print("Optimal solution found!")

    # Build the optimal tour path
    path = []
    current = 0
    while True:
        path.append(current)
        current = next(j for i, j in x_vars if i == current and pulp.value(x_vars[i, j]) == 1)
        if current == 0:
            break
    
    path.append(0) # Close the tour
    
    # Calculate the total distance and maximum edge distance
    total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path)-1))
    max_distance = max(euclidean_distance(path[i], path[i+1]) for i in range(len(path)-1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No optimal solution could be found.")