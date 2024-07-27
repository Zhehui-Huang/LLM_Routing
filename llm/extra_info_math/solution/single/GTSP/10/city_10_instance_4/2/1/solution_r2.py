import pulp
import math

# City coordinates
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Grouping of cities
groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define the problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in coordinates for j in coordinates if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in coordinates for j in coordinates if i != j)

# Constraints
# One exiting and one entering connection per group (excluding depot)
for group in groups.values():
    problem += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in coordinates if j not in group) == 1

# Flow conservation at each city (including depot)
for city in coordinates:
    problem += pulp.lpSum(x[(i, city)] for i in coordinates if i != city and (i, city) in x) == \
               pulp.lpSum(x[(city, j)] for j in coordinates if j != city and (city, j) in x)

# Solve the problem
status = problem.solve()

# Extracting the tour
if status == pulp.LpStatusOptimal:
    tour = []
    total_travel_cost = 0
    current_city = 0
    tour.append(current_city)

    while True:
        next_city = next(j for j in coordinates if j != current_city and pulp.value(x[(current_city, j)]) == 1)
        total_travel_cost += euclidean_distance(current_city, next_city)
        current_city = next_city
        if current_city == 0:
            break
        tour.append(current_city)

    tour.append(0)  # return to the depot
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
else:
    print("No optimal solution found.")