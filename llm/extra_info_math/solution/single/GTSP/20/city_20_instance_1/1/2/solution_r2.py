import pulp
import math

# Define city coordinates
city_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Define groups of cities
groups = [[5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]]

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)

distances = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Linear programming model
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j), 
                          cat=pulp.LpBinary)

# Add objective function
model += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in range(len(city_metrics)) for j in range(len(city_coords)) if i != j)

# Constraints: Ensure each city (except depot) is entered and exited exactly once
for i in range(1, len(city_coords)):
    model += pulp.lpSum(x[(i, j)] for j in range(len(city_coords)) if i != j) == 1  # leave i
    model += pulp.lpSum(x[(j, i)] for j in range(len(city_coords)) if i != j) == 1  # enter i

# Additional constraints: Each group must be visited exactly once
for group in groups:
    model += sum(x[(i, j)] for i in group for j in range(len(city_coords)) if j not in group) == 1
    model += sum(x[(j, i)] for i in group for j in range(len(city_coords)) if j not in group) == 1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Capture the results
if status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[status]}")
    journey = []
    for i in range(len(city_coords)):
        for j in range(len(city_coords)):
            if i != j and pulp.value(x[(i, j)]) == 1:
                journey.append((i, j))

    # The output should piece together a tour from the journey variable
    tour = [0]
    next_city = tour[0]
    while True:
        next_step = [step[1] for step in journey if step[0] == next_city]
        if not next_step:
            break
        next_city = next_step[0]
        tour.append(next_city)
        if next_city == 0:
            break

    total_travel_cost = sum(distances[step] for step in journey)

    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("The problem does not have an optimal solution.")