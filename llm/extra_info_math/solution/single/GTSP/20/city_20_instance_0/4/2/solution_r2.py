import pulp
import math

# Locations of all the cities including the depot
locations = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63),
    (93, 15)
]

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Create an LP problem instance
prob = pulp.LpProblem("Shortest_Tour", pulp.LpMinimize)

# Variables: x[i][j] is 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')

# Euclidean distance calculation
def distance(i, j):
    return math.sqrt((locations[i][0] - locations[j][0])**2 + (locations[i][1] - locations[j][1])**2)

# Objective: Minimize the total travel distance
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in range(20) for j in range(20) if i != j)

# Constraint: Enter and leave each group exactly once
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(20) if j not in group and i != j) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(20) if j not in group and i != j) == 1

# Flow conservation at each city, except city 0
for i in range(1, 20):
    prob += (pulp.lpSum(x[i, j] for j in range(20) if i != j) ==
             pulp.lpSum(x[j, i] for j in range(20) if i != j)), f"Flow_conservation_{i}"

# Solver configuration
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour from variables
path = []
current_city = 0
path.append(current_city)
for _ in range(len(groups)):
    next_cities = [j for j in range(20) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    path.append(next_city)
    current_city = next_city
path.append(0)  # Return to the starting city to complete the tour

# Calculate the tour cost
tour_cost = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

# Output
print("Tour:", path)
print("Total travel cost:", round(tour_cost, 2))