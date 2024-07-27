import pulp
from math import sqrt

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

# Create variables
for i in range(n):
    for j in range(n):
        if i != j:
            x_vars[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, cat='Binary')
            c_ij[(i, j)] = euclidean_distance(i, j)

# Objective function: minimize the maximum distance in the tour
Z = pulp.LpVariable("Z", lowBound=0, cat='Continuous')
problem += Z

for i, j in x_vars:
    problem += Z >= c_ij[(i, j)] * x_vars[(i, j)]

# Constraints
for i in range(n):
    problem += pulp.lpSum(x_vars[(i, j)] for j in range(n) if j != i) == 1  # Leave from each city
    problem += pulp.lpSum(x_vars[(j, i)] for j in range(n) if j != i) == 1  # Arrive at each city

# Subtour Elimination Constraints (SEC)
for m in range(2, n):
    for s in itertools.combinations(range(1, n), m):  # avoid using depot in subsets
        problem += pulp.lpSum(x_vars[(i, j)] for i in s for j in s if i != j) <= len(s) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    print("Optimal solution found!")
    
    # Extract the tour
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x_vars[(i, j)]) == 1]
    
    # Find the sequence of the tour starting from depot 0
    tour = [0]
    while len(tour) < n:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                edges.remove((i, j))
                break
    tour.append(0)  # Return to depot

    # Calculate the cost and max distance
    total_cost = sum(c_ij[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_dist = max(c_ij[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No optimal solution found.")