import math
import pulp

# Coordinates for the cities including the depot city
coordinates = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Groups of cities
groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Function to calculate Euclidean distance
def euclidean_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

n = len(coordinates)  # Total number of cities including the depot

# Initialize the problem
prob = pulp.LpProblem("Minimize_route_cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat="Binary")

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraint to ensure exactly one city from each group is visited
for group in groups:
    prob += pulp.lpSum(x[(0, j)] for j in group) == 1
    prob += pulp.lpSum(x[(j, 0)] for j in group) == 1

# Constraints to ensure each city in groups sends and receives only one path
for k in range(3):  # Three groups
    for i in groups[k]:
        prob += pulp.lpSum(x[(i, j)] for j in range(n) if j not in groups[k] and j != i) == 1
        prob += pulp.lpSum(x[(j, i)] for j in range(n) if j not in groups[k] and j != i) == 1

# Solve the problem
prob.solve()

# Collect the results if the problem is solved to optimality
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = [0]
    used_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[(i, j)]) == 1]
    current_loc = 0
    for _ in range(4):  # Number of edges in the tour will be 4
        next_loc = next(j for (i, j) in used_edges if i == current_loc)
        tour.append(next_loc)
        current_loc = next_loc

    # Calculate the travel cost
    total_travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("No optimal solution found.")