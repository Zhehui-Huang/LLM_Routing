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
num_cities = len(coordinates)

def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Model setup
model = pulp.LpProblem("Robot_Routing_Problem", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), 2, num_cities-1, cat=pulp.LpInteger)

# Objective Function to minimize total travel distance
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each city must be visited and left exactly once
for j in range(2, num_cities):
    model += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1  # Each city entered exactly once except depot
    model += pulp.lpSum(x[j, i] for i in range(num_cities) if i != j) == 1  # Each city left exactly once except depot 

# Subtour Elimination Constraints
for i in range(2, num_cities):
    for j in range(2, num_cities):
        if i != j:
            model += u[i] - u[j] + (num_cities - 1) * x[i, j] <= num_cities - 2

# Depot constraints
model += pulp.lpSum(x[0, j] for j in range(1, num_cities)) == 2     # All tours will start from Depot 0
model += pulp.lpSum(x[j, 1] for j in range(2, num_cities)) == 2     # All tours will end at Depot 1

# Resolve the model
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract results and calculate the travel cost
tours = {}
costs = {}
for k in [0]:  # Starting depots
    tour = [k]
    current_city = k
    next_city = None
    while True:
        next_city = [j for j in range(num_cities) if pulp.value(x[current_city, j]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        if next_city in tour:
            break
        tour.append(next_city)
        current_city = next_city
    if tour[-1] != 1:
        tour.append(1)  # end at Depot 1 for visualization
    tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    tours[f"Robot {k}"] = tour
    costs[f"Robot {k} Total Travel Cost"] = tour_cost

# Output
overall_cost = sum(costs.values())
for k, tour in tours.items():
    print(f"{k} Tour: {tour}")
    print(f"{k} Total Travel Cost: {costs[f'{k} Total Travel Cost']}")
print(f"Overall Total Travel Cost: {overall_cost}")