import pulp
import math

# Cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
n = len(cities)

# Distance calculation (Euclidean)
def get_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Problem setup
problem = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += d_max

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * get_distance(cities[i], cities[j]) <= d_max

# Subtour elimination constraint
for s in range(2, n):
    subsets = combinations(range(n), s)
    for subset in subsets:
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour from the variables
path = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]

# Reconstruct the path in a readable format and calculate costs
tour = [0]
current = 0
while len(tour) < n:
    for j in range(n):
        if (current, j) in path:
            tour.append(j)
            current = j
            break
tour.append(0)  # return to depot

# Calculate the total cost and max distance
total_cost = sum(get_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(get_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", pulp.value(d_max))