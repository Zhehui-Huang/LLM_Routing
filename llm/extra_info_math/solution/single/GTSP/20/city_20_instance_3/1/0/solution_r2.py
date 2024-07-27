import math
import pulp

# Coordinates of all cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Groups of cities
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a linear programming problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables: x[i, j] = 1 if travel from city i to city j, 0 otherwise
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)
     for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective function: Minimize total travel distance
prob += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i, j in x), "Total_Travel_Cost"

# Constraints for group inclusion
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if i != j and j not in group) == 1  # Outgoing connection
    prob += pulp.lpSum(x[j, i] for i in group for j in range(len(coordinates)) if i != j and j not in group) == 1  # Incoming connection

# Ensure all connections form a continuous path and return to start
for i in range(len(coordinates)):
    if i == 0:
        # From and to the depot
        prob += pulp.lpSum(x[i, j] for j in range(len(coordinates)) if i != j) == 1
        prob += pulp.lpSum(x[j, i] for j in range(len(coordinates)) if i != j) == 1
    else:
        # Flow conservation constraints
        prob += (pulp.lpSum(x[i, j] for j in range(len(coordinates)) if i != j) ==
                 pulp.lpSum(x[j, i] for j in range(len(coordinates)) if i != j))

# Solve the problem using the solver
prob.solve()

# Extract tour and calculate total travel cost
city = 0
tour = [city]
next_city = None
while next_city != 0:
    for j in range(len(coordinates)):
        if j != city and pulp.value(x[(city, j)]) == 1:
            tour.append(j)
            city = j
            break

total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)