import pulp
import math

# Define coordinates of cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculating Euclidean distances
def euclidean_distance(i, j):
    xi, yi = cities[i]
    xj, yj = cities[j]
    return math.sqrt((xi - xj)**2 + (yi - yj)**2)

# Construct the LP problem instance
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
objective = pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in cities for j in cities if i != j)
prob += objective

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # must leave city i
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # must enter city i

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = []
active = 0
while len(tour) < len(cities):
    tour.append(active)
    for j in cities:
        if j != active and pulp.value(x[active, j]) == 1:
            active = j
            break
tour.append(0)  # return to depot city

# Calculate the travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))