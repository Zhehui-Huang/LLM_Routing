import math
import pulp

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91),
    (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance
def euclidean_dist(i, j):
    dx = cities[i][0] - cities[j][0]
    dy = cities[i][1] - cities[j][1]
    return math.sqrt(dx*dx + dy*dy)

n = len(cities)

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
model += pulp.lpSum(x[(i, j)] * euclidean_dist(i, j) for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1   # Leave city i
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1   # Enter city i

# Subtour elimination
for sub_size in range(2, n):
    for s in itertools.combinations(range(1, n), sub_size):
        model += pulp.lpSum(x[(i, j)] for i in s for j in s if i != j) <= len(s) - 1

# Solve the model
model.solve()

# Extract tour
tour = []
visited = [0]
while len(visited) < n:
    for i in range(n):
        if pulp.value(x[(visited[-1], i)]) == 1:
            visited.append(i)
            break
tour = visited + [0]   # return to depot

# Calculate total cost
total_cost = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the tour and total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")