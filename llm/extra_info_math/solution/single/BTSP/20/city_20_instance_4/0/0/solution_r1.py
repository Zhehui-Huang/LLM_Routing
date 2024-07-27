import math
import pulp
import itertools

# Coordinates of each city including depot (indexed from 0 to 19)
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities, including the depot
n = len(coords)

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Problem declaration
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij where i, j are cities; j != i
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Variable to minimize the maximum distance between consecutive cities
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += max_distance

# Constraints ensuring each city is entered and left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Constrain max_distance to be at least the distance between each pair of cities in the path
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max_distance

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = prob.solve()
if status == pulp.LpStatusOptimal:
    tour = [0]
    while len(tour) < n:
        i = tour[-1]
        for j in range(n):
            if i != j and x[i, j].varValue > 0.99:
                tour.append(j)
                break
    tour.append(0)  # complete the tour by returning to the depot

    # Calculate total cost and max distance for the found tour
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_dist_btw_cities = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist_btw_cities}")
else:
    print("Failed to solve the problem.")