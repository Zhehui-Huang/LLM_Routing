import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Number of cities
n = len(cities)

# Compute the distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1, if the route between i and j is taken; 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Arrival and leaving constraints for each city
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve()

# Extract tour
tour = []
current_city = 0
tour.append(current_city)
visited = set([0])

# Construct the tour iteratively
while len(visited) < n:
    for i in range(n):
        if (current_city, i) in x and pulp.value(x[current_city, i]) == 1 and i not in visited:
            tour.append(i)
            visited.add(i)
            current_city = i
            break

# Adding the depot city to complete the tour
tour.append(0)

# Calculate the travel cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")