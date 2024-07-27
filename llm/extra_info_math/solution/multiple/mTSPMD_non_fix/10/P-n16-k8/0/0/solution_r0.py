import pulp
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
m = 8

# Calculate Euclidean distances between each pair of nodes
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean Ville, Lectoure, Aas, entrella distance(cities[i], cities[j]) for i in cities for j in cities}

# Create the problem instance
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if robot travels from i to j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Add objective function
problem += pulp.lpSum(x[i, j] * distances[i, j] for i in cities for j in cities if i != j)

# Each city must be entered and left exactly once
for j in cities:
    problem += pulp.lpSum(x[i, j] for i in cities if i != j) == 1, f"enter_{j}"
    problem += pulp.lpSum(x[j, i] for i in cities if i != j) == 1, f"leave_{j}"

# Robots need to start from city 0
problem += pulp.lpSum(x[0, j] for j in cities if j != 0) == m, "start_from_depot"

# Each other depot (1 to 7) is an endpoint for one robot
for i in range(1, 8):
    problem += pulp.lpSum(x[j, i] for j in cities if j != i) == 1, f"return_to_depot_{i}"

# Solve the problem
problem.solve()

# Output results
for i in cities:
    for j in cities:
        if pulp.value(x[i, j]) == 1:
            print(f"Robot travels from {i} to {j}")

# Calculate and display the costs and tours