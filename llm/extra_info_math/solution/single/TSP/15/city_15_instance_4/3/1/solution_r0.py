import pulp
import math

# City coordinates indexed by city number, city 0 is the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord1[1])**2 + (coord2[0] - coord2[1])**2)

n = len(coordinates)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[i, j] = 0

# Setting up the problem: Minimization
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if path i to j is chosen, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          cat='Binary')

# Objective function
model += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: ensure each city is arrived at and departed from exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Depart_from_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Arrive_at_{i}"

# Subtour elimination constraints
for s in range(2, n):
    for subset in itertools.combinations(range(1,n), s):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subsect) - 1

# Solve the problem
model.solve()

# Extracting the results
tour = []
current = 0  # start from depot
while True:
    tour.append(current)
    next_cities = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    current = next_cities[0]

# closing the tour by returning to depot
tour.append(0)

# Total travel cost calculation
total_cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")