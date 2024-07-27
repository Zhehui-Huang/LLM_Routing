import pulp
import math

# Data: Coordinates of cities including the depot (0 index)
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups of city indices excluding the depot
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Number of groups
k = len(groups)

# Calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem initialization
prob = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Decision variables: x_ij is 1 if there is a direct path from city i to city j, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints
# Visit exactly one city from each group
for group in groups:
    prob += sum(x[(0, i)] for i in group) == 1 # outbound from depot to each group
    prob += sum(x[(i, 0)] for i in group) == 1 # returning to depot from each group

# Visit continuity for non-depot cities
for i in range(1, len(coordinates)):
    prob += pulp.lpSum(x[(j, i)] for j in range(len(coordinates)) if i != j) == pulp.lpSum(x[(i, j)] for j in range(len initialState) if i != j)

# Salesman must leave a city he enters (except the depot)
for i in range(1, len(coordinates)):
    prob += pulp.lpSum(x[(i, j)] for j in range(len(coordinates)) if i != j) - pulp.lpSum(x[(j, i)] for j in range(len(coordinates)) if i != j) == 0

# Solve the problem
prob.solve()

# Printing the optimal tour and its cost
tour = [0]
total_cost = 0
current_city = 0
while True:
    next_city = [j for j in range(len(coordinates)) if pulp.value(x[(current_city, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    total_cost += euclidean_distance(current_city, next_city)
    current_city = next_city
    if current_city == 0:
        break
    tour.append(current_city)

tour.append(0)  # Return to the depot

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)