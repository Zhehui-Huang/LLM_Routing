import math
import pulp

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distances between all pairs of cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

num_cities = len(cities)
num_robots = 2

# Creating a problem variable
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# x[i][j][k]: robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", 
                          ((i, j, k) for i in range(num_cities) 
                                      for j in range(num_cities) 
                                      for k in range(num_robots)), 
                          cat='Binary')

# u[i]: auxiliary variable for preventing subtours (position in the tour)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective: Minimize the maximum distance a robot travels
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Add constraint: every city must be visited exactly once by exactly one robot
for j in range(1, num_cities):
    prob += (pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1)

# Add constraint: flow conservation
for k in range(num_robots):
    for p in range(num_cities):
        prob += (pulp.lpSum(x[p][j][k] for j in range(num_cities)) == 
                 pulp.lpSum(x[i][p][k] for i in range(num_cities)))

# Add constraint: each robot leaves the depot (city 0)
for k in range(num_robots):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1

# Add constraint: each robot returns to the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[i][0][k] for i in range(1, num_cities)) == 1

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += (u[i] - u[j] + num_cities * x[i][j][k] <= num_cities-1)

# Constraint on max distance
for k in range(num_robots):
    prob += pulp.lpSum(calc_distance(i, j) * x[i][j][k] for i in range(num_cities) for j in range(num_cities)) <= max_distance

# Solve the problem
prob.solve()

# Extract the result
for k in range(num_robots):
    tour = [0]
    current_location = 0
    while True:
        next_location = [j for j in range(num_cities) if pulp.value(x[current_location][j][k]) == 1][0]
        if next_location == 0:
            break
        tour.append(next_location)
        current_location = next_location
    tour.append(0)
    tour_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {tour_cost}')

max_cost = max(sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) for k in range(num_robots))
print(f'Maximum Travel Cost: {max_cost}')