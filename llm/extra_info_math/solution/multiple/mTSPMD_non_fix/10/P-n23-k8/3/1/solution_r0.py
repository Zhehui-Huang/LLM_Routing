import numpy as np
import pulp

# Constants
num_cities = 23
depot_cities = [0, 1, 2, 3, 4, 5, 6, 7]
non_depot_cities = list(set(range(num_cities)) - set(depot_cities))
num_robots = 8

# Coordinates of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating a travel cost matrix
cost_matrix = {
    (i, j): distance(coordinates[i], coordinates[j]) 
    for i in range(num_cities) for j in range(num_cities) if i != j
}

# Initialize the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective function: Minimize total cost
prob += pulp.lpSum([cost_matrix[i, j] * x[i, j] for i, j in cost_matrix.keys()]), "Total_Travel_Cost"

# Constraints
for j in non_depot_cities:
    prob += pulp.lpSum([x[i, j] for i in range(num_cities) if (i, j) in cost_matrix]) == 1, f"One_out_{j}"
    prob += pulp.lpSum([x[j, i] for i in range(num_cities) if (j, i) in cost_matrix]) == 1, f"One_in_{j}"

for d in depot_cities:
    prob += pulp.lpSum([x[d, j] for j in range(num_cities) if (d, j) in cost_matrix]) == 1, f"Depot_out_{d}"
    prob += pulp.lpSum([x[j, d] for j in range(num_cities) if (j, d) in cost_matrix]) == 1, f"Depot_in_{d}"

# Solve the problem
prob.solve()

# Output the solution
for r in range(num_robots):
    print(f"Robot {r} Tour:")
    current_city = 0  # All robots start at city 0
    tour = [current_city]
    tour_cost = 0
    while True:
        next_cities = [j for j in range(num_cities) if (current_city, j) in x and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        tour_cost += cost_matrix[current_city, next_city]
        current_city = next_city
        if current_city in depot_cities:
            break
    print(tour)
    print(f"Total Travel Cost: {tour_cost}")