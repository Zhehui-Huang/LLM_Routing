import pulp as pl
import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Creating a function for Euclidean distance
def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute cost between each pair of nodes not in the same city
cost = {(i, j): euclidean(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the model
model = pl.LpProblem("TSP", pl.LpMinimize)

# Decision variables: x[i, j] = 1 if travel from i to j
x = pl.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: Minimize total travel cost
model += pl.lpSum(cost[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in x)

# Each group must connect exactly once to any other city
for group_id, group in groups.items():
    selected_cities = [0] + group  # Include depot as a possible return point
    # Exactly one outgoing edge from group
    model += pl.lpSum(x[i, j] for i in selected_cities for j in cities if i != j and (i, j) in x) == 1
    # Exactly one incoming edge to group
    model += pl.lpSum(x[j, i] for i in selected_cities for j in cities if i != j and (j, i) in x) == 1

# Fixing the depot connections
model += pl.lpSum(x[0, j] for j in cities if j != 0 and (0, j) in x) == len(groups)  # Outgoing
model += pl.lpSum(x[j, 0] for j in cities if j != 0 and (j, 0) in x) == len(groups)  # Incoming

# Solve the model
model.solve()

# Extract the tour from the variables
tour = []
if pl.LpStatus[model.status] == 'Optimal':
    current_city = 0
    start_city = 0
    steps = [0] * len(groups)

    for _ in range(len(groups)):
        next_city = next(j for j in cities if j != current_city and pl.value(x[current_city, j]) == 1)
        steps[current_city] = next_city
        current_city = next_city

    # Close the tour by returning to the starting city
    tour = [start_city]
    while True:
        next_city = steps[tour[-1]]
        if next_city == start_city:
            break
        tour.append(next_city)

    # Append depot to close the circuit
    tour.append(start = 0)

# Calculate the total travel cost
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)