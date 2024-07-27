import pulp
import math

# City coordinates
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
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Problem initialization
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat=pulp.LpBinary)

# Objective function: Minimize the total travel cost
problem += pulp.lpSum(distance(i, j) * x[(i, j)] for i in coordinates for j in coordinates if i != j), "Total_Cost"

# Constraints
# Each group must connect exactly once to an outside node
for group, cities in groups.items():
    problem += pulp.lpSum(x[(i, j)] for i in cities for j in coordinates if j not in cities) == 1
    problem += pulp.lpSum(x[(j, i)] for i in cities for j in coordinates if j not in cities) == 1

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", [i for i in coordinates], lowBound=0, cat=pulp.LpInteger)
k = len(coordinates)  # Total number of cities
for i in coordinates:
    for j in coordinates:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + k * x[(i, j)] + (k-2) * x[(j, i)] <= k - 1

# Solve the problem
problem.solve()

# Output results
tour = []
visited = set()
current_city = 0
while True:
    visited.add(current_city)
    tour.append(current_city)
    next_cities = [j for j in coordinates if x[(current_city, j)].value() == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    current_city = next_city
    if current_city == 0:
        break

print("Tour:", tour + [0])
print("Total travel cost:", pulp.value(problem.objective))