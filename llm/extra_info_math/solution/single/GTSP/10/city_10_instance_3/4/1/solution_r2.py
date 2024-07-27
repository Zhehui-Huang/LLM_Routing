from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# City coordinates and groups are given
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
               (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Calculate Euclidean distances between every pair of cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distances[(i,j)] = calculate_distance(coordinates[i], coordinates[j])

# Create the optimization problem
prob = LpProblem("TSP_Grouped_Cities", LpMinimize)

# Variables: x[(i,j)] is 1 if the route is travelled from i to j
x = LpVariable.dicts("x", [(i, j) for i in range(10) for j in range(10)], cat=LpBinary)

# Objective Function: Minimize the total distance travelled
prob += lpSum(x[(i, j)] * distances[(i,j)] for i in range(10) for j in range(10))

# Each city in a group has exactly one edge leaving to another city not in the group
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in range(10) if j not in group) == 1

# Each city in a group receives exactly one edge from a city not in the group
for group in groups:
    prob += lpSum(x[(j, i)] for i in group for j in range(10) if j not in group) == 1

# Flow conservation constraint to ensure we arrive at each city once and leave it once
for i in range(1, 10):  # Excluding the depot i.e., city 0
    prob += lpSum(x[(i, j)] for j in range(10) if i != j) == lpSum(x[(j, i)] for j in range(10) if i != j)

# Choose exact one city from each group
for group in groups:
    prob += lpSum(x[(0, j)] for j in group) == 1
    prob += lpSum(x[(j, 0)] for j in group) == 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current = 0
tour.append(current)

# Collect path based on next available city with x[i, j] = 1
while len(tour) <= len(groups):
    for j in range(10):
        if x[(current, j)].varValue == 1 and j not in tour:
            tour.append(j)
            current = j
            break
tour.append(0)  # return to the depot

# Calculate total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")