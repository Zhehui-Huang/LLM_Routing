import pulp
import math

# Coordinates of all cities including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# City groups
groups = [
    [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
]

# Function to calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j], cat='Binary')

# Objective function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Each group must have exactly one outgoing and one incoming selection
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Continuity of the tour (i.e., flow conservation)
for j in range(len(coordinates)):
    problem += pulp.lpSum(x[(i, j)] for i in range(len(coordinates)) if i != j) == pulp.lpSum(x[(j, k)] for k in range(len(coordinates)) if k != j)

# Solve the problem
problem.solve()

# Extract the results
tour_solution = []
visited_cities = set([0])
current_city = 0

while True:
    next_city = None
    for j in range(len(coordinates)):
        if j != current_city and pulp.value(x[(current_city, j)]) == 1:
            next_city = j
            break
    if next_city is None or next_city == 0:
        tour_solution.append(0)
        break
    tour_solution.append(next_city)
    visited_cities.add(next_city)
    current_city = next_city

# Calculate the total travel cost
total_travel_cost = sum(euclidean_distance(tour_solution[i], tour_solution[i+1]) for i in range(len(tour_solution) - 1))

# Display the results
print("Tour:", tour_solution)
print("Total travel cost:", total_travel_cost)