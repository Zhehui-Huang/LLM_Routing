import pulp
import math

# Coordinates of cities and depots
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Function to calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Total number of cities and depots
n = len(coords)

# Distance matrix using Euclidean distance
distance_matrix = [[euclidean_dist(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# List of depots
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Problem setup
problem = pulp.LpProblem("MDMTSP", pulp.LpMinimize)

# Decision variables: x[i, j, k] = 1 if robot departs from depot k visits city i, then goes to city j
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for i in range(n) for j in range(n) for k in depots if i != j),
                          cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum(x[i, j, k] * distance_matrix[i][j] for i in range(n) for j in range(n) for k in depots if i != j)

# Constraints
# Only one exit and one entry per city except for depots
for j in set(range(n)) - set(depots):
    problem += sum(x[i, j, k] for i in range(n) for k in depots if i != j) == 1
    problem += sum(x[j, i, k] for i in range(n) for k in depots if i != j) == 1

# Each depot must have one robot leaving and coming back
for k in depots:
    problem += sum(x[k, j, k] for j in range(n) if j != k) == 1
    problem += sum(x[j, k, k] for j in range(n) if j != k) == 1

# Solving the problem
status = problem.solve()

# Output results
total_cost = 0
for k in depots:
    tour = [k]
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_cities or next_cities[0] == k:
            tour.append(k)
            break
        tour.append(next_cities[0])
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print("Overall Total Travel Cost:", total_cost)