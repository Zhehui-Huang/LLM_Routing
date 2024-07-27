import math
import pulp

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

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate distances
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# All city indices
V = list(coords.keys())

# Define the problem
prob = pulp.LpProblem("Group_TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", [(i, j) for i in V for j in V if i != j], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j] for i in V for j in V if i != j)

# Constraints of visiting exactly one city from each group and ensuring return
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in V if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in V if j not in group) == 1

# Flow conservation constraint to maintain the tour
for city in V:
    if city != 0:  # Excluding the depot from balance constraint
        prob += (pulp.lpSum(x[j, city] for j in V if j != city) -
                 pulp.lpSum(x[city, j] for j in V if j != city) == 0)

# Solve the problem
prob.solve()

# Extract the tour and calculate cost
tour = [0]
current = 0
total_cost = 0
while True:
    next_city = [j for j in V if j != current and pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    total_cost += distance(current, next_city)
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

tour.append(0)  # Complete the tour by returning to the depot
total_cost += distance(tour[-2], 0)  # Add the cost of returning to the depot

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")