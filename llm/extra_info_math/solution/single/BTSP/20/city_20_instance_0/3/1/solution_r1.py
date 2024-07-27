import pulp
import math
import itertools

# Coordinates of cities (including the depot as the first entry)
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

n = len(cities)

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the optimization model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Distance matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d_max = pulp.LpVariable("d_max", lowBound=0)

# Objective function
model += d_max

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distances[i, j] <= d_max

# Subtour elimination constraints (using the SEC method)
for S in range(3, n + 1):
    for subset in itertools.combinations(range(1, n), S - 1):
        subset_with_depot = tuple([0] + list(subset))
        model += pulp.lpSum(x[i, j] for i in subset_with_depot for j in subset_with_depot if i != j) <= len(subset_with_depot) - 1

# Solve the model
model.solve()

# Extract the tour
tour = []
current_city = 0
remaining_cities = set(range(n))
while remaining_cummies:
    tour.append(current_city)
    remaining_cities.remove(current_city)
    next_cities = [j for j in remaining_cities if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

tour.append(0)  # returning to the depot

# Calculate the total travel cost and the maximum distance between any two consecutive cities
total_travel_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_consecutive_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")