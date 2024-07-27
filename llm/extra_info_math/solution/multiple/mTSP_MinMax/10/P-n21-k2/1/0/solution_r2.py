import pulp
import math

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(coordinates)
num_robots = 2

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Define the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# Objective Function: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city visited exactly once by exactly one robot, excluding the depot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each robot departs the depot exactly once and returns exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j][0][k] for j in range(1, num_cities)) == 1

# Flow conservation for each city and robot
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i][j][k] for i in range(num_cities)) == pulp.lpSum(x[j][i][k] for i in range(num_cities))

# Subtour prevention
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i][j][k] <= num_cities - 2

# Defining the distances and linking to max distance
for k in range(num_robots):
    problem += pulp.lpSum(x[i][j][k] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities)) <= max_distance

# Solve the problem
problem.solve()

# Output results
for k in range(num_robots):
    tour = [0]
    current_city = 0
    while True:
        next_city = next(j for j in range(num_cities) if pulp.value(x[current_city][j][k]) == 1)
        if next_city == 0:
            break
        tour.append(next_city)
        current_obj = next_city
    tour.append(0)  # Return to depot
    tour_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_distance}")

print("Maximum Travel Cost:", pulp.value(max_distance))