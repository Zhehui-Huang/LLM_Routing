import math
import pulp

# Define the coordinates of each city including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Compute the Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {(i, j): distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j}

# Initialize the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] is 1 if we travel from city i to city j
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Objective: Minimize total travel distance
prob += pulp.lpSum([distances[(i, j)] * x[(i, j)] for (i, j) in distances])

# Constraints
# Each city must be arrived at from exactly one other city
for j in cities:
    prob += pulp.lpSum([x[(i, j)] for i in cities if i != j]) == 1, f"arrive_to_{j}"

# Each city must be departed to exactly one other city
for i in cities:
    prob += pulp.lpSum([x[(i, j)] for j in cities if i != j]) == 1, f"depart_from_{i}"

# Solve the problem
status = prob.solve()

# Check if the problem was solved
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    path = []
    current_city = 0
    visited = set([current_city])
    tour_cost = 0
    for _ in range(len(cities)):
        for next_city in cities:
            if pulp.value(x[(current_city, next_node)]) == 1:
                path.append(next_city)
                tour_cost += distances[(current_city, next_city)]
                current_city = next_city
                visited.add(current_city)
                break
    path.append(0)
    tour_cost += distances[(current_city, 0)]

    print(f"Tour: {path}")
    print(f"Total travel cost: {tour_cost:.2f}")
else:
    print("Optimal solution not found.")