import pulp
import math
import itertools

# City coordinates
coords = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(coords)  # Number of cities including depot
dist_matrix = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i!=j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i,j] for j in range(n) if i!=j) == 1
    prob += pulp.lpSum(x[j,i] for j in range(n) if i!=j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
steps = 0
while True:
    next_city = [j for j in range(n) if pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    steps += 1
    if steps > n:
        break

# Closing the tour by returning to depot
tour.append(0)

# Calculate the tour cost
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Printing the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")