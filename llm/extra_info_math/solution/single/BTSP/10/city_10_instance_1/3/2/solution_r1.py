import pulp
import itertools
import math

# Define the cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

n = len(cities)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the problem
prob = pulp.LpProblem("TSP_Min_Max_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += d

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1
    
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(cities[i], cities[j]) <= d

# Sub-tour elimination constraints
for s in range(2, n):
    subsets = itertools.combinations(range(n), s)
    for subset in subsets:
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Output results
tour = []
next_city = 0
visited = set([0])

for _ in range(n):
    for j in range(n):
        if j not in visited and pulp.value(x[next_city, j]) == 1:
            tour.append(j)
            visited.add(j)
            next_city = j
            break

tour = [0] + tour + [0]

total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")