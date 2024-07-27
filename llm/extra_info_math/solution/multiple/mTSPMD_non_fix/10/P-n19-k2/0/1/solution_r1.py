import pulp
import math

# Coordinates of the cities including depots
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

# Calculate Euclidean distance between two cities
def euclidean_distance(id1, id2):
    return math.sqrt((cities[id1][0] - cities[id2][0])**2 + (cities[id1][1] - cities[id2][1])**2)

# Number of cities
num_cities = 19

# Number of robots
num_robots = 2

# Initialize the optimization model
model = pulp.LpProblem("VRP_with_Multiple_Depots", pulp.LpMinimize)

# Variables: x_ij = 1 if robot travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective Function
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each city is connected exactly once
for j in range(2, num_cities):
    model += pulp.lpSum(x[i][j] for i in range(num_cities) if i != j) == 1

# Each city is reached exactly once
for i in range(2, num_cities):
    model += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1

# Start from each depot, ending is free
for i in range(num_robots):
    model += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1

# Solve the model
model.solve()

# Report the tours and costs
total_cost = 0
tours = []
for k in range(num_robots):
    current_city = k
    tour = [current_city]
    while True:
        next_cities = [j for j in range(num_cities) if pulp.value(x[current_city][j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
    tours.append(tour)
    cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")