import pulp
import math

# Define coordinates and depots.
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]
num_nodes = len(coordinates)
depot = 0  # Single depot starting point for all robots

# Initialize problem
model = pulp.LpProblem("TSP_with_Robots", pulp.LpMinimize)

# Variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') if i != j else None for j in range(num_nodes)] for i in range(num_nodes)]

# Objective function - minimizing the total travel distance
model += pulp.lpSum(x[i][j] * math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
                     for i in range(num_nodes) for j in range(num_nodes) if i != j)

# Constraints
# Each city (excluding the depot) must be visited exactly once
for j in range(1, num_nodes):  # Start from 1 to skip the depot
    model += pulp.lpSum(x[i][j] for i in range(num_nodes) if i != j) == 1
    model += pulp.lpSum(x[j][i] for i in range(num_nodes) if i != j) == 1

# Departing from the depot
model += pulp.lpSum(x[depot][j] for j in range(num_nodes) if j != depot) == 8  # 8 robots starting tours

# Arrive back at the depot is not necessary (mentioned it does not need to return)
# Ensure no sub-tour formation
u = [pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(num_nodes)]
for i in range(1, num_nodes):
    for j in range(1, num_nodes):
        if i != j:
            model += u[i] - u[j] + num_nodes * x[i][j] <= num_nodes - 1

# Solve the problem
model.solve()

# Output results
routes = {}
for i in range(num_nodes):
    for j in range(num_nodes):
        if x[i][j].varValue == 1:
            if i == depot:
                if depot in routes:
                    routes[depot].append(j)
                else:
                    routes[depot] = [j]
            else:
                routes[i] = j

# Determine the tours from routing dictionary
def find_tour(start, routes_map):
    tour = [start]
    next_city = routes_map[start]
    while next_city != start:
        tour.append(next_city)
        next_city = routes_map.get(next_city, start)
    return tour

tours = [find_tour(d, routes) for d in routes[depot]]

# Calculate costs
total_cost = 0
for tour in tours:
    tour_cost = sum(math.sqrt((coordinates[tour[i]][0] - coordinates[tour[i+1]][0])**2 + 
                              (coordinates[tour[i]][1] - coordinates[tour[i+1]][1])**2)
                    for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Tour: {tour}, Cost: {tour_cost}")

print(f"Total travel cost for all robots: {total_cost}")