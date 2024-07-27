import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of robots
num_robots = 8

# Initialize the problem
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities if i != j for k in range(num_robots)), 
                          cat='Binary')

u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), 
                          lowBound=0, cat='Continuous')

# Objective - Minimize the maximum travel cost among all robots
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
# Each city is visited exactly once by one robot
for j in cities:
    if j != 0:
        prob += pulp.lpSum(x[i, j, k] for i in cities if i != j for k in range(num_robots)) == 1

# Flow conservation constraints
for k in range(num_robots):
    for p in cities:
        prob += pulp.lpSum(x[p, j, k] for j in cities if p != j) == pulp.lpSum(x[j, p, k] for j in cities if p != j)

# Each robot leaves and enters the depot exactly once
for k in range(num_robots):
    prob += pulp.lpSum(x[0, j, k] for j in cities if j != 0) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in cities if j != 0) == 1

# Subtour elimination constraints
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            for k in range(num_robots):
                prob += u[i] - u[j] + len(cities) * x[i, j, k] <= len(cities) - 1

# Each robot's total travel cost does not exceed the maximum travel cost
for k in range(num_robots):
    prob += pulp.lpSum(x[i, j, k] * euclidean_distance(i, j) for i in cities for j in cities if i != j) <= max_distance

# Solve the problem
prob.solve()

# Output the results
for k in range(num_robots):
    tour = [0]
    current_city = 0
    while True:
        next_city = None
        for j in cities:
            if j != current_city and pulp.value(x[current_city, j, k]) == 1:
                tour.append(j)
                current_city = j
                break
        if current_city == 0:
            break
    print(f"Robot {k} Tour: {tour}")
    travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {travel_cost}")
print(f"Maximum Travel Cost: {pulp.value(max_distance)}")