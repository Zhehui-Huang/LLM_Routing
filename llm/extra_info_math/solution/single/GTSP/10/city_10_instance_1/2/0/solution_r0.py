import pulp
import math

# Define the cities' coordinates
city_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
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
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in range(10) for j in range(10) if i != j]), "Minimize total travel cost"

# Constraints
# Each group must connect exactly once
for group in city_groups:
    problem += pulp.lpSum([x[i, j] for i in group for j in range(10) if j not in group]) == 1, f"One outgoing from group {group}"
    problem += pulp.lpSum([x[j, i] for i in group for j in range(10) if j not in [group]]) == 1, f"One incoming to group {group}"

# Flow conservation constraint to maintain the tour
for k in range(1, 10):
    problem += pulp.lpSum([x[i, k] for i in range(10) if i != k]) - pulp.lpSum(
        [x[k, j] for j in range(10) if j != k]) == 0, f"Flow conservation at city {k}"

# Subtour elimination constraints:
k = len(city_groups) + 1  # as there are 4 groups plus one for the depot
for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            problem += u[i] - u[j] + k * x[i, j] + (k - 2) * x[j, i] <= k - 1

# Solve the problem
status = problem.solve()
print("Status:", pulp.LpStatus[status])

# Extract solution
tour = [0]
for k in range(10):
    next_city = [j for j in range(10) if pulp.value(x[tour[-1], j]) == 1]
    if not next_city:
        break
    tour.append(next_city[0])

tour.append(0)  # return to the depot

# Calculate total travel cost
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)