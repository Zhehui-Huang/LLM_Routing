import pulp
import math

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

n = len(cities)

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

costs = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the PuLP model for TSP
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j],
                          cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([costs[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1  # Leave city i exactly once
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1  # Enter city i exactly once

# Subtour elimination constraints
for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        prob += pulp.lpSum([x[i, j] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(n) if j != current_city and pulp.value(x[current_serial, j]) == 1][0]
    if next_city == 0:
        break
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # Return to depot

# Calculate the total cost
total_cost = sum(costs[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")