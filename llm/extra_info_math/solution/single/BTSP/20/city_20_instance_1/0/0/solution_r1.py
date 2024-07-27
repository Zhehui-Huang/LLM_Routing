from pulp import *
import math

# Coordinates of the cities including the depot city 0
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(coordinates)
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = LpVariable.dicts("u", indexs=range(n), lowBound=0, cat='Continuous')

# Objective function - Minimize the maximum distance between consecutive cities
prob += lpSum(distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter

# Eliminate subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
          prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
prob.solve()

# Output results
tour = []
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        i, j = map(int, v.name[2:-1].split(','))
        tour.append((i, j))

# Ensure tour starts and ends at the depot
final_tour, current_city = [0], 0
while len(final_tour) < n:
    for nxt in tour:
        if nxt[0] == current_city:
            current_city = nxt[1]
            final_tour.append(current_city)
            break
final_tour.append(0) # Return to depot

# Calculate total travel cost and max_distance
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")