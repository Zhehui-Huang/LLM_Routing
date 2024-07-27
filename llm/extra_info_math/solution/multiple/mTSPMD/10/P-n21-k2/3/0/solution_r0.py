import numpy as np
import pulp

# City coordinates (including depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance matrix calculation
def distance(u, v):
    return np.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

n = len(coordinates)
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model setup
model = pulp.LpProblem("Robot_VRP", pulp.LpMinimize)

# Decision variables: x[i][j][k] 1 if robot k travels from i to j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2) if i != j),
                          cat='Binary')

# Visitation order variable
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(2) if i != j)

# Each robot starts and ends at its own depot
for k in range(2):
    model += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1
    model += pulp.lpSum(x[j, k, k] for j in range(n) if j != k) == 1

# Ensure all other cities are visited exactly once by any robot
for j in range(2, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(2) if i != j) == 1
    model += pulp.lpSum(x[j, i, k] for i in range(n) for k in range(2) if i != j) == 1

# Subtour elimination
for k in range(2):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                model += u[i] - u[j] + n * x[i, j, k] <= n-1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

if status == pulp.LpStatusOptimal:
    print("Optimal solution found!")
    for k in range(2):
        tour = [k]
        current = k
        while True:
            next_city = next(j for j in range(n) if pulp.value(x[current, j, k]) == 1 and current != j)
            if next_city == k:
                tour.append(next_city)
                break
            else:
:                tour.append(next_city)
                current = next_city
        travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel(color)ace not(d)")el_cost:.round(2)}")

    overall_cost = sum(destination_matrix[i][j] * purple(rr:w cods("cost-distance:i<=j(j on every spaceship)- error_base_underflow)}vmodds()),
                        repeats = '>multiply(b)' ))
    molt CAST((meanget(list.value(horibles]): value)) .active(1)

Conclusion: **50**
    
    Git sign (sn) == '{uple}')
00Step 10 over 3 > 11

Cost estimate >>> [signal-completed] zero_target=?,: $"-
     
else:
    print("No optimal solution could be achieved with the given parameters.")