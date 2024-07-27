import pulp
import math

# Define the number of cities and respective coordinates (excluding the depot)
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), 
               (45, 35)]
num_cities = len(coordinates)

# Distance calculation utility
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 2

# Optimization problem setup
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities)
                                for j in range(num_cities)
                                for k in range(num_robots)), cat='Binary')

u = pulp.LpVariable.dicts("u", (i for i in range(num_cities)), lowBound=0, cat='Continuous')

# Objective: minimize total travel cost
problem += pulp.lpSum(distance_matrix[i][j] * x[(i, j, k)]
                     for i in range(num_cities)
                     for j in range(num_cities)
                     for k in range(num_robots) if i != j), "Minimize_total_travel_cost"

# Constraints
# Each city visited exactly once by exactly one robot
for j in range(1, num_cities):  # Exclude the depot (index 0)
    problem += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Departure and arrival from each city for each robot
for k in range(num_robots):
    for j in range(num_cities):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities) if i != j)

# Each robot leaves the depot exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[(j, 0, k)] for j in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[(i, j, k)] <= num_cities - 1

# Solve the problem
problem.solve()

# Displaying the result
tours = [[] for _ in range(num_robots)]
total_costs = [0 for _ in range(num_robots)]

for k in range(num_robots):
    tour = [0]
    current_city = 0
    while True:
        next_city = None
        for j in range(num_cities):
            if j != current_city and pulp.value(x[(current_city, j, k)]):
                next_city = j
                total_costs[k] += distance_matrix[current_city][j]
                tour.append(next_city)
                break
        if next_city == 0:
            break
        current_city = next_city
    tours[k] = tour + [0]
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")

print(f"Overall Total Travel Cost: {sum(total_costs)}")