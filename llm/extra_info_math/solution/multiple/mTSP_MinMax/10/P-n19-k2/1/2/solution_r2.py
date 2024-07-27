import pulp
import math

# Given data
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_cities = len(coordinates)
num_robots = 2

def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Problem setup
problem = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Variables for whether robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Continous variable for the maximum travel cost
max_travel_cost = pulp.LpVariable("max_travel_cost")
problem += max_travel_cost, "Maximize the travelled distance across all robots"

# Constraints
# Ensure each non-depot city is visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i,j,k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1, f"One visit to city {j}"

# Ensure each robot leaves the depot exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1, f"Start from depot Robot {k}"

# Ensure each robot returns to the depot exactly once
for k in range(num_robots):
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1, f"Return to depot Robot {k}"

# Make sure every robot that arrives at a city also leaves
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) == \
                   pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j), f"Leave city {j} robot {k}"

# Cost constraints and link with max_travel_cost
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                problem += x[i, j, k] * calc_distance(coordinates[i], coordinates[j]) <= max_travel_cost

# Solve the model
problem.solve()

# Collect and print the solution
if problem.status == pulp.LpStatusOptimal:
    print("Optimal Solution Found:")
    for k in range(num_robots):
        tour = [0]
        while True:
            found_next = False
            for j in range(num_cities):
                if pulp.value(x[tour[-1], j, k]) == 1:
                    tour.append(j)
                    found_next = True
                    break
            if not found_next or tour[-1] == 0:
                break
        travel_cost = sum(calc_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel_cost}")
    print(f"Maximum Travel Cost: {pulp.value(max_travel_cost)}")
else:
    print("No Optimal Solution Found.")