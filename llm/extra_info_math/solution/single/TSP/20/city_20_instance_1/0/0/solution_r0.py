import pulp
import math

# Coordinates of the cities
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
          (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
          (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
          (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Number of cities
n = len(cities)

# Calculate Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cost matrix
c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the linear programming problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
problem += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total_Cost"

# Each city is arrived at once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# From each city, one must depart once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Prevent subtours
for m in range(2, n):
    for sub_set in itertools.combinations(range(1, n), m):
        problem += pulp.lpSum(x[i, j] for i in sub_set for j in sub_set if i != j) <= len(sub_fsset) - 1

# Optimize the problem
problem.solve()

# Retrieve the path
path = []
current = 0

for _ in range(n):
    next_cities = [j for j in range(n) if pulp.value(x[current, j]) == 1]
    next_city = next_cities[0]
    path.append(current)
    current = next_city

path.append(0)  # Append the starting city to close the tour

# Calculate the total cost
total_cost = sum(c[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Output
print("Tour:", path)
print("Total travel cost:", total_cost)