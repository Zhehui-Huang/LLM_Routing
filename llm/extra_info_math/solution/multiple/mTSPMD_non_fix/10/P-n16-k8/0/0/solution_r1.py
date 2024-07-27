import pulp
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distances between each pair of nodes
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Create the problem instance
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if robot travels from i to j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Add objective function
problem += pulp.lpSum(x[i, j] * distances[i, j] for i in cities for j in cities if i != j)

# Each city must be entered and left exactly once (except depot)
for j in cities:
    problem += pulp.lpSum(x[i, j] for i in cities if i != j and (i, j) in x) == 1, f"enter_{j}"
    problem += pulp.lpSum(x[j, i] for i in cities if i != j and (j, i) in x) == 1, f"leave_{j}"

# Multiple robots start at depot 0
problem += pulp.lpSum(x[0, j] for j in cities if j != 0) == 8, "robots_start_at_depot_0"

# Solve the problem
problem.solve()

# Determine the paths taken by the robots
paths = {i: [] for i in range(8)}  # Assume robot ids from 0 to 7
for r in range(8):  # For each robot
    cur_location = 0
    paths[r].append(cur_location)
    while True:
        next_loc = [j for j in cities if j != cur_location and pulp.value(x[cur_location, j]) == 1]
        if not next_loc:
            break
        next_loc = next_loc[0]
        paths[r].append(next_loc)
        cur_location = next_loc
        if cur_location == 0:
            break

total_cost = 0
for r, path in paths.items():
    path_cost = sum(distances[path[i], path[i+1]] for i in range(len(path)-1))
    total_cost += path_cost
    print(f"Robot {r} Tour: {path}")
    print(f"Robot {r} Total Travel Cost: {path_cost}")

print(f"Overall Total Travel Cost: {total_cost}")