from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus
import math

# Define coordinates of all cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]
num_cities = len(coordinates)
all_cities = list(range(num_cities))

# Distance calculation function (Euclidean)
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Generate distance matrix
distances = {(i, j): calculate_distance(i, j) for i in all_cities for j in all_cities if i != j}

# Problem formulation
problem = LpProblem("Minimize_TSP_Distance", LpMinimize)

# Decision variables
x = {(i, j, k): LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for i in all_cities for j in all_cities for k in depots if i != j}

# Objective: Minimize the total distance traveled by all robots
problem += lpSum(distances[i, j] * x[i, j, k] for k in depots for i in all_cities for j in all_cities if i != j and (i, j) in distances)

# Constraints
# Each city must be visited exactly once, excluding depots
for j in all_cities:
    if j not in depots:
        problem += lpSum(x[i, j, k] for i in all_cities for k in depots if i != j and (i, j) in distances) == 1

# Departure and arrival constraint for each robot at its depot
for k in depots:
    problem += lpSum(x[k, j, k] for j in all_cities if j != k and (k, j) in distances) == 1
    problem += lpSum(x[j, k, k] for j in all_cities if j != k and (j, k) in distances) == 1

# Flow conservation constraint
for k in depots:
    for j in all_cities:
        if j not in depots:
            problem += (lpSum(x[i, j, k] for i in all_cities if i != j and (i, j) in distances) == 
                        lpSum(x[j, i, k] for i in all_cities if i != j and (j, i) in distances))

# Solve the problem
problem.solve()

# Output the results
overall_total_cost = 0
for k in depots:
    print(f"\nRobot {k} Tour starting and ending at Depot {k}:")
    tour = []
    current_city = k
    while True:
        next_city = next((j for j in all_cities if j != current_city and x[current_city, j, k].varValue == 1), None)
        if next_city is None or next_city == k:
            if next_city == k:
                tour.append(k)
            break
        tour.append(current_city)
        current_city = next_city
    print(" -> ".join(map(str, tour)))
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Tour Cost for Robot {k}: {tour_cost}")
    overall_total_cost += tour_cost

print(f"\nOverall Total Travel Cost: {overall_total_cost}")