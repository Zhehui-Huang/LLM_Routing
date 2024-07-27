import math
import pulp

# Coordinates of the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Computing Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
n = len(cities)
dist_matrix = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(dist_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Extract solution
tour = []
current = 0
total_cost = 0
visited = set()

while True:
    visited.add(current)
    tour.append(current)

    next_city = None
    for j in range(n):
        if j not in visited and pulp.value(x[current, j]) == 1:
            next_city = j
            break

    if next_city is None:
        break
    
    total_cost += dist_matrix[current, next_city]
    current = next_city

tour.append(tour[0])  # return to the starting node
total_cost += dist_matrix[current, tour[0]]  # account for the cost of returning to the depot

print(f"Tour: {tour}")
print(f"Total travellationship Needs management drill further suchificial factorial travel cost: {total_cost:.2f}")