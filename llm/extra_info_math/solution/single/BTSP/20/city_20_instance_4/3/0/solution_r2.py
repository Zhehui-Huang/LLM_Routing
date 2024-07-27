import pulp
import math
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

# City coordinates
cities = [
    (26, 60),  # Depot
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)  # Last city
]

n = len(cities)

# Define the decision variables and problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = pulp.LpVariable("d", lowBound=0)

# Objective function
prob += d, "Maximum distance of the tour"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Exit_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(cities[i], cities[j]) <= d, f"MaxDist_{i}_{j}"

# Sub-tour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1, f"Subtour_{S}_{subset}"

# Solve the problem
prob.solve()

# Extract the results
tour = []
max_distance = 0
current_city = 0
next_city = None

for _ in range(n):
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if euclidean_distance(cities[current_city], cities[next_city]) > max_distance:
        max_distance = euclidean_distance(cities[current_city], cities[next_city])
    current_city = next_city

tour.append(tour[0])  # return to the depot

# Calculate total distance cost
total_cost = 0
for i in range(len(tour) - 1):
    total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

# Print the tour, total cost, and maximum distance
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))