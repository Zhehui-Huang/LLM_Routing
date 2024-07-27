import math
import pulp

# Define cities and their coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Compute Euclidean distances between cities
def euclidean(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create distances dictionary
n = len(coordinates)
distances = {(i, j): euclidean(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Create the problem
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(2)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective
problem += pulp.lpSum(x[i, j, k] * distances[i, j] for i in range(n) for j in range(n) if i != j for k in range(2))

# Constraints
# Ensure that every city except depot is visited exactly once by any robot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(2)) == 1

# Each robot begins and ends at the depot
for k in range(2):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpShiftSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(2):
                problem += u[i] - u[j] + n * x[i, j, k] <= n-1

# Solve the problem
problem.solve()

# Extract tours and calculate costs
tours = {k: [] for k in range(2)}
costs = {k: 0 for k in range(2)}

for k in range(2):
    tour = [0]  # start from the depot
    while True:
        next_cities = [j for j in range(n) if x[tour[-1], j, k].varValue == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tours[k].append(next_city)
        costs[k] += distances[tour[-1], next_city]
        tour = tours[k]
    tours[k].append(0)  # return to the depot
    costs[k] += distances[tour[-1], 0]

# Output results
for k in range(2):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

max_cost = max(costs.values())
print(f"Maximum Travel Cost: {max_cost}")