import pulp
import math

# Coordinates of the cities including the depot (city 0)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_cities = len(cities)
robots = 8

# Function to calculate the Euclidean distance between two cities
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem instance
problem = pulp.LpProblem("RobotVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(robots)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), 0, num_cities-2, cat='Continuous')

# Objective: Minimize the maximum travel cost
problem += pulp.lpSum(x[i, j, k] * calc_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(robots))

# Constraints
# Every city is visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(robots) if i != j) == 1

# Flow conservation
for k in range(robots):
    for p in range(num_cities):
        problem += pulp.lpSum(x[i, p, k] for i in range(num_cities) if i != p) - pulp.lpSum(x[p, j, k] for j in range(num_cities) if j != p) == 0

# Each robot departs from the depot
for k in range(robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1

# Eliminate subtours
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the problem using CBC solver
problem.solve()

# Processing results
for k in range(robots):
    tour = [0]
    potential_next_cities = [j for j in range(1, num_cities) if pulp.value(x[0, j, k]) > 0.5]
    while potential_next_cities:
        current_city = potential_next_cities.pop(0)
        tour.append(current_city)
        next_cities = [j for j in range(num_cities) if pulp.value(x[current_city, j, k]) > 0.5 and j not in tour]
        if next_cities:
            potential_next_cities = [next_cities[0]]

    tour.append(0)  # return to depot
    travel_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {travel_cost}")

max_travel_cost = max(sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) for tour in tours.values())
print("Maximum Travel Cost:", max_travel_cost)