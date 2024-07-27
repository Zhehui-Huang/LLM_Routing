from pulp import *
import math

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Group information
groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create the linear programming model to minimize distances
model = LpProblem("TSP", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", [(i, j) for i in cities.keys() for j in cities.keys() if i != j], cat='Binary')

# Subset for easier manipulation
u = LpVariable.dicts("u", [i for i in groups.keys()], lowBound=0)

# Objective function
model += lpSum([x[(i, j)] * distance(i, j) for i in cities.keys() for j in cities.keys() if i != j])

# Constraints
# Guarantee only one departure from each group excluding the depot
for index, group in groups.items():
    model += lpSum([x[(i, j)] for i in group for j in cities if j not in group]) == 1

# Guarantee only one arrival to each group excluding the depot
for index, group in groups.items():
    model += lpSum([x[(j, i)] for i in group for j in cities if j not in group]) == 1

# Flow conservation at each node
for k in cities:
    model += lpSum([x[(i, k)] for i in cities if i != k]) == lpSum([x[(k, j)] for j in cities if j != k])

# Subtour elimination
n = len(groups)
for p in groups:
    for q in groups:
        if p != q:
            for i in groups[p]:
                for j in groups[q]:
                    model += u[p] - u[q] + n * x[(i, j)] <= n - 1

# Solve the model
model.solve()

# Gather the solutions
route = []
for i in cities.keys():
    for j in cities.keys():
        if i != j and x[(i, j)].varValue == 1:
            route.append((i, j))

# Extract the route in proper order
sorted_route = [0]
while len(sorted_route) < len(route):
    last = sorted_route[-1]
    for (s, d) in route:
        if s == last:
            sorted_route.append(d)
            break

sorted_route.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance(sorted_route[i], sorted_route[i+1]) for i in range(len(sortedroute) - 1))

print(f"Tour: {sorted_route}")
print(f"Total travel cost: {total_cost:.2f}")