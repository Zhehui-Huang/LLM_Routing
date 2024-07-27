import pulp
import math

# Define the city coordinates
city_coords = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define city groups (including depot)
groups = {
    1: [1, 2, 5, 6],
    2: [8, 9, 10, 13],
    3: [3, 4, 7],
    4: [11, 12, 14]
}

# Calculate distances between cities using Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {(i, j): calculate_cleanance(city_coords[i], city_coords[j])
             for i in city_coords
             for j in city_coords if i != j}

# Create the problem
problem = pulp.LpProblem("TSP_variant", pulp.LpMinimize)

# Create variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)
     for i in city_coords
     for j in city_coords if i != j}

# Objective function
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in city_coords for j in city_coords if i != j)

# Constraints
for k in groups:
    cluster = groups[k]
    problem += pulp.lpSum(x[i, j] for i in cluster for j in city_coords if j not in cluster) == 1
    problem += pulp.lpSum(x[j, i] for i in cluster for j in city_coords if j not in cluster) == 1

# Adding flow conservation constraints
for j in city_coords:
    problem += pulp.lpSum(x[i, j] for i in city_coords if i != j) == pulp.lpSum(x[j, k] for k in city_coords if k != j)

# Solve the problem
problem.solve()

# Extract the tour from the decision variables
tour = [0]
current_city = 0
for _ in range(len(city_coords)):
    next_cities = [j for j in city_coords if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Include return to the depot
tour.append(0)

# Calculate the total cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))