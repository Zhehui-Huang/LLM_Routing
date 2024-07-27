import pulp
import math

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Groups
groups = {
    1: [1, 2, 6],
    2: [3, 7, 8],
    3: [4, 5, 9]
}

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Decision variables: x[i, j] -- travel from i to j
x = pulp.LpVariable.dicts("travel",
                          ((i, j) for i in coordinates for j in coordinates if i != j),
                          cat='Binary')

# Objective Function: Minimize total distance traveled
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in coordinates for j in coordinates if i != j), "Total_Cost"

# Each group should have exactly one outgoing and one incoming edge to/from selected nodes
for g, cities in groups.items():
    prob += pulp.lpSum(x[i, j] for i in cities for j in coordinates if j not in cities) == 1, f"One_outgoing_from_group_{g}"
    prob += pulp.lpSum(x[j, i] for i in cities for j in coordinates if j not in cities) == 1, f"One_incoming_to_group_{g}"

# Conservation of flow in each city
for city in coordinates:
    if city == 0:
        # Depot may have two edges (start/end)
        prob += pulp.lpSum(x[0, j] for j in coordinates if j != 0) == 2, f"Flow_start_end_depot"
        prob += pulp.lpSum(x[i, 0] for i in coordinates if i != 0) == 2, f"Flow_back_to_depot"
    else:
        prob += pulp.lpSum(x[i, city] for i in coordinates if i != city) == \
                pulp.lpSum(x[city, j] for j in coordinates if j != city), f"Flow_conservation_{city}"

# Solve the problem
prob.solve()

# Extract the tour from the variable values
edges = [(i, j) for i in coordinates for j in coordinates if i != j and pulp.value(x[i, j]) == 1]
tour = [0]  # Start at the depot
current = 0
cost = 0

while len(edges) > 0:
    for i, j in edges:
        if i == current:
            tour.append(j)
            cost += distance(i, j)
            current = j
            edges.remove((i, j))
            break

# Include the return to the depot
cost += distance(tour[-1], 0)
tour.append(0)  # End at the depot

print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")