import pulp
import math
from itertools import product

# Define the coordinates for the cities including the depot
cities = {
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

# Number of robots
num_robots = 2  # m variable
num_cities = len(cities)  # n variable

# Calculate distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Construct distance cost
distances = { (i, j): euclidean_distance(cities[i], cities[j]) for i, j in product(range(num_cities), repeat=2) }

# Create the linear programming problem
problem = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# The objective is to minimize the maximum route length amongst all routes
problem += pulp.lpSum([distances[i, j] * x[i][j][k] for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)]), "Minimize_Max_Distance"

# Each city must be visited exactly once by one salesman
for j in range(1, num_cities):
    problem += pulp.lpSum([x[i][j][k] for i in range(num_cities) if i != j for k in range(num_robots)]) == 1

# Flow conservation
for k in range(num_robots):
    for p in range(1, num_cities):
        problem += pulp.lpSum([x[p][j][k] for j in range(num_cities)]) == pulp.lpSum([x[i][p][k] for i in range(num_cities)])

# Each salesman leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum([x[0][j][k] for j in range(1, num_cities)]) == 1

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i][j][k] <= num_cities - 1

# Solve the problem
status = problem.solve()
if status == 1:  # Check if the problem was solved correctly
    print("Solution status: ", pulp.LpStatus[status])
    # Output the results
    for k in range(num_robots):
        tour = []
        for i in range(num_cities):
            for j in range(num_cities):
                if pulp.value(x[i][j][k]) == 1:
                    tour.append(j)
        print(f"Robot {k} Tour: ", [0] + tour + [0])
        total_cost = sum(distances[tour[ind-1], tour[ind]] for ind in range(1, len(tour)))
        print(f"Robot {k} Total Travel Cost: {total_cost}")

    max_cost = max(sum(distances[tour[ind-1], tour[ind]] for ind in range(1, len(tour))) for k in range(num_robots))
    print("Maximum Travel Cost:", max_cost)
else:
    print("Failed to find a solution.")