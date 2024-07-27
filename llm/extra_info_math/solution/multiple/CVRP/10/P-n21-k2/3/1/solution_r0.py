import pulp
import math

# Function to calculate Euclidean distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Problem parameters
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160
num_robots = 2
num_cities = len(coordinates)

# Create the problem
problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

# Decision variables: x[r][i][j], 1 if robot r travels from city i to city j
x = [[[pulp.LpVariable(f"x_{r}_{i}_{j}", cat='Binary') for j in range(num_cities)] for i in range(num_cities)] for r in range(num_robots)]

# Objective function: Minimize total travel cost
problem += pulp.lpSum(distance(coordinates[i], coordinates[j]) * x[r][i][j] 
                      for r in range(num_robots) 
                      for i in range(num_cities) 
                      for j in range(num_cities) if i != j)

# Constraints
# Each city is visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[r][i][j] for r in range(num_robots) for i in range(num_cities) if i != j) == 1

# Depot constraints
for r in range(num_robots):
    problem += pulp.lpSum(x[r][0][j] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[r][j][0] for j in range(1, num_cities)) == 1

# Flow conservation
for r in range(num_robots):
    for j in range(1, num_cities):
        inflow = pulp.lpSum(x[r][i][j] for i in range(num_cities) if i != j)
        outflow = pulp.lpSum(x[r][j][i] for i in range(num_cities) if i != j)
        problem += inflow - outflow == 0

# Capacity constraints
for r in range(num_robots):
    problem += pulp.lpSum(demands[j] * x[r][i][j] for i in range(num_cities) for j in range(1, num_cities) if i != j) <= capacity

# Solve the problem
status = problem.solve()

# Prepare and display output results
if status == pulp.LpStatusOptimal:
    print("Optimal solution found:\n")
    total_cost = 0
    for r in range(num_robots):
        print(f"Robot {r} Tour: ", end="")
        tour = [0]
        next_city = None
        for i in range(num_cities-1):  # max num_cities-1 more visits
            next_city = next(j for j in range(num_cities) if pulp.value(x[r][tour[-1]][j]) == 1)
            tour.append(next_city)
            if next_city == 0:
                break
        print(tour)
        tour_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost
    print(f"\nOverall Total Travel Cost: {total_cost:.2f}")
else:
    print("No optimal solution found. Status:", pulp.LpStatus[status])