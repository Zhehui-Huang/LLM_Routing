from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities (clusters)
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate a dictionary with all pairs of cities and their distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_depo_distance(cities[i], cities[j])

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Variables x_ij, where i, j are cities indices and (i != j)
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)

# Variables u for subtour elimination
u = LpVariable.dicts("u", (i for i in range(1, len(groups) + 1)), lowBound=0, cat='Continuous')

# Objective function
problem += lpSum(distances[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
# Each group must have exactly one outgoing and one incoming to/from any city outside the group
for g in groups:
    problem += lpSum(x[(i, j)] for i in g for j in cities if j not in g) == 1, f"One outgoing for group {g}"
    problem += lpSum(x[(j, i)] for i in g for j in cities if j not in g) == 1, f"One incoming for group {g}"

# Flow conservation constraints for each city
for i in cities:
    problem += lpSum(x[(j, i)] for j in cities if i != j) - lpSum(x[(i, j)] for j in cities if i != j) == 0, f"Flow conservation at city {i}"

# Subtour elimination constraints (Miller-Tucker-Zemlin)
k = len(groups) + 1
for p in range(1, len(groups)):
    for q in range(1, len(groups)):
        if p != q:
            for i in groups[p]:
                for j in groups[q]:
                    problem += u[p] - u[q] + k * x[(i, j)] + (k-2) * x[(j, i)] <= k - 1

# Solve the problem
problem.solve()

# Prepare the output
tour = [0]
current_city = 0
while True:
    next_city = [j for j in cities if j != current_city and x[(current_city, j)].varValue == 1]
    if next_city:
        next_city = next_city[0]
        tour.append(next_city)
        current_city = next_city
    if current_city == 0:
        break

total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")