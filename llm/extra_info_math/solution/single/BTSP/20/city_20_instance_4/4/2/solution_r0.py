import pulp
import math
from itertools import combinations

# Cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
n = len(cities)

# Distance calculation (Euclidean)
def get_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Problem setup
problem = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=pulp.LpBinary)  # Tour variables
d_max = pulp.LpVariable("d_max", lowBound=0, cat=pulp.LpContinuous)  # Max distance variable

# Objective
problem += d_max, "Minimize_the_maximum_distance"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city once
    
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * get_distance(cities[i], cities[j]) <= d_max  # Distance constraints

# Sub-tour elimination
for size in range(2, n):
    for S in combinations(range(n), size):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= size - 1

# Solve the problem
status = problem.solve()
tour_order = []
visited = [0] * n
current_city = 0
visited[current_city] = 1
tour_order.append(current_city)

# Retrieve the tour
while True:
    next_cities = [(j, x[current_city, j].varValue) for j in range(n) if j != current_city]
    for city, used in next_cities:
        if used > 0.5 and not visited[city]:
            tour_order.append(city)
            visited[city] = 1
            current_city = city
            break
    if current_city == 0:
        break

# Calculate the total cost and max distance
total_cost = sum(get_distance(cities[tour_order[i]], cities[tour_order[i + 1]]) for i in range(len(tour_order) - 1))
max_distance = max(get_distance(cities[tour_order[i]], cities[tour_order[i + 1]]) for i in range(len(tour_order) - 1))

# Output
print("Tour:", [ti for ti in tour_order])
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", d_max.varValue)