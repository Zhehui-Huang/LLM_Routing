from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, LpBinary
import math

# Cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities
n = len(cities)

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Variables x_ij where i, j are cities
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)

# Objective function
problem += lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j), "Total_Distance"

# Constraints
for i in cities:
    problem += lpSum(x[i, j] for j in cities if i != j) == 1, f"Leave_{i}"
    problem += lpSum(x[j, i] for j in cities if i != j) == 1, f"Enter_{i}"

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += (x[i, j] + x[j, i] <= 1)

# Solve the problem
problem.solve()

# Collect results
tour = []
visited = set()
current = 0
while True:
    tour.append(current)
    visited.add(current)

    # Find next city with x[current, j] == 1
    next_city = next(j for j in cities if j != current and x[current, j].varValue == 1)
    if next_city == 0:
        break
    current = next_city

# Ensuring the return to depot:
tour.append(0)

# Calculate the total cost
total_travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")