import pulp
import math

# Define city coordinates and groups
city_coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize LP model
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coordinates for j in city_coordinates if i != j),
                          cat=pulp.LpBinary)

# Objective Function
prob += pulp.lpSum(x[i, j] * distance(city_coordinates[i], city_coordinates[j]) for i in city_coordinates for j in city_coordinates if i != j)

# Constraints

# One outgoing edge from each city, considering exactly one per group
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in city_coordinates if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in city_coordinates if j not in group) == 1

# Flow conservation at each node
for city in city_coordinates:
    if city != 0:
        prob += (pulp.lpSum(x[j, city] for j in city_coordinates if j != city) ==
                 pulp.lpSum(x[city, j] for j in city_coordinates if j != city))
        
# Adding depots start and end conditions
prob += pulp.lpSum(x[0, j] for j in city_coordinates if j != 0) == 1
prob += pulp.lpSum(x[i, 0] for i in city_coordinates if i != 0) == 1

# Solve the problem
prob.solve()

# Extract tour from the variables
tour = [0]
total_distance = 0

while True:
    this_city = tour[-1]
    next_moves = [j for j in city_coordinates if j != this_city and pulp.value(x[this_city, j]) == 1]
    if not next_moves:
        break
    next_city = next_moves[0]
    tour.append(next_city)
    total_distance += distance(city_coordinates[this_city], city_coordinates[next_city])
    
    if next_city == 0:
        break

# Output the tour and the total distance
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_distance, 2)}")