import pulp
import math
from itertools import product

# Cities coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Compute Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost matrix creation to represent distances between each city pair (undirected)
cost_matrix = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j}

# Define the problem
model = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables: x_i,j,k = 1 if travel from i to j by robot k
x_vars = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat=pulp.LpBinary) 
          for k in [0, 1] for i in coordinates for j in coordinates if i != j}

# Objective function: Minimize the total distance travelled
objective = pulp.lpSum(x_vars[i, j, k] * cost_matrix[i, j] for k in [0, 1] for i in coordinates for j in coordinates if i != j)
model += objective

# Constraint: Each city is entered exactly once (ignoring depots)
for j in coordinates:
    if j not in [0, 1]:
        model += pulp.lpSum(x_vars[i, j, k] for k in [0, 1] for i in coordinates if (i, j, k) in x_vars) == 1

# Constraint: Route continuity for each robot k
for k in [0, 1]:
    for i in coordinates:
        if i != k:  # Ignore depots themselves
            model += pulp.lpSum(x_vars[j, i, k] for j in coordinates if (j, i, k) in x_vars) \
                     == pulp.lpSum(x_vars[i, j, k] for j in coordinates if (i, j, k) in x_vars)

# Additional constraints to ensure robots return to their respective depots
for k in [0, 1]:
    model += pulp.lpSum(x_vars[k, j, k] for j in coordinates if j != k) == 1  # leave depot k
    model += pulp.lpSum(x_vars[j, k, k] for j in coordinates if j != k) == 1  # return to depot k

# Solve the problem
model.solve()

# Retrieve results
if model.status == pulp.LpStatusOptimal:
    robot_tours = {0: [], 1: []}
    for k in [0, 1]:
        current_city = k
        sequence = []
        while True:
            next_city = next(j for j in coordinates if j != current_city and pulp.value(x_vars[current_city, j, k]) == 1)
            sequence.append(next_city)
            current_city = next_city
            if current_city == k:
                break
        robot_tours[k] = [k] + sequence + [k]
    
    total_cost = sum(cost_matrix[i, j] * pulp.value(x_vars[i, j, k]) for k in [0, 1] for i in coordinates for j in coordinates if i != j)
    
    for k in [0, 1]:
        partial_cost = sum(cost_matrix[robot_tours[k][i], robot_tours[k][i+1]] for i in range(len(robot_tours[k]) - 1))
        print(f"Robot {k} Tour: {robot_tours[k]}")
        print(f"Robot {k} Total Travel Cost: {partial_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution found.")