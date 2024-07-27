import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities including the depot
num_cities = len(coordinates)
num_robots = 2

# Create the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) 
                               for j in range(num_cities) 
                               for k in range(num_robots)), 
                          cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), cat='Continuous')
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective
problem += max_distance

# Constraints
# Each node must be visited exactly once by exactly one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each robot starts and ends at the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1
    
# Flow conservation for each robot
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities)) == pulp.lpSum(x[j, i, k] for i in range(num_cities))

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Maximizing the maximum distance constraint
for k in range(num_robots):
    problem += pulp.lpSum(x[i, j, k] * math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + 
                                                 (coordinates[i][1] - coordinates[j][1])**2) 
                          for i in range(num_cities) 
                          for j in range(num_cities)) <= max_distance

# Solve the problem
if problem.solve() == pulp.LpStatusOptimal:
    for k in range(num_robots):
        tour = []
        for i in range(num_cities):
            for j in range(num_cities):
                if pulp.value(x[i, j, k]) == 1:
                    tour.append((i, j))
        # Extract the order of the tour
        ordered_tour = [0]
        while len(ordered_tour) - 1 < len(tour):
            next_city = tour.pop(0)[1]
            ordered_tour.append(next_city)
            tour = [(i, j) for i, j in tour if i == next_city]
        ordered_tour.append(0)  # return to depot

        tour_cost = sum(math.sqrt((coordinates[ordered_tour[i]][0] - coordinates[ordered_tour[i+1]][0])**2 + 
                                  (coordinates[ordered_tour[i]][1] - coordinates[ordered_tour[i+1]][1])**2) 
                        for i in range(len(ordered_tour) - 1))
        print(f"Robot {k} Tour: {ordered_tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    max_cost = pulp.value(max_distance)
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("No optimal solution found.")