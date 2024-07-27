import pulp as pl
import math

# City coordinates
city_coordinates = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Groups of cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Distance function using Euclidean distance calculation
def calc_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0])**2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1])**2)

# Initialize PuLP model
model = pl.LpProblem("Robot_Tour_Problem", pl.LpMinimize)

# Variables: x_ij where i, j are cities, and indicate if the robot travels from city i to city j
x = pl.LpVariable.dicts("x",
                        [(i, j) for i in city_coordinates for j in city_coordinates if i != j],
                        cat=pl.LpBinary)

# Objective Function: Minimize the total travel cost
model += pl.lpSum(x[i, j] * calc_distance(i, j) for i in city_coordinates for j in city_coordinates if i != j)

# Constraints
# Ensure exactly one outgoing connection from each group to non-group cities
for group_id, group_cities in groups.items():
    model += pl.lpSum(x[i, j] for i in group_cities for j in city_coordinates if j not in group_cities) == 1

# Ensure exactly one incoming connection to each group from non-group cities
for group_id, group_cities in groups.items():
    model += pl.lpSum(x[j, i] for i in group_cities for j in city_coordinates if j not in group_cities) == 1

# Flow conservation at non-depot cities
for city in city_coordinates:
    if city != 0:
        model += pl.lpSum(x[city, j] for j in city_coordinates if j != city) - \
                 pl.lpSum(x[i, city] for i in city_coordinates if i != city) == 0

# Solve the problem
model.solve()

# Check if a valid solution exists
if pl.LpStatus[model.status] == 'Optimal':
    # Extract the tour order
    path_edges = [(i, j) for i in city_coordinates for j in city_coordinates if i != j and pl.value(x[i, j]) == 1]
    tour = [0]
    current_city = 0

    while len(path_edges) > 0:
        for i, j in path_edges:
            if i == current_city:
                tour.append(j)
                current_city = j
                path_edges.remove((i, j))
                break

    # Calculate the total travel cost
    total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")