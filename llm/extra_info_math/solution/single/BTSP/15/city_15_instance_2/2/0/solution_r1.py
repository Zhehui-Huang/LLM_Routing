# Necessary Libraries
import pulp
import math

# City coordinates
coordinates = [
    (54, 87),  # Depot City 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

n = len(coordinates)

# Function to calculate distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
d = pulp.LpVariable("max_distance", cat='Continuous')

# Objective
problem += d

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Enforce max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += d >= distance(i, j) * x[i, j]

# Solving the problem
status = problem.solve()

# Making sure the problem is solved
if status == pulp.LpStatusOptimal:
    tour = [0]
    current = 0
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[current,j]) == 1 and j != current]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current = next_city
        if current == 0:
            break

    # Calculate max distance and total travel cost
    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("An optimal solution could not be found.")