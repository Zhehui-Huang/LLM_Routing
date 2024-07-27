import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City locations
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

# Define city groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Initialization of the linear programming problem
model = pulp.LpProblem("Minimize_travel_cost", pulp.LpMinimize)

# Variables: x[i][j] is 1 if we travel from city i to city j, else 0.
x = pulp.LpVariable.dicts("travel", 
                          ((i, j) for i in range(20) for j in range(20) if i != j), 
                          cat='Binary')

# Objective: minimize the total travel distance
model += pulp.lpSum(x[(i, j)] * euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for i in range(20) for j in range(20) if i != j)

# Each city in group must have exactly one entering and one leaving connection
for group in city_groups:
    model += sum(x[(i, j)] for i in group for j in range(20) if j not in group) == 1
    model += sum(x[(j, i)] for i in group for j in range(20) if j not in group) == 1

# Adding flow conservation constraints at each non-depot city
for city in range(1, 20):
    model += sum(x[(j, city)] for j in range(20) if j != city) == sum(x[(city, j)] for j in range(20) if j != city)

# Solve the problem
model.solve()

# From the solved variables, construct the tour starting from depot (0)
current_city = 0
tour = [current_city]
for _ in range(len(city_groups)):
    next_city = [j for j in range(20) if pulp.value(x[(current_map, j)]) == 1][0]
    tour.append(next_city)
    current_city = next_city

tour.append(0)  # returning to depot
total_travel_cost = sum(euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)