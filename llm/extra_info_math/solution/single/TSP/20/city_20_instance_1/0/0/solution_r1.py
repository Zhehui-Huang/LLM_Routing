import pulp
import math
import itertools

# Coordinates of the cities
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
          (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
          (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
          (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Number of cities
n = len(cities)

# Function to calculate Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cost matrix
c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the linear programming problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Defining variables
x = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x({i},{j})", cat='Binary')

# Objective
problem += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination
for m in range(2, n):
    for S in itertools.combinations(range(1, n), m):
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the solution
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(current_city)
    current_city = next_city
    if current_city == 0:
        break

# Append the initial city to complete the tour
tour.append(0)

# Calculate the total travel distance
total_distance = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Result
print("Tour:", tour)
print("Total travel cost:", total_distance)