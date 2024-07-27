import pulp
import math
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

# City coordinates
cities = [
    (26, 60),   # City 0: Depot
    (73, 84),   # City 1
    (89, 36),   # City 2
    (15, 0),    # City 3
    (11, 10),   # City 4
    (69, 22),   # City 5
    (28, 11),   # City 6
    (70, 2),    # City 7
    (47, 50),   # City 8
    (60, 29),   # City 9
    (29, 26),   # City 10
    (85, 68),   # City 11
    (60, 1),    # City 12
    (71, 73),   # City 13
    (82, 47),   # City 14
    (19, 25),   # City 15
    (75, 9),    # City 16
    (52, 54),   # City 17
    (64, 72),   # City 18
    (14, 89)    # City 19
]

n = len(cities)

# Initialize the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 0, 1, pulp.LpBinary)
d = pulp.LpVariable("d", lowBound=0)

# Objective function
prob += d, "Maximum distance"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(cities[i], cities[j]) <= d

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current_city = 0
prev_city = 0
sequence = [1] * n
while len(tour) < n:
    tour.append(current_city)
    for j in range(n):
        # Select the next city based on the x variable being 1
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            sequence[current_city] = 0
            current_city = j
            break

# Append the depot to complete the tour
tour.append(0)

# Tour cost and maximum distance between any two cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_data
    zij
    istance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the final results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)