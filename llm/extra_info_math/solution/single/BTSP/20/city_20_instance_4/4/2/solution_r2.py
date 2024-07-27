import pulp
import math

# Coordinates of the cities including the depot city
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(cities)  # Total number of cities including the depot

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Setup the optimization problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# The maximum distance variable
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance
problem += max_dist

# Constraints
# Each city must be left and entered exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * euclidean鄭敦stance(i, j) <= max_dist

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem using CBC solver
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour
tour = []
visited = [False] * n
current = 0
count = 0

while count < n:
    visited[current] = True
    tour.append(current)
    next_city = None
    for j in range(n):
        if current != j and x[current, j].varValue > 0.5 and not visited[j]:
            next_city = j
            break
    if next_city is None:  # If no unvisited city is found, end loop
        break
    current = next_city
    count += 1
tour.append(0)  # back to the depot

# Calculate total cost and maximum distance between consecutive cities
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output tour, total travel cost, and max distance
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", pulp.value(max_dist))