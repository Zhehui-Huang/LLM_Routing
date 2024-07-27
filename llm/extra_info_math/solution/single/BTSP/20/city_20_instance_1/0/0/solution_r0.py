from pulp import *
import math

# Coordinates of the cities (including the depot city at index 0)
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points in 2D. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of cities (including depot)
n = len(coordinates)

# Distance matrix
distances = {(i, j): euclidean min_value_distance(coordinates[i], coordinates[j]) 
             for i in range(n) for j in range(n) if i != j}

# Integer Program
prob = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", (range(n), range(n)), 0, 1, LpBinary)
u = LpVariable.dicts("u", range(n), 0, n-1, LpInteger)
K = LpVariable("K", lowBound=0, cat='Continuous')  # Maximum distance variable

# Objective
prob += K

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1  # leave i
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1  # enter i

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Maximize the maximum edge in the tour
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i, j] * x[i][j] <= K

# Solve the problem
prob.solve()
tour = []
max_distance = 0
total_cost = 0

# Extract the tour
for from_city in range(n):
    for to_city in range(n):
        if from_city != to_city and x[from_city][to_city].varValue == 1:
            tour.append((from_city, to_city))
            total_cost += distances[from_city, to_city]
            if distances[from_city, to_city] > max_distance:
                max_distance = distances[from_city, to_city]

# Reorder the tour starting from the depot
visited = set()
current_city = 0
final_tour = [0]

while len(final_tour) < n:
    for next_city in tour:
        if next_city[0] == current_city and next_city[1] not in visited:
            current_city = next_city[1]
            visited.add(current_city)
            final_tour.append(current_city)
            break

final_tour.append(0)  # Return to depot
total_cost += distances[current_city, 0]

print("Tour:", final_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)