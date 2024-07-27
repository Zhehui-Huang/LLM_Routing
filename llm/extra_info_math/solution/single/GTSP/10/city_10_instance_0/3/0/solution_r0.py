import pulp
import math

# Define the city coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
city_groups = {
    1: [1, 2, 6],
    2: [3, 7, 8],
    3: [4, 5, 9]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the problem
problem = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(10) for j in range(10) if i != j], cat='Binary')

# Objective function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(10) for j in range(10) if i != j)

# Constraints
# Each group exactly one outgoing and incoming
for group, cities in city_groups.items():
    problem.addConstraint(pulp.lpSum(x[(i, j)] for i in cities for j in set(range(10)) - set(cities)) == 1)
    problem.addConstraint(pulp.lpSum(x[(j, i)] for i in cities for j in set(range(10)) - set(cities)) == 1)

# Flow conservation
for i in range(10):
    problem.addConstraint(pulp.lpSum(x[(i, j)] for j in range(10) if i != j) - pulp.lpSum(x[(j, i)] for j in range(10) if i != j) == 0)

# Solve the problem
problem.solve()

# Extract the tour path
path = []
current = 0
visited = set()
while True:
    next_city = [j for j in range(10) if j != current and pulp.value(x[(current, j)]) == 1]
    if next_city:
        next_city = next_city[0]
        path.append(next_city)
        visited.add(next_city)
        current = next_city
        if current == 0:
            break

# Place depot as start and end
path = [0] + path + [0]

# Calculate total cost
total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path)-1))

# Output Result
print("Tour:", path)
print("Total travel cost:", total_cost)