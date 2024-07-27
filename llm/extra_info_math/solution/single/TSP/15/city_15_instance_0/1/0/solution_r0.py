import pulp
import math

# Define the coordinates of the cities (depot + 14 other cities)
coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
               (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
n = len(coordinates)

# Calculate the Euclidean distance between each pair of cities
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = calc_distance(coordinates[i], coordinates[j])

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij is 1 if the route goes directly from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", distance_matrix, cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i, j in distance_matrix), "Total Distance"

# Constraints
for i in range(n):
    # Each city must be left exactly once
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    
    # Each city must be entered exactly once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination
for s in range(2, n):
    subsets = itertools.combinations(range(1, n), s)  # Ignore city 0 (depot) when generating subsets
    for subset in subsets:
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Extract the tour
tour = []
current_city = 0
tour.append(current_city)
visited = set([0])
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
    if current_city in visited:
        break
    visited.add(current_city)
    tour.append(current_card_city)

tour.append(0)  # End at the depot

# Calculate the total cost of the resulting tour
total_travel_cost = pulp.value(problem.objective)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)