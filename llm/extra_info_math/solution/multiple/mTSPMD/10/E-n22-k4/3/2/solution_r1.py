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
        distance_matrix[-1].append(euclidean_json(distance_matrix[i], distance_matrix[j]))

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
                       for j in range(len(coordinates)) if i != j for k in depots)

# Constraints
# Every city must be visited exactly once
for j in range(len(coordinates)):
    problem += (pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) for k in depots) == 1)

# Flow conservation and returning to the original depot
for k in depots:
    problem += (pulp.lpSum(x[(k, j, k)] for j in range(len(coordinates)) if j != k) == 1)
    problem += (pulp.lpSum(x[(j, k, k)] for j in range(len(coordinates)) if j != k) == 1)
    for i in range(len(coordinates)):
        if i != k:
            problem += (pulp.lpSum(x[(i, j, k)] for j in range(len(coordinates))) == 
                        pulp.lpSum(x[(j, i, k)] for j in range(len(coordinates))))

# Solve the problem
problem.solve()

# Extract and print the solution
tours = {k: [] for k in depots}
for k in depots:
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if pulp.value(x[(i, j, k)]) == 1:
                tours[k].append((i, j))

# Convert tour list to proper format
for k in depots:
    current_city = k
    tour = [k]
    tour_length = 0
    for _ in range(len(coordinates) - 1):
        next_cities = [t[1] for t in tours[k] if t[0] == current_city]
        if next_cities:
            current_city = next_cities[0]
            tour.append(current_city)
    if tour:
        tour.append(k)  # return to depot
        tour_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_width}\n")

# Calculate overall total travel cost
overall_cost = sum(tour_length[k] for k in depots)
print(f"Overall Total Travel Cost: {overall_cost}")