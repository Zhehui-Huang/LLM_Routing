import pulp
import math

# Given cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20),  2: (79, 69),  3: (17, 20),
    4: (18, 61), 5: (40, 57),  6: (57, 30),  7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60),  11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Euclidean distance between two points
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Prepare data
n = len(cities)
distances = [[euclidean_dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Problem setup
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] is 1 if we travel from i to j
x = [[pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for j in range(n)] for i in range(n)]
y = pulp.LpVariable("max_distance", lowBound=0, cat="Continuous")

# Objective function
prob += y, "Minimize the maximum distance between consecutive cities"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if j != i) == 1, f"From_City_{i}"
    prob += pulp.lpSum(x[j][i] for j in range(n) if j != i) == 1, f"To_City_{i}"

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i][j] + x[j][i] <= 1

# Enforce distance constraints and prevent self-loops
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * distances[i][j] <= y

prob.solve()

# Extract the solution and the path
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_city)
    for next_city in range(n):
        if pulp.value(x[current_city][next_city]) == 1:
            current_city = next_city
            break
tour.append(0)  # returning to the depot

# Calculate tour details
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")