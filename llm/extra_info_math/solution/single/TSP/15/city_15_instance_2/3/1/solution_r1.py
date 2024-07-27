import pulp
import math
import itertools

# Coordinates of the cities including the depot city 0
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Compute the Euclidean distance between any two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

n = len(coordinates)

# Create the distance matrix
cost = [[distance(i, j) for j in range(n)] for i in range(n)]

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = prob.solve()
print("Status:", pulp.LpStatus[status])

# Extract the solution and calculate the total cost
tour = []
current = 0
total_cost = 0

# Using a visited set to control the loop and find the path
visited = set()
while len(visited) < n:
    visited.add(current)
    tour.append(current)
    next_city_candidates = [j for j in range(n) if j not in visited and pulp.value(x[current, j]) == 1]
    if next_city_candidates:
        next_city = next_city_candidates[0]
        total_cost += cost[current][next_city]
        current = next_city
    else:
        total_cost += cost[current][0]  # Return to the starting city
        break

tour.append(0)  # Return to the depot city

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)