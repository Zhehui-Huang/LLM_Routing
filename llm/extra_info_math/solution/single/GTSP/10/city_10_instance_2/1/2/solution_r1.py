import pulp as pl
import math

# City coordinates
coords = {
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

# Grouping information
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Set all cities and define V as a unique set collecting all city indices
V = set(coords.keys())

# Integer Programming Model
model = pl.LpProblem("TSP_Group_Selection", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')

# Objective function: Minimize the total distance
model += pl.lpSum(x[i, j] * distance(i, j) for i in V for j in V if i != j)

# Constraints ensuring each group has one city selected, and connected to tour
for group in groups.values():
    # Exactly one city from each group must have a selected outgoing edge
    model += pl.lpSum(x[i, j] for i in group for j in V if i != j) == 1
    # Exactly one city from each group must have a selected incoming edge
    model += pl.lpSum(x[j, i] for i in group for j in V if i != j) == 1

# Flow conservation constraint to ensure a legal tour
for v in V:
    model += pl.lpSum(x[v, j] for j in V if v != j) == pl.lpSum(x[j, v] for j in V if v != j)

# Solve the problem
status = model.solve()
if status == pl.LpStatusOptimal:
    print("Optimal solution found.")

    # Construct the tour from the decision variables
    tour = []
    current_city = 0
    tour.append(current_city)

    while True:
        next_city = None
        for j in V:
            if j != current_city and x[current_city, j].varValue > 0.9:
                next_city = j
                tour.append(next_city)
                current_city = next_city
                break
        if next_city == 0:
            break

    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")