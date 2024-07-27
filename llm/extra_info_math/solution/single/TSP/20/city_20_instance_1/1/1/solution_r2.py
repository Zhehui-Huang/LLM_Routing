import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus
import itertools

# Coordinate of cities {city_index: (x_coord, y_coord)}
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
n = len(cities)
costs = {(i, j): euclidean travel_distance(cmap[i], cmap[j]) for i in range(n) for j in range(n) if i != j}

# Problem
model = LpProblem("TSP", LpMinimize)

# Variables: x[i, j] is 1 if route is taken, 0 otherwise
x = LpVariable.dicts('x', costs, 0, 1, LpInteger)

# Objective
model += lpSum(x[i, j] * costs[i, j] for i, j in costs)

# Constraints
# Each city has one departure
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if (i, j) in costs) == 1

# Each city has one arrival
for j in range(n):
    model += lpSum(x[i, j] for i in range(n) if (i, j) in costs) == 1

# Subtour elimination
for k in range(3, n + 1):
    for subset in itertools.combinations(range(1, n), k - 1):  # 1-based index
        subset = list(subset)
        subset.append(0)  # Include the depot city
        model += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Check if a valid solution exists
if model.status == 1:
    # Extract tour
    routes = [(i, j) for i in range(n) for j in range(n) if x[i, j].value() == 1]
    tour = []
    next_city = 0
    while True:
        tour.append(next_city)
        next_citys = [j for i, j in routes if i == next_city]
        if not next_citys:
            break
        next_city = next_citys[0]
    tour.append(tour[0])  # Return to starting city

    # Total Cost
    total_cost = sum(costs[i, j] for i, j in zip(tour[:-1], tour[1:]))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No feasible solution found.")