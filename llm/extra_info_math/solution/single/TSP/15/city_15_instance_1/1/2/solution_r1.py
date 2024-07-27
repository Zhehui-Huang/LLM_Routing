import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, value
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 44),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize the problem
problem = LpProblem("TSP", LpMinimize)

# Variable x_ij: 1 if the path goes from city i to city j
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
problem += lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "Total Travel Distance"

# Constraints
for k in cities:
    problem += lpSum(x[(i, k)] for i in cities if i != k) == 1  # Exactly one entry to city k
    problem += lpSum(x[(k, j)] for j in cities if k != j) == 1  # Exactly one departure from city k

# Solving the problem
problem.solve()

# Determine the tour based on x values
def find_tour():
    edges = [(i, j) for i in cities for j in cities if i != j and value(x[(i, j)]) == 1]
    tour = [0]  # Starting from the depot city
    while len(edges) > 0:
        for e in edges:
            if e[0] == tour[-1]:
                tour.append(e[1])
                edges.remove(e)
                break
    return tour

tour = find_tour()
tour.append(0)  # Returning to the start point (depot city)

# Calculate the total cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))