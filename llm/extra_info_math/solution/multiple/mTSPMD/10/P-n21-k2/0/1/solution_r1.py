import pulp
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Distance matrix
num_cities = len(cities_coords)
distance_matrix = [[calculate_distance(cities_coords[i], cities_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

depots = [0, 1]
robots = len(depots)

# Optimization problem
prob = pulp.LpProblem("VRP_Multiple_Depots", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in depots], 0, 1, pulp.LpBinary)

# Objective
prob += pulp.lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) for k in depots)

# Constraints
# Visit each non-depot city exactly once
for j in range(num_cities):
    if j not in depots:
        prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) for k in depots) == 1

# Departure and return for each robot
for k in depots:
    prob += pulp.lpSum(x[(k, j, k)] for j in range(num_cities) if j != k) == 1
    prob += pulp.lpSum(x[(j, k, k)] for j in range(num_cities) if j != k) == 1

# Maintain flow within tours
for k in depots:
    for j in range(1, num_cities):
        prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities)) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities))

# Solve the problem
if prob.solve() == pulp.LpStatusOptimal:
    print("Status:", pulp.LpStatus[prob.status])
    
    total_cost = 0
    for k in depots:
        tour = [k]
        next_city = k
        while True:
            for j in range(num_cities):
                if pulp.value(x[(next_city, j, k)]) == 1:
                    next_city = j
                    tour.append(next_city)
                    break
            if next_city == k:
                break
        
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour}")


    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("The problem did not solve successfully. Status:", pulp.LpStatus[prob.status])