import math
import pulp

# Define the cities and their coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

n = len(coordinates)

# Compute Euclidean distances between each pair of points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the path between i to j is chosen in the tour, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# The maximum distance in the path (objective variable)
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance used in the tour
model += z, "MinimizeMaxDistance"

# Each city is arrived at from exactly one other city
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Each city is departed to exactly one other city
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Maximum link constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i, j] * x[i, j] <= z

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation with additional variables
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i, j] <= n-1

# Solve the problem
model.solve()

# Results
tour = []
total_cost = 0
max_distance = 0
current_city = 0
tour.append(current_city)

# Tracing the tour from city 0
while True:
    for j in range(n):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            next_city = j
            tour.append(next_city)
            total_cost += distances[current_city, next_city]
            max_distance = max(max_longest_path, distances[current_city, next_city])
            current_city = next_city
            break
    if next_city == 0:
        break

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)