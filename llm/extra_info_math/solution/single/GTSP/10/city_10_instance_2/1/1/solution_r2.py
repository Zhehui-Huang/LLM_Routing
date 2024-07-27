import pulp
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Grouping of cities where exactly one city must be visited
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2],
}

# Euclidean distance
def calculate_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize model
model = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Variables: x[(i,j)] = 1 if travel from i to j
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
model += pulp.lpSum(x[(i, j)] * calculate_distance(i, j) for i in cities for j in cities if i != j)

# Constraints for ensuring exactly one city per group and proper route formation
for group in groups.values():
    # Select exactly one node from each group
    model += pulp.lpSum(x[k, j] for k in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, k] for k in group for j in cities if j not in group) == 1

# Flow conservation to maintain connectivity from and to the depot
for c in cities:
    if c != 0:  # Depot constraints are handled by group constraints
        model += pulp.lpSum(x[i, c] for i in cities if i != c) == \
                 pulp.lpSum(x[c, j] for j in cities if j != c)

# Solve
model.solve()

# Extract the tour route and calculate the distance
tour = [0]  # Start from the depot
current_city = 0
while True:
    next_city = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_csv:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate total traveling cost
travel_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", travel_cost)