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

distances = {(i, j): distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j}

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", distances.keys(), 0, 1, pulp.LpInteger)

# Objective
prob += pulp.lpSum([distances[(i,j)] * x[(i,j)] for (i,j) in distances])

# Constraints
# Incoming flow to each city
for j in cities:
    prob += pulp.lpSum([x[(i, j)] for i in cities if i != j]) == 1

# Outgoing flow from each city
for i in cities:
    prob += pulp.lpSum([x[(i, j)] for j in cities if i != j]) == 1

# Subtour Elimination Constraints
for s in range(2, len(cities)):
    for S in itertools.combinations(cities, s):
        prob += pulp.lpSum([x[(i, j)] for i in S for j in S if i != j]) <= len(S) - 1

# Solve the problem using the default solver
prob.solve()

# Output the solution
tour = []
current_city = 0
total_cost = 0

for _ in range(len(cities)):
    for j in cities:
        if pulp.value(x[(current_city, j)]) == 1:
            tour.append(j)
            total_cost += distances[(current_city, j)]
            current_city = j
            break

# Append the starting city to close the tour
tour.append(0)
total_cost += distances[(tour[-2], 0)]

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")