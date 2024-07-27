import math
import pulp

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_cities = len(cities)
num_robots = 2

# Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distances = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Setup the optimization problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for i in range(num_cities)
                                     for j in range(num_cities) if i != j
                                     for k in range(num_robots)),
                          cat='Binary')
u = pulp.LpVariable.dicts("u",
                          (i for i in range(1, num_cities)),
                          lowBound=0, cat='Continuous')

# Add objective function to minimize the maximum distance traveled by any robot
max_distance_var = pulp.LpVariable("MaxDistance")
problem += max_distance_var

# Constraints
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) - \
                   pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j) == 0

# Subtour Elimination
for (i, j) in product(range(1, num_cities), repeat=2):
    if i != j:
        for k in range(num_robots):
            problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

for k in range(num_robots):
    problem += pulp.lpSum(distances[i][j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance_var

# Solve the problem
problem.solve()

# Extract tours for each robot and calculate cost
tours = []
costs = []
for k in range(num_robots):
    tour = [0]
    current_city = 0
    total_cost = 0
    while True:
        next_city = None
        for j in range(num_cities):
            if pulp.value(x[current_city, j, k]) == 1:
                next_city = j
                break
        if next_city == 0:  # If returning to the depot
            tour.append(next_city)
            total_cost += distances[current_city][next_city]
            break
        tour.append(next_city)
        total_cost += distances[current_city][next_city]
        current_city = next_city
    tours.append(tour)
    costs.append(total_cost)

# Output results
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Maximum Travel Cost: {max(costs)}")