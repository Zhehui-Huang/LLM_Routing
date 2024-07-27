import math
from pulp import *

# City coordinates keyed by city index
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Grouping of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

all_cities = list(city_coords.keys())
selected_cities = [min(group, key=lambda x: distance(0, x)) for group in city_groups.values()] + [0]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# TSP problem
prob = LpProblem("TSP", LpMinimize)

# Variables x[i,j] for each pair i,j of cities
x = LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], cat='Binary')

# Objective function: minimize the travel distance
prob += (lpSum(x[i, j] * distance(i, j) for i in selected_cities for j in selected_cities if i != j), "total_distance")

# Constraint for coming in and out of each city
for c in selected_cities:
    prob += (lpSum(x[i, c] for i in selected_cities if i != c) == 1, f"enter_{c}")
    prob += (lpSum(x[c, j] for j in selected_cities if c != j) == 1, f"leave_{c}")

# Solve the problem
prob.solve()

# Output the tour and total cost
route = []
current_position = 0
total_cost = 0

# Generate route starting from the depot city
for _ in range(len(selected_cities)):
    for next_city in selected_cities:
        if x[current_position, next_city].varValue == 1:
            route.append(next_city)
            total_cost += distance(current_position, next_city)
            current_position = next_city
            break

# Close the loop to the start city
route.append(0)
total_cost += distance(current_position, 0)

# Print results
print(f"Tour: {route}")
print(f"Total travel cost: {total_cost}")