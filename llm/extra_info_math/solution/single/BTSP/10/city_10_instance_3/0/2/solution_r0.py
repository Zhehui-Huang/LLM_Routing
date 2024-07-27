import pulp
import math

# Define the cities' coordinates
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

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Total number of cities (including depot)
n = len(coordinates)

# Calculate distances between each pair of cities
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Create a linear problem variable
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables, x_ij is 1 if the path from i to j is included in the tour
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}

# Objective function: minimize the maximum distance between consecutive cities in the tour
problem += pulp.lpSum(c[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Maximize the minimum distance"

# Constraints
# Each city must be left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"

# Each city must be entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"Enter_city_{j}"

# Subtour elimination
for k in range(3, n+1):
    for subset in itertools.combinations(range(1, n), k-1):
        subset = (0,) + tuple(subset)
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset)-1

# Solve the problem
status = problem.solve()
print("Status:", pulp.LpStatus[status])

# Extract the tour
tour = []
current_city = 0
next_city = None
total_cost = 0
max_distance = 0
visited = [False] * n
visited[0] = True
tour.append(current_city)

while True:
    next_city = next(j for j in range(n) if not visited[j] and pulp.value(x[current_city, j]) == 1)
    visited[next_city] = True
    tour.append(next_city)
    distance = c[current_city, next_city]
    total_cost += distance
    max_distance = max(max_distance, distance)
    current_city = next_city
    if len(tour) == n:
        break

tour.append(0)  # Return to depot
total_cost += c[current_city, 0]
max_distance = max(max_distance, c[current_city, 0])  # add last leg distance

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")