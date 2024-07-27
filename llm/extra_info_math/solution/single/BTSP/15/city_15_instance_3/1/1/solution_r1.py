import pulp
import math

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities
n = len(cities)

# LP problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective
prob += z, "Minimize the maximum distance between consecutive cities"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * calc_distance(i, j) <= z, f"Max_distance_constraint_{i}_{j}"

# Solution
prob.solve()

# Check if a valid solution exists
if prob.status == 1:
    # Extract tour following x variables
    tour = []
    cur = 0
    while len(tour) < n:
        tour.append(cur)
        cur = next(j for j if x[cur, j].varValue == 1)
    
    tour.append(0)  # closing the tour back to the depot
    
    # Calculate the objective values
    total_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_distance = max(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    # Maximum distance is simply the minimized objective value z
    print("Maximum distance between consecutive cities:", round(pulp.value(z), 2))
else:
    print("Failed to find a valid solution.")