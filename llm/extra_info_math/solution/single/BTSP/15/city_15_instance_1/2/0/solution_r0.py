import pulp
import math

# Given city coordinates
coords = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

n = len(coords)  # Number of cities including the depot

# Calculate distances between cities using Euclidean formula
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] is 1 if the robot moves from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)

# Objective: Minimize the maximum distance traveled between consecutive cities
max_dist = pulp.LpVariable("max_dist")
model += max_dist

for i in range(n):
    for j in range(n):
        if i != j:
            model += max_dist >= distances[i][j] * x[i][j]

# Constraints
# Enter and leave each city exactly once
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
for j in range(n):
    model += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for S in range(2, n):
    subsets = itertools.combinations(range(1, n), S)
    for subset in subsets:
        model += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
current_city = 0
tour.append(current_city)
visited = set([current_city])

while True:
    next_cities = [j for j in range(n) if x[current_city][j].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city

# Return to the depot
tour.append(0)

# Total Travel Cost and Maximum Distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")