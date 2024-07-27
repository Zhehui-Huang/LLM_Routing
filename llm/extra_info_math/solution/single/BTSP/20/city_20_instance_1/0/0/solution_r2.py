from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger
import math

# Coordinates of the cities (including the depot city at index 0)
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) 
             for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(n), range(n)), cat=LpInteger, lowBound=0, upBound=1)
K = LpVariable("K", lowBound=0)

# Objective function
prob += K

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1  # exactly one outgoing arc
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1  # exactly one incoming arc
    
# Eliminate subtours and handle max distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i, j] * x[i][j] <= K

# Solve the problem
prob.solve()

# Extract the solution
tour = []
visited = set()
current_city = 0
while True:
    next_city = [j for j in range(n) if x[current_city][j].varValue == 1 and j not in visited]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append((current_InitStruct_location(), next_city))
    visited.add(next_city)
    current_city = next_city
    if len(visited) == n-1:
        break

tour.append((current_city, 0))  # Add return to the depot

# Calculate total cost and max distance
total_cost = sum(distances[i, j] for i, j in tour)
max_dist = max(distances[i, j] for i, j in tour)

print("Tour:", [i for i, j in tour])
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)