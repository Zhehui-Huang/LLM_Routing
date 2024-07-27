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
    return math.sqrt((cities[id1][0] - cities[id2][0]) ** 2 + (cities[id1][1] - cities[id2][1]) ** 2)

# Total number of cities
num_cities = 19

# Number of robots
num_robots = 2

# Initializing the optimization model
model = pulp.LpProblem("VRP_with_Multiple_Depots", pulp.LpMinimize)

# Variables: x_ij = 1 if robot travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Constraints and Objective function
cost = 0

# Start from each depot, ending is free
for k in range(num_robots):
    model += pulp.lpSum(x[k, j] for j in range(num_cities) if k != j) == 1  # exactly one edge out of each depot

for j in range(num_cities):
    model += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1  # each city is visited exactly once
    model += pulp.lpSum(x[j, i] for i in range(num_cities) if i != j) == 1  # each city is left exactly once

# Minimize the total cost
cost = pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)
model += cost

# Solve the model
status = model.solve()

# Output the results if an optimal solution was found
if status == pulp.LpStatusOptimal:
    print("Solution Found\n")
    total_travel_cost = 0
    for k in range(num_robots):
        tour = [k]
        next_city = k
        while True:
            next_cities = [j for j in range(num_cities) if pulp.value(x[next_city, j]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
        travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel_cost}")
        total_travel_cost += travel_cost

    print(f"\nOverall Total Travel Cost: {total_travel.