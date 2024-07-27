import math
import pulp

# Define the city coordinates
coordinates = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define city groups (clusters)
city_groups = {
    0: [0],  # Depot (additional group for the depot as origin and destination)
    1: [7, 9],
    2: [1, 3],
    3: [4, 6],
    4: [8],
    5: [5],
    6: [2]
}

# Function for Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Creating LP problem
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in all_cities for j in all_cities if i != j}

# Objective function
problem += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Ensure every group connects out exactly once
for group_id, group in city_groups.items():
    if group_id != 0:  # Exclude depot since it's handled as returning point
        problem += pulp.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
        problem += pulp.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation at each node
for city in all_cities:
    if city != 0:
        problem += pulp.lpSum(x[j, city] for j in all_cities if j != city) == 1
        problem += pulp.lpSum(x[city, j] for j in all_cities if j != city) == 1

# Solving the problem
status = problem.solve()

# Extract the tour
if status == pulp.LpStatusOptimal:
    current_city = 0
    path = [current_city]
    next_city = None
    while True:
        next_city = next(j for j in all_cities if pulp.value(x[current_city, j]) == 1 and j != current_city)
        if next_city == 0:
            path.append(next_city)
            break
        path.append(next_city)
        current_city = next_city
    tour_cost = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))

    # Output results
    print(f"Tour: {path}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("No optimal solution found.")