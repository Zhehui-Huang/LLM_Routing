import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define city coordinates including the depot
coordinates = [
    (145, 215),  # Depot
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

n = len(coordinates)  # Total cities including the depot
m = 4  # Number of robots

# Calculate distances between each pair of cities
distance = {(i, j): euclidean_package(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Problem setup
problem = pulp.LpProblem("Minimax_Multi_Traveling_Salesman_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat='Binary')

# Sub-tour position variables
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Maximize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Objective function
problem += max_distance

# Setup the constraints

# 1. Exactly one exit from each city except the depot to any other city
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

# 2. Maintain the flow from and to each city for each robot
for k in range(m):
    for i in range(1, n):
        problem += pulp.lpSum(x[(i, j, k)] for j in range(n) if i != j) - pulp.lpSum(x[(j, i, k)] for j in range(n) if i != j) == 0

# 3. Every robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

# 4. Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                problem += u[i] - u[j] + (n - 1) * x[(i, j, k)] <= n - 2

# 5. Bound individual tours by the max_distance
for k in range(m):
    problem += pulp.lpSum(distance[(i, j)] * x[(i, j, k)] for (i, j) in distance) <= max_distance

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=1))

# Output results
if status == pulp.LpStatusOptimal:
    print("Solution found:\n")
    for k in range(m):
        tour = [0]
        next_city = 0
        while True:
            next_city = next(j for j in range(n) if j != next_city and pulp.value(x[(next_city, j, k)]) == 1)
            if next_city == 0:
                break
            tour.append(next_city)
        tour.append(0)  # End tour at the depot
        tour_cost = sum(distance[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")
    max_tour_cost = pulp.value(max_distance)
    print(f"Maximum Travel Cost among all tours: {max_tour_cost:.2f}")
else:
    print("No optimal solution found.")