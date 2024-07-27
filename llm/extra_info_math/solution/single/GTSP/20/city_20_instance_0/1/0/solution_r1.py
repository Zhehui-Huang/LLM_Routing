import math
import pulp

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates, including the depot
coordinates = [
    (8, 11),   # Depot
    (40, 6),   (95, 33),   (80, 60),   (25, 18),   (67, 23),
    (97, 32),  (25, 71),   (61, 16),   (27, 91),   (91, 46),
    (40, 87),  (20, 97),   (61, 25),   (5, 59),    (62, 88),
    (13, 43),  (61, 28),   (60, 63),   (93, 15)
]

# Groups of cities
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate distances
n = len(coordinates)
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Adding auxiliary depot city to groups for modeling convenience
groups = [ [0] + group for group in city_groups ] + [[0]]

# Setup the MILP
prob = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Variables: x[i, j] is a binary variable indicating whether the path from i to j is used
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j and (i, j) in distances])

# Constraints
for group in city_groups:
    prob += sum(x[i, j] for i in group for j in range(n) if (i, j) in x) == 1
    prob += sum(x[j, i] for i in group for j in range(n) if (j, i) in x) == 1
    
# Sub-tour prevention constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j and (i, j) in x:
            prob += u[i] - u[j] <= n - 1 - n * (1 - x[i, j])

# Start and end at the depot
prob += sum(x[0, j] for j in range(n) if (0, j) in x) == 3
prob += sum(x[i, 0] for i in range(n) if (i, 0) in x) == 3

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
for v in prob.variables():
    if v.varValue != 0 and v.name.startswith('x'):
        i, j = map(int, v.name[2:-1].split(","))
        if x[i, j].value() == 1:
            tour.append(j)

# Fix tour order to start from 0 and come back to 0
final_tour = [0]
visited = set([0])
current_city = 0
while len(visited) < len(tour):
    for i in range(1, len(tour)):
        if tour[i] not in visited and x[current_city, tour[i]].value() == 1:
            current_city = tour[i]
            final_tour.append(current_city)
            visited.add(current_city)
            break
final_tour.append(0)

# Calculate the cost
total_cost = sum(distances[final_tour[i], final_tour[i+1]] for i in range(len(final_tour)-1))

# Results
print("Tour:", final_tour)
print("Total travel cost:", total_cost)