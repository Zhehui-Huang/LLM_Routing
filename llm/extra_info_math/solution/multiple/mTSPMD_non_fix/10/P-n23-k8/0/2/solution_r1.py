import math
from mip import Model, xsum, BINARY, INTEGER

# Coordinates of the cities (depot inclusive)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of salesmen (robots)
m = 8

# Number of cities including Depots
n = len(coordinates)

# Depot city for all salesmen (all start from depot 0)
depot = 0

# Calculate Euclidean distance matrix
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Distance matrix
c = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Model
model = Model()

# Variables
x = [[model.add_var('B') for j in range(n)] for i in range(n)]  # Travel between cities
u = [model.add_var(var_type=INTEGER, lb=1, ub=n) for i in range(n)]  # Position in tour for sub-tour prevention

# Objective: minimize the total distance traveled
model.objective = xsum(c[i][j]*x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Depart from the depot exactly m times
model += xsum(x[depot][j] for j in range(n) if j != depot) == m

# Arrive at the depot exactly m times
model += xsum(x[j][depot] for j in range(n) if j != depot) == m

# Each city must be entered and left exactly once
for i in range(1, n):
    model += xsum(x[i][j] for j in range(n) if j != i) == 1
    model += xsum(x[j][i] for j in range(n) if j != i) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the model
status = model.optimize()

# If a valid solution has been found, construct the tours for output
if status == OptimizationStatus.OPTIMAL:
    # Finding the tours
    tours = [[] for i in range(m)]
    for i in range(m):
        current_city = depot
        while True:
            next_city = [j for j in range(n) if j != current_city and x[current_city][j].x >= 0.99][0]
            tours[i].append(current_city)
            if next_city == depot:
                tours[i].append(depot)
                break
            current_city = next_city

    # Display the tours and calculate the tour costs
    overall_cost = 0
    for i in range(m):
        tour = tours[i]
        tour_cost = sum(c[tour[j]][tour[j+1]] for j in range(len(tour)-1))
        overall_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {overall_cost}")

elif model.status == OptimizationStatus.INFEASIBLE:
    print("No feasible solution found.")