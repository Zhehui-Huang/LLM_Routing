import pulp
import math

# City coordinates indexed from 0 (depod) to 21 (last city)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Total number of cities including the depot
num_cities = len(coordinates)

# Distance function
def distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Parameters
num_robots = 4

# Optimization problem setup
problem = pulp.LpProblem("Multiple Robot TSP", pulp.LpMinimize)

# Variables: x[i][j][k] is 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)),
                          cat='Binary',
                          lowBound=0,
                          upBound=1)

# Node order for the subtour elimination constraint
u = pulp.LpVariable.dicts("u", range(num_cities), lowBound=0, cat='Continuous')

# Objective function: minimize the sum of all distances traveled by all robots
problem += pulp.lpSum(distance(i, j) * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots))

# Constraints
# Each city is visited exactly once by exactly one robot (excludes the starting city depot 0)
for j in range(1, num_cities):
    problem += sum(x[(i, j, k)] for i in range(num_cities) if i != j for k in range(num_robots)) == 1

# Each robot returns to the starting city
for k in range(num_robots):
    problem += sum(x[(j, 0, k)] for j in range(num_cities) if j != 0) == 1

# Every robot starts from the starting city
for k in range(num_robots):
    problem += sum(x[(0, j, k)] for j in range(num_cities) if j != 0) == 1

# Flow conservation constraints
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += sum(x[(i, j, k)] for i in range(num_cities) if i != j) - sum(x[(j, i, k)] for i in range(num_cities) if i != j) == 0

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities) * x[(i, j, k)] <= num_cities - 1

# Solving the problem
problem_status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Collect the result tours
total_distance = 0
for k in range(num_robots):
    tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[(i, j, k)]) == 1:
                tour.append((i, j))
    print(f"Robot {k} Tour:")
    itinerary = [0]
    while tour:
        for i, (s, e) in enumerate(tour):
            if itinerary[-1] == s:
                itinerary.append(e)
                tour.pop(i)
                break
    print(itinerary)
    tour_distance = sum(distance(itinerary[i], itinerary[i+1]) for i in range(len(itinerary) - 1))
    print(f"Distance for Robot {k}: {tour_distance}")
    total_distance += tour

print(f"Total Distance: {total_distance}")