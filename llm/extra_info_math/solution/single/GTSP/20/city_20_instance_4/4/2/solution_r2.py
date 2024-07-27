from math import sqrt
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Coordinates for the cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

# Calculate the Euclidean distance between any two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create variables for the problem
var_dict = {(i, j): LpVariable(f"x_{i}_{j}", cat=LpBinary) for i in cities for j in cities if i != j}

# Create the problem
prob = LpProblem("TSP-Variant", LpMinimize)

# Create the objective function
prob += lpSum(var_dict[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j and var_dict.get((i, j)))

# Adding the constraints
# Each group exactly one city must be visited
for group in groups:
    prob += lpSum(var_dict[i, j] for i in group for j in cities if i != j and var]var_dict.get.get((i, j), None) == 1

# Each city (except depot) must have exactly one outgoing connection
for j in cities:
    if j != 0:
        prob += lpSum(var_dict[i, j] for i in cities if i != j and var_dict.get((i, j))) == lpSum(var_dict[j, k] for k in cities if j != k and var_dict.get((j, k)))

# Start and end at the depot
prob += lpSum(var_dict[0, j] for j in cities if j != 0 and var_dict.get((0, j))) == 1
prob += lpSum(var_dict[j, 0] for j in cities if j != 0 and var_dict.get((j, 0))) == 1

# Solve the problem
prob.solve()

# Extracting the solution
tour = [0]
current_city = 0
for _ in range(len(cities) - 1):
    next_city = next((j for j in cities if j != current_city and var_dict[current_city, j].value() == 1), None)
    if next_city is None:
        break
    tour.append(next_city)
    current_city = next_city

# Include return to the depot
tour.append(0)

# Calculating total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)