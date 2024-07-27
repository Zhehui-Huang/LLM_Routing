import pulp
import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Number of groups
k = len(groups)

# Calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("TSP_Group", pulp.LpMinimize)

# Decision variables: x_ij where i, j are cities
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for i in cities for j in cities if i != j}

# Objective function: minimize the total travel cost
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints for ensuring exactly one node from each group is connected
for group in groups.values():
    problem += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation at nodes
for i in cities:
    problem += pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if j != i)

# Solve the problem
problem.solve()

# Extract the tour and calculate the total cost
tour = []
current = 0
visited = {0}
total_cost = 0

while len(visited) < k + 1:
    for j in cities:
        if j != current and x[current, j].varValue == 1:
            tour.append(j)
            total_cost += euclidean_distance(current, j)
            current = j
            visited.add(j)
            break

# Append the return to the depot
tour.append(0)
total_cost += euclidean_distance(tour[-2], 0)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")