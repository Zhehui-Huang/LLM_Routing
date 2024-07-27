import pulp
import math

# Helper function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Coordinates of cities including the depot
coordinates = [
    (8, 11),   # Depot City 0
    (40, 6),   (95, 33),   (80, 60),   (25, 18),   (67, 23),  # Cities 1-5
    (97, 32),  (25, 71),   (61, 16),   (27, 91),   (91, 46),  # Cities 6-10
    (40, 87),  (20, 97),   (61, 25),   (5, 59),    (62, 88),  # Cities 11-15
    (13, 43),  (61, 28),   (60, 63),   (93, 15)               # Cities 16-19
]

# Define city groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Initiate the problem
problem = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Variable x_ij where i, j are city indices, binary decision (0 or 1)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')

# Objective Function: Minimize Total Distance
problem += pulp.lpSum(x[i, j] * calculate_distance(coordinates[i], coordinates[j]) for i in range(20) for j in range(20) if i != j), "Total Travel Distance"

# Constraint: From the depot to one city in each group and back
for group in city_groups:
    problem += pulp.lpSum(x[0, j] for j in group) == 1
    problem += pulp.lpSum(x[j, 0] for j in group) == 1

# Constraint: Visit exactly one city from each group
for k, group in enumerate(city_groups):
    for i in range(20):
        if i in group or i == 0:
            continue
        problem += pulp.lpSum(x[i, j] for j in group if j != i) == 1
        problem += pulp.lpSum(x[j, i] for j in group if j != i) == 1

# Solve the problem
problem.solve()

# Ensure the problem solved correctly
if problem.status:
    # Calculate and collect the results
    total_travel_cost = 0
    tour = [0]
    visited = set([0])
    current = 0
    
    while len(tour) < 4:
        for j in range(20):
            if x[current, j].varValue > 0.5 and j not in visited:
                tour.append(j)
                total_travel_cost += calculate_distance(coordinates[current], coordinates[j])
                visited.add(j)
                current = j
                break
    tour.append(0) # Return to depot
    total_travel_cost += calculate_distance(coordinates[current], coordinates[0])

    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("No feasible solution found.")