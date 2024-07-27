from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define the points (cities) and their coordinates
points = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define the city groups
city_groups = [
    [7, 9], [1, 3], [4, 6], [8], [5], [2]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# All cities including depot
V = list(points.keys())

# Create a LP problem instance
model = LpProblem(name="minimum-travel-cost-tsp", sense=LpMinimize)

# Variables x_ij where i, j in V
x = LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat=LpBinary)

# Objective Function: Minimize the travel cost
model += lpSum(euclidean_distance(points[i], points[j]) * x[i, j] for i in V for j in V if i != j)

# Constraints for entering and leaving each node
for j in V:
    model += lpSum(x[i, j] for i in V if i != j) == lpSum(x[j, k] for k in V if j != k)

# Additional constraints to ensure each group is visited exactly once
for group in city_groups:
    model += lpSum(x[i, j] for i in group for j in V if j not in group) == 1  # exit each group exactly once
    model += lpSum(x[j, i] for i in group for j in V if j not in group) == 1  # enter each group exactly once

# Solve the model
model.solve()

# Extract the solution
tour = [0]
for _ in range(len(city_groups)):
    next_city = next(j for i in tour for j in V if i != j and x[i, j].value() == 1)
    tour.append(next_city)

# Add return to the depot city
tour.append(0)

# Calculate the total travel cost
total_cost = sum(euclidean cancelpoints[tour[i]], points[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")