import pulp
import math

# Given data
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_cities = len(coordinates)

# Euclidean distance calc function
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Set up problem
problem = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(1, num_cities) for j in range(1, num_cities) if i != j for k in range(2)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective - Minimize maximum travel cost
max_travel_cost = pulp.LpVariable("max_travel_self")
problem += max_travel_cost

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(1, num_cities) for k in range(2) if i != j) == 1

# Flow conservation constraints
for k in range(2):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(1, num_cities) if i != j) \
                   - pulp.lpSum(x[j, i, k] for i in range(1, num_cities) if i != j) == 0

# Connecting depot
for k in range(2):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Travel cost constraints
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist = calc_distance(coordinates[i], coordinates[j])
            for k in range(2):  # Ensure this constraint links properly across all vehicles
                problem += x[i, j, k] * dist <= max_travel_cost

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=0))

if problem.status == pulp.LpStatusOptimal:
    print("Solution Found:")
    for k in range(2):
        tour = [0]
        while True:
            next_cities = [j for j in range(1, num_cities) if x[tour[-1], j, k].value() == 1]
            if not next_cities:
                break
            tour.append(next_cities[0])
            if next_cities[0] == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_cost = sum(calc_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        print(f"Robot {k} Travel Cost: {tour_cost}")
else:
    print("No optimal solution found.")