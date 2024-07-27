import pulp
import math

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

# Calculating distances between every pair of cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(coords)  # Number of cities including depot
dist_matrix = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Setting up the integer programming problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if path i to j is chosen
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)],
                          cat='Binary', lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination (creating a large number of constraints could be inefficient, only reasonable for small n)
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
prob.solve()

# Finding the optimal tour
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if pulp.value(x[current, j]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

if tour[0] != 0:  # Ensure to start at depot
    tour = [0] + tour
total_cost = pulp.value(prob.objective)

print(f"Tour: {tour + [0]}")
print(f"Total travel cost: {total_cost}")