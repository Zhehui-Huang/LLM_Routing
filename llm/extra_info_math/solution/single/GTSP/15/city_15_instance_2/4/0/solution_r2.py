import pulp
import math

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# LP Model
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for i in cities for j in cities if i != j}

# Objective
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "Total_Distance"

# Constraints
# Each group should connect to/from non-group cities exactly once
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

# Flow conservation constraint
for node in cities:
    model += pulp.lpSum(x[(i, node)] for i in cities if i != node) == \
             pulp.lpSum(x[(node, j)] for j in cities if j != node), f"Flow_conserv_{node}"

# Solve the problem
model.solve(pulp.PULP_CBC_CMD())

# Extract the resultant tour
tour = [0]
used_edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) == 1]
current = 0

while len(used_edges) > 0:
    for i, j in used_edges:
        if i == current:
            tour.append(j)
            current = j
            used_edges.remove((i, j))
            break
    if current == 0:
        break

# Compute the tour cost
tour_cost = sum([distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])

# Output
print("Tour:", tour)
print("Total travel cost:", tour_cost)