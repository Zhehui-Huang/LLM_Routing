import pulp as pl
import math

# Define the cities and their positions
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 
    3: (86, 92), 4: (54, 93), 5: (34, 73), 
    6: (6, 61), 7: (86, 69), 8: (30, 50), 
    9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = len(cities)
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Define problem
prob = pl.LpProblem("Minimax_TSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
z = pl.LpVariable("z", lowBound=0)

# Objective
prob += z

# Constraints
for i in cities:
    prob += pl.lpSum(x[(i, j)] for j in cities if i != j) == 1
    prob += pl.lpSum(x[(j, i)] for j in cities if i != j) == 1

for i in cities:
    for j in cities:
        if i != j:
            prob += x[(i, j)] * distances[(i, j)] <= z

# Subtour elimination constraints
for S in range(3, n):  # Generate all subsets of the node set of size >= 3
    for subset in pl.combination(cities.keys(), S):
        prob += pl.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve problem
prob.solve()

# Output
tour = []
current_city = 0
remaining_cities = set(cities.keys()) - {0}
while remaining_cities:
    for j in remaining_cities:
        if pl.value(x[(current_city, j)]) == 1:
            tour.append(j)
            remaining_cities.remove(j)
            current_city = j
            break

# Add depot city to complete the tour
tour = [0] + tour + [0]

# Calculation of the total travel cost and maximum distance
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)