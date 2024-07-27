import pulp
import itertools
from math import sqrt

# Define the coordinates of 10 cities
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

n = len(coordinates)  # Number of cities

# Euclidean distance function
def euclidean_dist(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Preparing distance dictionary
distances = {(i, j): euclidean_dist(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Initialize problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Problem variables
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}
d = pulp.LpVariable("d", lowBound=0)

# Objective function to minimize the maximum distance d
problem += d

# Constraints
# Only one outgoing edge from each node
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Only one incoming edge to each node
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Distance constraints relating the decision variables
for i, j in distances:
    problem += x[i, j] * distances[i, j] <= d

# Solve the problem
problem.solve()

# Find the tour from the solution
tour = [0]
current = 0
for _ in range(n-1):
    next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
    tour.append(next_city)
    current = next_city
tour.append(0) # Return to the starting point

# Calculate the maximum distance and total cost
max_dist = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")