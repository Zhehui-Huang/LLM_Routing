import pulp
import math

# Helper function to compute Euclidean Distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Coordinates of each city including the depot
cities_coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 49)
}

# Define groups of cities
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Our problem variables
problem = pulp.LpProblem("Minimize_Path_Cost", pulp.LpMinimize)
selected_cities = {g: pulp.LpVariable.dicts(f'group_{g}', group, cat='Binary') for g, group in city_groups.items()}
x = pulp.LpVariable.dicts("path", ((i, j) for i in cities_coordinates for j in cities_coordinates if i != j), cat='Binary')

# Objective to minimize travel cost
problem += pulp.lpSum(x[(i, j)] * calc_distance(cities_coordinates[i], cities_coordinates[j]) for i in cities_coordinates for j in cities_coordinates if i != j)

# Constraints to ensure each group is represented exactly once
for g, group in city_groups.items():
    # Exactly one city from each group is chosen
    problem += pulp.lpSum(selected_cities[g][city] for city in group) == 1
    # Link the city choice with the path decision variables
    for city in group:
        problem += pulp.lpSum(x[(city, j)] for j in cities_coordinates if j != city) == selected_cities[g][city]

# Make sure every city is entered and left once
for k in cities_coordinates:
    problem += pulp.lpSum(x[(i, k)] for i in cities_coordinates if i != k) == pulp.lpSum(x[(k, j)] for j in cities_coordinates if k != j)

# Solve the optimization problem
problem.solve()

# Extract Solution
if pulp.LpStatus[problem.status] == "Optimal":
    tour = []
    total_cost = 0
    for i in cities_coordinates:
        for j in cities_coordinates:
            if i != j and pulp.value(x[(i, j)]) == 1:
                tour.append((i, j))
                total_cost += calc_distance(cities_coordinates[i], cities_coordinates[j])

    # Organize the tour to start and end at the depot
    organized_tour = [0] 
    while len(organized_tour) < len(tour) + 1:
        last = organized_tour[-1]
        for (start, end) in tour:
            if start == last:
                organized_tour.append(end)
                break

    print("Tour:", organized_tour)
    print("Total travel cost:", total_cost)
else:
    print("Could not find an optimal solution.")