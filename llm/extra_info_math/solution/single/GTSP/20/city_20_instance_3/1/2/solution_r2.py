import pulp
import math

# Data: Coordinates of cities including the depot (0 index)
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups of city indices excluding the depot
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Problem initialization
prob = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Flatten group list to include all grouped cities in optimization
all_grouped_cities = [city for group in groups for city in group]

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in [0] + all_grouped_cities for j in [0] + all_grouped_cities if i != j], cat='Binary')

# Objective function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in [0] + all_grouped_cities for j in [0] + all_grouped_cities if i != j)

# Constraints to ensure exactly one exit and entrance from each city in groups
for group in groups:
    prob += pulp.lpSum(x[(0, j)] for j in group) == 1
    prob += pulp.lpSum(x[(j, 0)] for j in group) == 1

# Continuity within the route for non-depot cities
for city in all_grouped_cities:
    prob += pulp.lpSum(x[(i, city)] for i in [0] + all_grouped_cities if i != city) == pulp.lpSum(x[(city, j)] for j in [0] + all_grouped_cities if j != city)

# Optimizing the problem
prob.solve()

# Determine the optimized route
current_city = 0
tour = [current_city]
visited = set(tour)
while True:
    possible_moves = [(j, x[(current_city, j)].varValue) for j in [0] + all_grouped_cities if j != current_city]
    next_city = next(j for j, varValue in possible_moves if varValue is not None and varValue > 0)
    if next_city == 0:
        tour.append(next_city)
        break
    elif next_city not in visited:
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city

# Calculate the total cost from the tour
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)