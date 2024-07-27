import pulp
from math import sqrt

# Define the data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
num_robots = 2
num_cities = len(coordinates)
depot = 0

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat=pulp.LpContinuous)

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each robot leaves the depot and returns to the depot exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[depot][j][k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[i][depot][k] for i in range(1, num_cities)) == 1

# Flow conservation
for k in range(num_robots):
    for p in range(1, num_cities):
        problem += pulp.lpSum(x[i][p][k] for i in range(num_cities) if i != p) - pulp.lpSum(x[p][j][k] for j in range(num_cities) if j != p) == 0

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i][j][k] <= num_cities - 2

# Solve the problem
status = problem.solve()

# Extract Solution
if status == pulp.LpStatusOptimal:
    for k in range(num_robots):
        tour = [depot]
        current_location = depot
        while True:
            next_location = None
            for j in range(num_cities):
                if j != current_location and pulp.value(x[current_location][j][k]) == 1:
                    next_location = j
                    tour.append(next_location)
                    current_location = next_location
                    break
            if next_location == depot:
                break
        tour.append(depot)
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    overall_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for k in range(num_robots) for i in range(len(tour[k]) - 1))
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Failed to find an optimal solution.")