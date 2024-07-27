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

# Variables: x_ij = 1, if route between i and j is taken; 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: Minimize the sum of travel costs
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: Each city is arrived at and left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"

# Subtour elimination constraints
for i in range(n):
    for j in range(1, n):
        if i != j:
            model += x[i, j] + x[j, i] <= 1

# Solve the problem
model.solve()

# Extract the tour from the model
tour = []
current_city = 0
remaining_cities = list(range(1, n))
tour.append(current_city)

while remaining_cities:
    next_city = [j for j in remaining_cities if pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    current_city = next_city
    remaining_cities.remove(current_city)

tour.append(0) # Ending back at the depot

# Calculate the total travel cost
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")