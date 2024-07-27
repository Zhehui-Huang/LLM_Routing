import pulp
import math

# Define the data for cities including the depot
cities = [
    (54, 87),  # City 0 - Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(cities)
distances = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j and (i, j) in x) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j and (j, i) in x) == 1

# Subtour elimination constraints
for k in range(3, n+1):
    for S in itertools.combinations(range(1, n), k):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j and (i, j) in x) <= len(S) - 1

# Solve the problem
model.solve()

# Retrieve the solution
tour = []
visited = [0]
while len(visited) < n:
    for j in range(n):
        if x[visited[-1], j].varValue == 1:
            visited.append(j)
            break
tour = visited + [0]

# Calculate the total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")