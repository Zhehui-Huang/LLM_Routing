from itertools import combinations
import pulp
import math

# City coordinates including the depot city
city_coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

n = len(city_coordinates)

# Distance function based on Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distance_matrix = [[calculate_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] is 1 if we travel from i to j; otherwise 0
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective function: minimize the sum of distances for included edges
model += pulp.lpSum(distance_matrix[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if j != i) == 1
    model += pulp.lpSum(x[j][i] for j in range(n) if j != i) == 1

# Subtour constraints
for k in range(2, n):
    for subtour in combinations(range(1, n), k):
        model += pulp.lpSum(x[i][j] for i in subtourcehold_city for j in subtour if i != j) <= len(subtour) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Recover the tour by following successors
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current_city][j]) == 1]
    if next_cities:
        current_city = next_cities[0]
        if current_city == 0:
            break
    else:
        break

# Calculate the tour distance
tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", tour_cost)