import math
import pulp as pl

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Problem instance
prob = pl.LpProblem("Minimax_TSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n) if i != j], cat='Binary')
d = pl.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective
prob += d

# Constraints
for i in range(n):
    prob += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"One_outgoing_{i}"
    prob += pl.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"One_incoming_{i}"

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distances[i][j] <= d, f"Dist_constraint_{i}_{j}"

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(n), s):
        prob += pl.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extracting the tour from the variables
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if j not in visited and pl.value(x[current, j]) == 1:
            tour.append((current, j))
            visited.append(j)
            current = j
            break
tour.append((current, 0))  # Return to depot

# Calculating final outputs
tour_indices = [i[0] for i in tour] + [0]
max_dist = max(distances[i][j] for i, j in tour)
total_cost = sum(distances[i][j] for i, j in tour)

print(f"Tour: {tour_indices}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")