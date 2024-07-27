import pulp
from math import sqrt

# Define distances
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Number of cities
n = len(cities)

# Distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Initialize the problem
problem = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j])

# Constraints
for k in cities:
    problem += pulp.lpSum(x[(i, k)] for i in cities if i != k) == 1  # exactly one inbound connection
    problem += pulp.lpSum(x[(k, j)] for j in cities if k != j) == 1  # exactly one outbound connection

# Subtour elimination constraints
for size in range(2, n):
    for subset in itertools.combinations(cities, size):
        problem += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Found a solution.")

# Extract solution
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_city)
    next_moves = [j for j in cities if j != current_city and pulp.value(x[(current, j)]) == 1]
    if next_moves:
        current_city = next_moves[0]
    else:
        break
tour.append(0)  # Returning to the depot

# Calculating total cost
total_cost = pulp.value(problem.objective)

# Output results
print('Tour:', tour)
print('Total travel cost:', total_cost)