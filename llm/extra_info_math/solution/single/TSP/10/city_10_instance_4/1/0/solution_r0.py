import pulp
import math

# City coordinates (including the depot as city 0)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62),
}

# Calculate the Euclidean distance between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {
    (i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the route goes from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: Minimize the total distance traveled
prob += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j]), "Total_Distance"

# Each city is entered exactly once
for j in cities:
    prob += pulp.lpSum([x[(i, j)] for i in cities if i != j]) == 1, f"Enter_{j}"

# Each city is left exactly once
for i in cities:
    prob += pulp.lpSum([x[(i, j)] for j in cities if i != j]) == 1, f"Leave_{i}"

# Subtour Elimination Constraints
for n in range(2, len(cities)):
    for S in itertools.combinations(cities.keys(), n):
        prob += pulp.lpSum([x[(i, j)] for i in S for j in S if i != j]) <= len(S) - 1

# Solve the problem
prob.solve()

# Retrieve the solution
tour = []
visited = [0]
current = 0
total_cost = 0

while True:
    next_city = [j for j in cities if j != current and pulp.value(x[(current, j)]) == 1][0]
    tour.append(next_city)
    total_cost += distances[(current, next_city)]
    current = next_city
    if current == 0:
        break

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)