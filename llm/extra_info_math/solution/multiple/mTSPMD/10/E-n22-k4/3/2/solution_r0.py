import pulp
import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Robot depots
depots = [0, 1, 2, 3]

# Number of robots
num_robots = 4

# Compute the Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = []
for i in range(len(coordinates)):
    distance_matrix.append([])
    for j in range(len(coordinates)):
        distance_matrix[-1].append(euclidean_distance(coordinates[i], coordinates[j]))

# Initialize the problem
problem = pulp.LpProblem("VRP_with_multiple_depots", pulp.LpMinimize)

# Variables: x[i][j][k] == 1 if robot k travels from city i to city j
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        for k in depots:
            x[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(len(coordinates)) 
                       for j in range(len(coordinates)) if i != j for k in depots), "Total_Distance"

# Each city is visited exactly once by any robot
for j in range(4, len(coordinates)):
    problem += (pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) for k in depots) == 1), f"Visit_{j}"

# Departing from and returning to the depot conditions
for k in depots:
    problem += (pulp.lpSum(x[(k, j, k)] for j in range(len(coordinates)) if j != k) == 1), f"Leave_depot_{k}"
    problem += (pulp.lpSum(x[(j, k, k)] for j in range(len(coordinates)) if j != k) == 1), f"Return_depot_{k}"

# Flow conservation for non-depot cities
for i in range(4, len(coordinates)):
    for k in depots:
        problem += (pulp.lpSum(x[(i, j, k)] for j in range(len(coordinates))) == 
                    pulp.lpSum(x[(j, i, k)] for j in range(len(coordinates)))), f"Flow_conservation_{i}_{k}"

# Solve the problem
problem.solve()

# Extract results
if pulp.LpStatus[problem.status] == 'Optimal':
    # For each robot
    overall_cost = 0
    for k in depots:
        tour = [k]
        next_location = k
        while True:
            next_location = [j for j in range(len(coordinates)) if pulp.value(x[(next_location, j, k)]) == 1][0]
            if next_page in tour:
                break
            tour.append(next_location)
        tour.append(k)  # Return to depot
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        overall_cost += tour_cost
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}\n")
    print(f"Overall Total Travel, Cost: {overall_cost}")
else:
    print("No optimal solution obtained.")