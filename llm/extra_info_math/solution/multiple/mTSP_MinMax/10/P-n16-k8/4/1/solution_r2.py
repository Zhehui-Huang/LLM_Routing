from mip import Model, xsum, minimize, BINARY, INTEGER
import math

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

n = len(coordinates)  # Number of cities including depot
m = 8  # Number of robots

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Create a new model
model = Model()

# Decision variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=1) for i in range(1, n)]

# Objective: minimize the maximum distance traveled by any vehicle
max_distance = model.add_var()
model.objective = minimize(max_name)

# Each city is visited exactly once by one robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Robots must leave from and return to depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Tour formation and subtour prevention
for k in range(m):
    for i in range(1, n):
        model += xsum(x[i][j][k] for j in range(n)) == xsum(x[j][i][k] for j in range(n))

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i-1] - u[j-1] + n*xsum(x[i][j][k] for k in range(m)) <= n-2
            
# Enforce the maximum distance constraint
for k in range(m):
    model += xsum(distance(i, j) * x[i][j][k] for i in range(n) for j in range(n)) <= max_distance

# Solve the model
model.optimize()

# Output the results
if model.num_solutions:
    for k in range(m):
        tour = [0]
        for _ in range(1, n):
            i = tour[-1]
            for j in range(n):
                if x[i][j][k].x >= 0.99:
                    tour.append(j)
                    break
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_distance}")
    print(f"Maximum Travel Cost: {max_distance.x}")
else:
    print("No solution found")