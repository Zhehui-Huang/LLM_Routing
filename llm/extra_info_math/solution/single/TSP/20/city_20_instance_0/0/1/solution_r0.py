import pulp
from math import sqrt

# Define the city coordinates
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities including the depot
n = len(city_coords)

# Function to calculate Euclidean distance between two cities
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Construct the cost matrix
cost_matrix = [[distance(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Create problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(x[(i, j)] * cost_feature['weight'] * cost_matrix[i][j] for i in range(n) for j in range(n) if i != j)

# Subject to
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination constraints placeholder (to be filled with actual constraints or use of callbacks)

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Add the return to depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(distance(city_coords[tour[i]], city_coords[tour[i + 1]]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)