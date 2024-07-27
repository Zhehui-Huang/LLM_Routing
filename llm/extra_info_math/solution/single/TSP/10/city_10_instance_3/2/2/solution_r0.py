import pulp
from math import sqrt

# Coordinates of cities (depot + cities 1 to 9)
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Number of cities (including the depot)
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Creating the cost matrix
cost_matrix = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

# PuLP model setup
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function - Minimize the total cost of the tour
model += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints ensuring each city is entered and left exactly once
for i in range(n):
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"

# Subtour elimination constraints (naive implementation - can be improved for larger problems)
for i in range(2, n):
    for subset in itertools.combinations(range(1, n), i):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve()

# Extract the tour from the variables
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total travel cost
total_travel_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")