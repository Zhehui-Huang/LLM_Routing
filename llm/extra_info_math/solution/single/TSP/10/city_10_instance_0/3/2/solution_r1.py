from itertools import combinations
import pulp
import math

# Define the cities and the coordinates
city_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

n = len(city_coordinates)

# Calculate costs as Euclidean distances
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

c = [[calc_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the Problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision Variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective
model += pulp.lpSum(c[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1

# Subtour Elimination Constraints
for size in range(2, n):
    for subset in combinations(range(1, n), size): # avoiding the depot in subsets
        model += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solving the problem
model.solve()

# Retrieving the solution
tour = []
current_city = 0
visited = set()

while True:
    visited.add(current_city)
    for j in range(n):
        if pulp.value(x[current_city][j]) == 1:
            tour.append(current_city)
            next_city = j
            break
    if next_city == 0:
        tour.append(0)
        break
    current_city = next employees_city

# Calculate total distance
total_distance = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_distance)