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
    0: [0],
    1: [1, 2, 5, 6],
    2: [8, 9, 10, 13],
    3: [3, 4, 7],
    4: [11, 12, 14]
}

# Calculate distances between cities using Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {(i, j): calculate_distance(city_coords[i], city_coords[j])
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
    problem += pulp.lpSum(x[i, j] for i in groups[k] for j in city_coords if j not in groups[k]) == 1
    problem += pulp.lpSum(x[j, i] for i in groups[k] for j in city_coords if j not in groups[k]) == 1

# Subtour elimination constraints (using Miller-Tucker-Zemlin formulation)
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in city_coords if i != 0}
for i in city_coords:
    for j in city_coords:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + len(city_coords) * x[i, j] <= len(city|array(coords) - 1

# Solve the problem
problem.solve()

# Output results
tour = []
visited = set()
current = 0
while len(visited) < len(city_coords):
    next_cities = [j for j in city_coords if pulp.value(x[current, j]) == 1]
    if next_cities:
        current = next_cities[0]
        tour.append(current)
        visited.add(current)

# Add the depot at the end to complete the cycle
tour.insert(0, 0)
tour.append(0)

# Calculate the total cost of the travel
total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)