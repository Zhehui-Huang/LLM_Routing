import pulp
import math

# Define the cities' coordinates
city_coordinates = [
    (53, 68),  # Depot city 0: index 0
    (75, 11),  # City 1: index 1
    (91, 95),  # City 2: index 2
    (22, 80),  # City 3: index 3
    (18, 63),  # City 4: index 4
    (54, 91),  # City 5: index 5
    (70, 14),  # City 6: index 6
    (97, 44),  # City 7: index 7
    (17, 69),  # City 8: index 8
    (95, 89)   # City 9: index 9
]

# Define city groups
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Calculate Euclidean distances between each pair of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a dictionary to hold the distances
distances = {}
for i in range(len(city_coordinates)):
    for j in range(len(city_coordinates)):
        if i != j:
            distances[(i, j)] = calculate_distance(city_coordinates[i], city_coordinates[j])

# Setup the problem
problem = pulp.LpProblem("RobotRoutingProblem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(10) for j in range(10) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, 10)), lowBound=0)

# Objective
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in range(10) for j in range(10) if i != j and (i, j) in distances]), "Minimize total travel cost"

# Ensure each group has exactly one outgoing link to other cities
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(10) if j not in group) == 1

# Ensure each group has exactly one incoming link from other cities
for group in city_groups:
    problem += pulp.lpSum(x[j, i] for i in group for j in range(10) if j not in group) == 1

# Flow conservation constraints
for k in range(10):
    problem += pulp.lpSum(x[k, j] for j in range(10) if (k, j) in x) == pulp.lpSum(x[i, k] for i in range(10) if (i, k) in x)

# Elimination of subtours
for i in range(1, 10):
    for j in range(1, 10):
        if i != j and (i, j) in x:
            problem += u[i] - u[j] + len(city_coordinates) * x[i, j] <= len(city_coordinates) - 1

# Solve the problem
status = problem.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Retrieving the results if the problem was solved
if status == pulp.LpStatusOptimal:
    total_cost = 0
    tour = [0]
    while True:
        next_cities = [j for j in range(10) if pulp.value(x[tour[-1], j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_tour)
        total_cost += distances[(tour[-2], tour[-1])]
    tour.append(0)  # Wrap tour to the depot city

    # Complete the final leg cost
    total_cost += distances[(tour[-2], tour[-1])]

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("The problem did not have an optimal solution under the current parameters.")