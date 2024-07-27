import pulp
import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Robot depots
depots = [0, 1, 2, 3]

# Number of total cities
num_cities = len(coordinates)

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Problem instance
problem = pulp.LpProblem("VRP_Multiple_Depots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in depots),
                          cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) if i != j for k in depots)

# Constraints

# Only one tour starts from each depot per robot
for k in depots:
    problem += pulp.lpSum(x[(k, j, k)] for j in range(num_cities) if j != k) == 1

# Only one tour ends at each depot per robot
for k in depots:
    problem += pulp.lpSum(x[(j, k, k)] for j in range(num_cities) if j != k) == 1

# Ensure each city is visited exactly once by exactly one robot
for j in range(num_cities):
    if j not in depots:
        problem += pulp.lpSum(x[(i, j, k)] for k in depots for i in range(num_cities) if i != j) == 1

# Ensure route continuity for non-depot nodes
for j in range(num_cities):
    if j not in depots:
        for k in depots:
            problem += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities) if i != j)

# Solving the model
problem.solve()

# Output the solution
overall_cost = 0
for k in depots:
    tour_cost = 0
    print(f"Robot {k} Tour:", end=" ")
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and pulp.value(x[(i, j, k)]) == 1:
                tour_cost += distance_matrix[i][j]
                print(f"{i} -> ", end="")
    print(f"{k}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}\n")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")