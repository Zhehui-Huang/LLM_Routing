import math
import pulp

# Define the city coordinates
coordinates = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define city groups (clusters)
city_groups = {
    0: [0],  # Depot group
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

# Formulation starts
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# Complete set of cities
all_cities = list(coordinates.keys())

# Create decision variables x_ij for all pairs (i, j), where i != j
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j],
                          cat=pulp.LpBinary)

# Objective Function: Minimize the total distance
problem += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Each group must connect exactly once
for group_id, group in city_groups.items():
    if group_id != 0:  # Ignoring depot group for outgoing connection
        problem += pulp.lpSum(x[i, j] for i in group for j in all_cities if i != j) == 1
        problem += pulp.lpSum(x[j, i] for i in group for j in all_cities if i != j) == 1

# Flow conservation constraint
for city in all_cities:
    problem += pulp.lpSum(x[j, city] for j in all_cities if j != city) == pulp.lpSum(x[city, j] for j in all_cities if j != city)

# Solve the problem
problem.solve()

# Check if a feasible solution has been found
if pulp.LpStatus[problem.status] == 'Optimal':
    # Extracting the tour using the solution
    path = []
    current_city = 0
    path.append(current_city)
    visited = set()
    visited.add(current_city)
    tour_cost = 0
    while True:
        next_moves = [(j, x[current_city, j].varValue) for j in all_cities if j != current_city]
        next_city = next(j for j, xij in next_moves if xij > 0.5 and j not in visited)
        if next_city is None:
            break
        path.append(next_city)
        tour_cost += calculate_distance(current_city, next_city)
        visited.add(next_city)
        current_city = next_city
        if current_city == 0:
            break
    path.append(0)  # To return to depot
    
    print(f"Tour: {path}")
    print(f"Total travel cost: {round(tour_cost, 2)}")
else:
    print("No optimal solution found")