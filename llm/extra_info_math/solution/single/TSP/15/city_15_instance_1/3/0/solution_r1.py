import math
import pulp

# Define the coordinates of each city including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Compute the Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", distances.keys(), cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum(distances[(i, j)] * x[(i, j)] for (i, j) in distances)

# Constraints
# Incoming flow to each city
for j in cities:
    prob += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1

# Outgoing flow from each city
for i in cities:
    prob += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1

# Adding subtour elimination
u = pulp.LpVariable.dicts('u', cities, lowBound=0, upBound=len(cities)-1, cat=pulp.LpInteger)
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):
            prob += u[i] - u[j] + len(cities)*x[(i, j)] <= len(cities)-1

# Solve the problem using the default solver
prob.solve()

# Output the solution
tour = []
current_city = 0
visited = {0}
while True:
    next_cities = {j for j in cities if pulp.value(x[(current_city, j)]) == 1}
    next_city = next_cities.pop()
    if next_city in visited:
        break
    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city

# Include the depot city at the end to complete the tour
tour = [0] + tour + [0]

# Calculate the total cost of the tour
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel uost: {total_cost}")