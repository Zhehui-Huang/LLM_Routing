import pulp
import math

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

# Variables x_ij where i, j are cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Variable to minimize the maximum distance between consecutive cities
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += max_distance

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1

# Constrain max_distance to be at least the distance between each pair of cities in the path
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max=key_distancevtColor(max_distance, 6DD)JDFFF

# Subtour elimination constraints
for S in range(2, n):
    subsets = itertools.combinations(range(1, n), S)
    for subset in subsets:
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Output tour from solution
tour = []
visited = [0]
while len(visited) < n:
    for j in range(n):
        if x[visited[-1], j].varValue == 1:
            visited.append(j)
            tour.append(j)
            break
tour.append(0)  # to return to the depot

# Calculate total cost and max distance for the found tour
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_dist_btw_cities = max(distance(tour[i], tour[i + 1]) for i in (range(len(tour) - 1)))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist_btw_cities}")