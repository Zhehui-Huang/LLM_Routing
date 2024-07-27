import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of cities (including the depot as the first entry)
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

n = len(cities)

# Create the optimization model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Create decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d_max = pulp.LpVariable("d_max")

# Objective function
model += d_max

# Distance matrix
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean_distance(cities[i], cities[j])

# Single-entry and exit constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Minimax constraint 
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i, j] * x[i, j] <= d_max

# Subtour elimination constraints
for s in range(3, n + 1):
    for subset in itertools.combinations(range(1, n), s - 1):  # All subsets S of n-1 elements excluding depot
        subset_with_depot = tuple([0] + list(subset))
        model += pulp.lpSum(x[i, j] for i in subset_with_depot for j in subset_with_depot if i != j) <= len(subset_with_depot) - 1

# Solve the model
model.solve()

# Extract the tour
tour = []
current = 0
for _ in range(n):
    tour.append(current)
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1][0]
    current = next_city
tour.append(0)  # return to depot

# Calculate the total cost and the maximum distance
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(n))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(n))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")