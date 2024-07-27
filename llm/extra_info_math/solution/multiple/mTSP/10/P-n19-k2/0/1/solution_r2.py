import pulp
from math import sqrt

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2 

# Distance function
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(num_robots) 
                                for i in range(len(coordinates)) 
                                for j in range(len(coordinates))], 
                          cat='Binary')
order = pulp.LpVariable.dicts("order", [(i, k) for k in range(num_robots) for i in range(1, len(coordinates))], 
                              lowBound=0, upBound=len(coordinates)-2, cat='Continuous')

# Objective
prob += pulp.lpSum([distance(coordinates[i], coordinates[j]) * x[(i, j, k)]
                    for k in range(num_robots)
                    for i in range(len(coordinates))
                    for j in range(len(coordinates)) if i != j])

# Constraints
for j in range(1, len(coordinates)):
    prob += pulp.lpSum([x[(i, j, k)] for i in range(len(coordinates)) for k in range(num_robots)]) == 1

for k in range(num_robots):
    prob += pulp.lpSum([x[(0, j, k)] for j in range(1, len(coordinates))]) == 1
    prob += pulp.lpSum([x[(i, 0, k)] for i in range(1, len(coordinates))]) == 1

for k in range(num_robots):
    for j in range(1, len(coordinates)):
        prob += pulp.lpSum([x[(i, j, k)] for i in range(len(coordinates))]) == pulp.lpSum([x[(j, i, k)] for i in range(len(coordinates))])

# Subtour prevention constraints
num_cities = len(coordinates)
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                prob += order[(i, k)] - order[(j, k)] + num_cities*x[(i, j, k)] <= num_cities-1

# Solve the problem
prob.solve()

# Extract tours
for k in range(num_robots):
    tour = [0]
    while True:
        next_cities = [j for j in range(1, num_cities) if pulp.value(x[(tour[-1], j, k)]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        if next_city == 0:
            tour.append(next_city)
            break
        else:
            tour.append(next_city)
    print(f"Robot {k} Tour: {tour}")

# Calculate travel costs
for k in range(num_robots):
    tour_cost = sum([distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1)])
    print(f"Robot {k} Total Travel Cost: {tour_input}")
    
total_cost = sum(distance(coordinates[i], coordinates[j]) * pulp.value(x[(i, j, k)]) 
                 for k in range(num_robots)
                 for i in range(num_cities)
                 for j in range(num_cities) if i != j)
print(f"Overall Total Travel Cost: {total_cost}")