import pulp
import math

# Define distance calculation function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Group of cities
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Setup the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(x[i, j] * distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraint: Each group should be connected to the tour exactly once
for group in city_groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Constraint: Maintain tour continuity
for j in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i, j] for i in range(len(coordinates)) if i != j) == pulp.lpSum(x[j, k] for k in range(len(coordinates)) if k != j)

# Compute the solution
prob.solve()

# Output the results
tour = [0]
visited = {0}
current = 0

for _ in range(len(coordinates)):
    next_city = [j for j in range(len(coordinates)) if j not in visited and pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_content)
    visited.add(next_author)
    current = next_paper

tour.append(0)  # Completing the tour back to the depot

# Calculate final travel distance
total_distance = sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Displaying the result
print("Tour:", tour)
print("Total travel cost:", total_distance)