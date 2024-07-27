import pulp
import math

# Define the cities, including the depot city at index 0
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Number of cities including the depot
n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Calculate costs for all city pairs
costs = {}
for i in range(n):
    for j in range(n):
        if i != j:
            costs[i, j] = euclidean_distance(cities[i], cities[j])

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum([costs[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints: Each city is arrived at from exactly one other city
for j in range(n):
    model += pulp.lpSum([x[i, j] for i in range(n) if i != j]) == 1

# Constraints: Each city is left to exactly one other city
for i in range(n):
    model += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1

# Subtour elimination
for sub_tour_size in range(2, n):
    for sub_tour in itertools.combinations(range(n), sub_tour_size):
        model += pulp.lpSum([x[i, j] for i in sub_tour for j in sub_tour if i != j]) <= len(sub_tour) - 1

# Solve the problem
model.solve()

# Extract the tour
tour = []
curr_city = 0
while True:
    next_city = [j for j in range(n) if j != curr_city and pulp.value(x[curr_city, j]) == 1][0]
    tour.append(curr_city)
    if next_city == 0:
        break
    else:
        curr_city = next_city
tour.append(0)  # Return to depot

# Calculate the total cost of the tour
total_cost = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")