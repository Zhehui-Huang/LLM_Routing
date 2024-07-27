import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Define the problem
prob = pulp.LpProblem("Minimal_Tour_Cost", pulp.LpMinimize)

# Creating decision variables
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective Function
prob += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints
for group in groups:
    # Exactly one outgoing edge to a city not in the group
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1
    # Exactly one incoming edge from a city not in the group
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(lenlices)) if i not in group) == 1

# Additional constraints for flow conservation in cities
for i in range(1, len(coordinates)):
    prob += pulp.lpSum(x[(j, i)] for j in range(len(coordinates)) if j != i) == pulp.lpSum(x[(i, k)] for k in range(len(coordinates)) if k != i), f"Flow_{i}"

# Ensure the tour starts and ends at the depot
prob += pulp.lpSum(x[(0, j)] for j in range(1, len(coordinates))) == 1
prob += pulp.lpSum(x[(j, 0)] for j in range(1, len(coordinates))) == 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(len(coordinates)) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculating the total cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")