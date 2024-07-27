import pulp
from math import sqrt

# Cities coordinates
coordinates = {
    0: (30, 40),  # Depot city 0
    1: (37, 52),  # Depot city 1
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

# Parameters of the problem
num_robots = 2
num_cities = len(coordinates)

def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Model setup
model = pulp.LpProblem("Robot_Routing_Problem", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(num_cities)), lowBound=0, upBound=num_cities - 1, cat='Integer')

# Objective Function
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for j in range(2, num_cities):
    model += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1  # Each city is entered exactly once
    model += pulp.lpSum(x[j, i] for i in range(num_cities) if i != j) == 1  # Each city is left exactly once

# Salesmen leave and return to their designated depots
for i in [0, 1]:  # Depots
    model += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1  # Salesman starts from the depot
    model += pulp.lpSum(x[j, i] for j in range(num_cities) if i != j) == 1  # Salesman ends at the depot

# Subtour elimination
for i in range(2, num_cities):
    for j in range(2, num_cities):
        if i != j:
            model += u[i] - u[j] + (num_cities - 1) * x[i, j] <= num_cities - 2

# Solve the problem
status = model.solve()

# Output the results
if status == pulp.LpStatusOptimal:
    print("Found optimal solution.")
    total_distance = 0
    for robot in range(num_robots):
        tour = []
        current_city = robot  # Start at the designated depot
        while True:
            next_cities = [j for j in range(num_cities) if pulp.value(x[current_city, j]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
            current_city = next_city
            if current_city <= 1:
                break
        tour_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_distance += tour_distance
        tour_cycle = [robot] + tour + [robot]
        print(f"Robot {robot} Tour: {tour_cycle}")
        print(f"Robot {robot} Total Travel Cost: {tour_distance}")
    print(f"Overall Total Travel Cost: {total_distance}")
else:
    print("No optimal solution found.")