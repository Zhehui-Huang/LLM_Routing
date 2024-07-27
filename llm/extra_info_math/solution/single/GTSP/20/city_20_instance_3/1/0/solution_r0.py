import pulp
import math

# Coordinates of cities including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Groups of cities where the robot has to visit one city from each group
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Define the problem
prob = pulp.LpProblem("Minimal_Tour_Cost", pulp.LpMinimize)

# Decision variables
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[i, j] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective Function: Minimize the total travel cost
prob += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), "Total_travel_cost"

# Constraints for each group
for group in groups:
    # Exactly one outgoing edge to a node outside the group
    prob += sum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1
    # Exactly one incoming edge from a node outside the group
    prob += sum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Constraints that ensure starting and ending at the depot
prob += sum(x[0, j] for j in range(1, len(coordinates))) == 1
prob += sum(x[j, 0] for j in range(1, len(coordinates))) == 1

# Flow conservation constraints
for i in range(1, len(coordinates)):
    prob += (sum(x[j, i] for j in range(len(coordinates)) if j != i) ==
             sum(x[i, k] for k in range(len(coordinates)) if k != i)), f"Flow_conservation_vertex_{i}"

# Solve the problem
prob.solve()

# Fetch the results
tour = []
visited = [0]
current = 0
while len(visited) < len(groups) + 1:
    for j in range(len(coordinates)):
        if pulp.value(x[current, j]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break
tour.append(0)  # Returning to the depot

# Calculate total travel cost
total_cost = sum(euclidean_textdistance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)