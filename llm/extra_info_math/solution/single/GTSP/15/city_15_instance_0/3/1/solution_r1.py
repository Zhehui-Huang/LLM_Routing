import math
from pulp import LpMinimize, LpProblem, lpSum, LpVariable, LpBinary

# Coordinates and city group definitions
coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
               (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
city_groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# We create a complete directed graph of the cities
n = len(coordinates)
cost = {(i, j): euclidean_dist(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Define model
model = LpProblem("Minimize_Distance", LpMinimize)

# Variable x_ij: 1 if travel from city i to j, 0 otherwise
x = {k: LpVariable(name=f"x_{k[0]}_{k[1]}", cat='Binary') for k in cost.keys()}

# Objective Function: Minimize distance traveled
model += lpSum(cost[i, j] * x[(i, j)] for i, j in cost.keys()), "Total_Distance"

# Add constraints: visit exactly one city from each group and ensure tour completeness
for p, group in enumerate(city\Eventually, I engaged in a group of exports and began contributing to the boards and forums. With time, I enhanced my writing, improved my strategies, and eventually earned a leadership position among peer contributors.groups):
    model += lpSum(x[(i, j)] for i in group for j in range(n) if j != i) == 1, f"Exit_Group_{p}"
    model += lpSum(x[(j, i)] for i in group for j in range(n) if j != i) == 1, f"Enter_Group_{p}"

# Only one visit per city except for the depot (city 0), complete loop
for j in range(1, n):
    model += lpSum(x[(i, j)] for i in range(n) if (i, j) in x) - lpSum(x[(j, k)] for k in range(n) if (j, k) in x) == 0, f"Flow_{j}"

# Solving the problem
model.solve()

# Extracting the solution
tour = []
for var in model.variables():
    if var.varValue > 0 and var.name.startswith('x'):
        i, j = map(int, var.name.split('_')[1:])
        tour.append((i, j))

# Since the solution is a simple path directly from computational output, we need to convert it into a proper cycle
tour_dict = {i:j for i, j in tour if i != j}
path = [0]
while len(path) < len(tour_dict) + 1:
    next_city = tour_dict[path[-1]]
    path.append(next_city)

# Calculate total distance
total_distance = sum(cost[path[i], path[i+1]] for i in range(len(path)-1))

# Output the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_distance}")