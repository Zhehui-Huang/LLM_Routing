import pulp
import math

# City coordinates
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

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# TSP model
tsp_model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
tsp_model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# 1. Each city is left exactly once
for i in range(1, n):
    tsp_model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# 2. Each city is entered exactly once
for j in range(1, n):
    tsp_model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# 3. Subtour elimination (using additional constraints)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=1, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            tsp_model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve problem
tsp_model.solve()

# Extract tour
tour = [0]
total_cost = 0

for _ in range(n-1):
    current = tour[-1]
    next_city = [j for j in range(n) if pulp.value(x[current, j]) == 1][0]
    tour.append(next_city)
    total_cost += distances[current][next_city]

tour.append(0)  # Return to depot
total_cost += distances[tour[-2]][0]  # Add the distance from last city back to the depot

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")