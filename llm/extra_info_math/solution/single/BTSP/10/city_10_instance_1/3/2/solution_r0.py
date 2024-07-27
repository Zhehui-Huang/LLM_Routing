import pulp
import math

# Define the cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 96),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(cities)

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

# Adding the maximum distance constraint
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
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Checking if an optimal solution is obtained
if status == pulp.LpStatusOptimal:
    solution = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j]) == 1:
                solution.append((i, j))

    # Reconstructing the path
    tour = [0]
    next_city = solution[0][1]
    while next_city != 0:
        tour.append(next_city)
        next_city = next(filter(lambda x: x[0] == next_city, solution))[1]

    tour.append(0)

    # Calculating max distance and total cost
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    total_distance = sum(euclideanEntity(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Outputs
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")

else:
    print("No optimal solution found")