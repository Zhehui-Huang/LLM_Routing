import math
from mip import Model, xsum, minimize, BINARY

# Provided city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
n = len(coordinates)  # number of nodes (cities)
m = 8  # number of robots

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(1, n)]

# Objective function to minimize the maximum distance traveled by any robot
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot must leave and return to the depot exactly once
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        model.add_constr(xsum(x[p][j][k] for j in range(n) if j != p) -
                         xsum(x[i][p][k] for i in range(n) if i != p) == 0)

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i-1] - u[j-1] + n * x[i][j][k] <= n - 1
                
# Each robot's distance constraint should not exceed the maximum distance
for k in range(m):
    model += xsum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Optimize the model
status = model.optimize(max_seconds=600)

# Output results
if status == model.OPTIMAL or status == model.FEASIBLE:
    print(f"Optimal or feasible solution found:\n")
    max_cost = max_distance.x
    for k in range(m):
        tour = [0]
        current_city = 0
        while True:
            next_city = next(j for j in range(n) if j != current_city and x[current_city][j][k].x >= 0.99)
            if next_city == 0:
                tour.append(next_city)
                break
            tour.append(next_city)
            current_city = next_city
        tour_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("No feasible solution found due to constraints or solver limitations.")