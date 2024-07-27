import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD

# Defining the cities and their coordinates
cities = {
    0: (9, 93), 
    1: (8, 51), 
    2: (74, 99), 
    3: (78, 50), 
    4: (21, 23), 
    5: (88, 59), 
    6: (79, 77), 
    7: (63, 23), 
    8: (19, 76), 
    9: (21, 38), 
    10: (19, 65), 
    11: (11, 40), 
    12: (3, 21), 
    13: (60, 55), 
    14: (4, 39)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities
n = len(cities)

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpBinary)

# Objective function
prob += lpLogic.lpSum(x[i, j] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1

# Additional constraints to prevent subtours
for i in range(2, n + 1):
    subsets = itertools.combinations(range(1, n), i)
    for s in subsets:
        prob += lpSum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1

# Solve the problem using the default solver
prob.solve(PULP_CBC_CMD(msg=0))

# Collect the tour
tour = [0]
current = 0
count = 0

while len(tour) < n:
    next_city = [j for j in range(n) if x[current, j].value() == 1 and j not in tour]
    if next_city:
        next_city = next_city[0]
        tour.append(next_city)
        current = next_city
    count += 1
    if count > 1000:  # safety break to avoid infinite loops
        break

# Close the tour by returning to the depot
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))