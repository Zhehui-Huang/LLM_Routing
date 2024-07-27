import pulp
import math

# Define city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define depots and robots
depots = list(range(8))
num_robots = 8
assert len(depots) == num_robots

# Create distance matrix
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = {}
for i in range(len(city_coordinates)):
    for j in range(len(city_coordinates)):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Create the problem variable to contain the problem data
prob = pulp.LpProblem("Multiple_Depot_Vehicle_Routing_Problem", pulp.LpMinimize)

# Create decision variables and LP variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(16) for j in range(16) if i != j for k in range(8)), 
                          cat='Binary', lowBound=0, upBound=1)

# Objective: Minimize the total cost of the tours
prob += pulp.lpSum(distance_matrix[i, j] * x[i, j, k] for i in range(16) for j in range(16) if i != j for k in range(8))

# Constraints:

# Each depot only starts one tour
for k in depots:
    prob += pulp.lpSum(x[k, j, k] for j in range(16) if j != k) == 1

# Each city is visited exactly once
for j in range(8, 16):
    prob += pulp.lpSum(x[i, j, k] for i in range(16) for k in range(8) if i != j) == 1

# Tour continuity
for k in depots:
    for i in range(16):
        if i != k:
            prob += (pulp.lpSum(x[i, j, k] for j in range(16) if j != i) - 
                     pulp.lpSum(x[j, i, k] for j in range(16) if j != i)) == 0

# Every tour must return to the depot
for k in depots:
    prob += pulp.lpSum(x[j, k, k] for j in range(16) if j != k) == 1

# Solve the problem
prob.solve()

# Extracting the solution
robot_tours = {k: [k] for k in depots}
for k in depots:
    current_city = k
    while True:
        for j in range(16):
            if j != current_city and pulp.value(x[current_city, j, k]) == 1:
                robot_tours[k].append(j)
                current_city = j
                break
        if current_city == k:
            break

# Calculate costs and display the results
total_costs = 0
for k in depots:
    tour_cost = sum(distance_matrix[robot_tours[k][i], robot_tours[k][i+1]] for i in range(len(robot_tours[k])-1))
    total_costs += tour_cost
    print(f"Robot {k} Tour: {robot_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_costs}")