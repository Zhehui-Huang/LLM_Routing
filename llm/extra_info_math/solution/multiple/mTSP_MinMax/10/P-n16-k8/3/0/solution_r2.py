import pulp as pl
import math

# City coordinates including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_robots = 8
num_cities = len(cities)

# Distance calculation
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): calculate_types Sum(x[i][j][k]*distances[i][j] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Adding the constraints
# Each non-depot city is visited exactly once by any robot
for j in range(1, num_cities):
    problem += pl.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Every robot departs and arrives at the depot
for k in range(num_robots):
    problem += pl.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1
    problem += pl.lpSum(x[i][0][k] for i in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities-1) * x[i][j][k] <= num_cities-2

# Solve the problem
problem.solve()

# Extract the solution
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pl.value(x[i][j][k]) == 1:
                tours[k].append((i, j))

# Convert each tour list to a proper tour order
tour_paths = {}
for k in tours:
    tour = [0]
    next_city = tour[-1]
    while len(tour) < num_cities:
        for i, j in tours[k]:
            if i == next_city:
                tour.append(j)
                next_city = j
                break
    tour.append(0)  # return to the depot
    tour_paths[k] = tour

# Output results
max_cost = 0
for k in tour_paths:
    path = tour_paths[k]
    cost = sum(distances[path[i], path[i+1]] for i in range(len(path)-1))
    max_cost = max(max_cost, cost)
    print(f"Robot {k} Tour: {path}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print("Maximum Travel Cost:", max_cost)