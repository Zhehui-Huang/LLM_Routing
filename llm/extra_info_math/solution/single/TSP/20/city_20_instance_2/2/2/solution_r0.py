from pulp import *
import math

# Define cities and their coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to compute Euclidean distance between two cities
def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Total number of cities including the depot
n = len(cities)

# Create the TSP model
model = LpProblem("TSP", LpMinimize)

# Decision variables: x[i, j] is 1 if we travel from city i to j
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: Minimize the travel cost
model += lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints: Enter and leave each city exactly once
for j in cities:
    model += lpSum(x[i, j] for i in cities if i != j) == 1, f"Enter_{j}"
    model += lpSum(x[j, k] for k in cities if k != j) == 1, f"Leave_{j}"

# Solve the problem
model.solve(PULP_CBC_CMD(msg=0))

# Extract the tour
tour = []
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and x[current_city, j].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Total travel cost calculation
total_travel_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Formatting output
tour = [0] + tour + [0]
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")