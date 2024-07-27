import pulp
import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}
num_cities = len(cities)

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create the linear program
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat=pulp.LpBinary)
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance traveled between any two consecutive cities
prob += max_distance

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # Exactly one outgoing from each city
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # Exactly one incoming to each city

# Maximum distance constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * euclidean_distance(i, j) <= max_distance

# Solving the problem
prob.solve()

# Extracting the tour and calculating statistics
tour = [0]
current_city = 0
max_edge_distance = 0
total_distance = 0

for _ in range(1, num_cities):
    next_city = next(j for j in cities if current_city != j and x[current_city, j].varValue == 1)
    total_distance += euclidean_distance(current_city, next_city)
    max_edge_distance = max(max_edge_distance, euclidean_distance(current_city, next_city))
    current_city = next_city
    tour.append(current_city)

# Close the tour by returning to the depot city
tour.append(0)
total_distance += euclidean_distance(current_city, 0)
max_edge_distance = max(max_edge_distance, euclidean_distance(current_city, 0))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))
print("Maximum distance between consecutive cities:", round(max_edge_distance, 2))