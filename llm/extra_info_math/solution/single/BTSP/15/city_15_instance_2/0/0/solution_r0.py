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
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Binary decision variables: x[i][j] is 1 if we travel from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat=pulp.LpBinary)

# Minimax objective variable
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective function
prob += max_distance

# Constraints
for i in cities:
    prob += pulp.lpSum([x[i, j] for j in cities if i != j]) == 1  # Leaving each city
    prob += pulp.lpSum([x[j, i] for j in cities if i != j]) == 1  # Entering each city

# Max distance constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * euclidean_distance(i, j) <= max_distance

# Solve the problem
prob.solve()

# Retrieve the solution
tour = []
distance = 0
current_city = 0
visited = set()
while True:
    for j in cities:
        if j != current_city and x[current_city, j].value() == 1:
            distance += euclidean_distance(current_state, j)
            visited.add(j)
            tour.append(j)
            current_city = j
            break
    if current_city == 0:
        break

# Calculate the maximum edge distance in the tour
max_edge_distance = max(
    euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)
)

# Display the results
print("Tour:", [0] + tour + [0])
print("Total travel cost:", sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)))
print("Maximum distance between consecutive cities:", max_edge_distance)