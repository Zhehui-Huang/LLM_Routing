import pulp as pl
import math

# Coordinates of the cities
city_coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
               (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
               (56, 58), (72, 43), (6, 99)]

# Groups of cities
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Euclidean distance calculation
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + 
                     (city_coords[i][1] - city_coords[j][1]) ** 2)

# Problem definition
prob = pl.LpProblem("TSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts('x', ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j),
                        cat='Binary')

# Objective
prob += pl.lpSum(x[(i, j)] * euclidean_dist(i, j) for i in range(len(city_coords)) 
                 for j in range(len(city_coords)) if i != j), "Total Travel Cost"

# Constraints
# Connectivity within groups
for group in groups.values():
    prob += pl.lpSum(x[(i, j)] for i in group for j in range(len(city_coords)) if i != j) == 1
    prob += pl.lpSum(x[(j, i)] for i in group for j in range(len(city_coords)) if i != j) == 1

# Visit each city once and preserve flow
for i in range(len(city_coords)):
    # Incoming flow
    prob += pl.lpSum(x[(j, i)] for j in range(len(city_coords)) if i != j) == pl.lpSum(x[(i, j)] for j in range(len(city_coords)) if i != j)

# Solve the problem
prob.solve()

# Output results
tour = []
visited = [0]  # starting point at depot (city 0)
while len(visited) < len(groups) + 1:
    for j in range(len(city_coords)):
        if x[(visited[-1], j)].varValue == 1:
            tour.append((visited[-1], j))
            visited.append(j)
            break

# Include return to the depot
tour.append((visited[-1], 0))
total_cost = sum(euclidean_dist(i, j) for i, j in tour)

print("Tour:", [i for i, j in tour] + [0])
print("Total travel cost:", total_cost)