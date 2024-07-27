import pulp
import math

def calculate_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Define coordinates of each city including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, upBound=num_cities-1, cat='Continuous')

# Distance matrix
distance = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Objective function: minimize the maximum distance traveled by any robot
maximum_distance_traveled = pulp.LpVariable("max_distance_traveled")
problem += maximum_tour_length

for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                problem += maximum_distance_traveled >= distance[i][j] * x[i, j, k]

# Constraints
# 1. Each city is visited exactly once by exactly one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# 2. Each robot leaves each city only once
for k in range(num_robots):
    for i in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for j in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for j in range(num_cities) if i != j)

# 3. & 4. Each robot leaves and returns to the depot exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# 5. Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
status = problem.solve()

# Prepare the output
if status == pulp.LpStatusOptimal:
    max_travel_cost = pulp.value(problem.objective)
    print(f"Maximum Travel Cost: {max_travel_cost}")
    
    for k in range(num_robots):
        print(f"Robot {k} Tour: [0", end='')
        current_location = 0
        tour_cost = 0
        while True:
            next_location = None
            for j in range(num_cities):
                if pulp.value(x[current_location, j, k]) == 1:
                    next_location = j
                    tour_cost += distance[current_location][j]
                    print(f", {next_location}", end='')
                    current_location = j
                    break
            if current_location == 0:
                break
        print("]")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
else:
    print("Failed to find an optimal solution.")