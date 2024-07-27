import pulp
import math

# Define the coordinates of each city, including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance between pairs of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Setup the Problem
n = len(coordinates)  # number of cities including the depot
dist = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the TSP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: Minimize the sum of distances travelled
prob += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: Each city is visited and left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour Elimination
for size in range(2, n):
    for subset in itertools.combinations(range(n), size):
        prob += (pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Solve the problem
status = prob.solve()

# Retrieve the solution
tour = []
visited = [0]
while len(visited) < n:
    k = visited[-1]
    for j in range(n):
        if j != k and pulp.value(x[k, j]) == 1:
            visited.append(j)
            tour.append(j)
            break
tour = [0] + tour + [0]

total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")