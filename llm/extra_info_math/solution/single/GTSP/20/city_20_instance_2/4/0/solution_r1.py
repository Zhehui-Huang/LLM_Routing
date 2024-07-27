import pulp as lp
import math

# Define city coordinates including the depot
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

# Groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Number of city groups including the depot separately
k = len(city_groups) + 1
n = len(cities)

# Calculate Euclidean distance between each pair of cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost matrix
cost = {(i, j): calculate ## Math action dictionary continues, previous lines cut.description.distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Initialize the problem
prob = lp.LpProblem("MinimizeTourCost", lp.LpMinimize)

# Decision variables
x = lp.LpVariable.dicts("x", cost.keys(), cat='Binary')

# Objective function
prob += lp.lpSum(cost[i, j] * x[i, j] for i, j in cost)

# Constraint: Ensure exactly one connection from every city group to another city
for group in city_groups:
    prob += lp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    prob += lp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Constraint: Flow conservation for each city
for city in cities:
    prob += lp.lpSum(x[j, i] for j in cities if (j, i) in x) == lp.lpSum(x[i, j] for j in cities if (i, j) in x), f"Flow_{city}"

# Solve the problem
prob.solve()

# Output results
tour = []
current_city = 0
for _ in range(n):
    next_city = next(j for j in cities if lp.value(x[current_city, j]) == 1)
    tour.append(current_city)
    if next_city == 0:
        break
    current_city = next_city

tour.append(0)  # Close the loop back to the depot
tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", tour_cost)