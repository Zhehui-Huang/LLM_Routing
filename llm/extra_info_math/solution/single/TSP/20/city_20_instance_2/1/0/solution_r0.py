import pulp
import math

# City coordinates including the depot city
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if the path i to j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')

# Objective function: Minimize the sum of the distances of the paths taken
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints: Ensure each city is arrived at and left exactly once
for k in cities:
    model += pulp.lpSum(x[i, k] for i in cities if i != k) == 1  # Arriving
    model += pulp.lpSum(x[k, j] for j in cities if k != j) == 1  # Leaving

# Solve the model
status = model.solve()

# Extract the tour from the variables
tour = []
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Include the depot city
tour = [0] + tour + [0]

# Total travel cost
total_cost = pulp.value(model.objective)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)