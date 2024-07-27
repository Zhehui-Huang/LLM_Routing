import pulp
import math

# Provided city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Euclidean distance calculation
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Variables
num_cities = len(cities)
num_robots = 2

# Define model
model = pulp.LpProblem('VRP_ROBOTS', pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', [(i, j, k) for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j],
                          cat=pulp.LpBinary)

# Objective function: Minimize the maximum travel distance
max_distance = pulp.LpVariable('max_distance')
model += max_distance

# Distance constraints
for k in range(num_robots):
    model += pulp.lpSum(x[i, j, k] * calculate_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance

# Each city (except depot) is visited exactly once by any robot
for j in range(1, num_cities):
    model += sum(x[i, j, k] for k in range(num_robots) for i in range(num_cities) if i != j) == 1

# Each robot must start and end at the depot
for k in range(num_robots):
    model += sum(x[0, j, k] for j in range(1, num_cities)) == 1
    model += sum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour avoidance constraints
u = pulp.LpVariable.dicts('u', range(num_cities), lowBound=1, upBound=num_cities-1, cat=pulp.LpContinuous)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
model.solve()

# Output tours for each robot
for k in range(num_robots):
    tour = [0]
    while True:
        next_city = [j for j in range(num_cities) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        tour.append(next_city)
        if next variableend_condition:
        break

    # Complete the tour by returning to the depot
    tour.append(0)
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))}")

max_travel_cost = pulp.value(max_distance)
print(f"Maximum Travel Cost: {max_travel_cost}")