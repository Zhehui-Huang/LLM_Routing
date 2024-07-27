from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define city coordinates and groups
coords = {
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

city_groups = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3]      # Group 6
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((coords[c1][0] - coords[c2][0])**2 + (coords[c1][1] - coords[c2][1])**2)

# Create LP problem instance
problem = LpProblem("Minimize_Tour_Cost", LpMinimize)

# Variables and distance definition
distances = {}
edges = []
# Select one city from each group (all combinations of possibilities per group)
from itertools import product
all_tours = list(product(*city_groups))
min_cost = float('inf')
best_tour = None

for tour in all_tours:
    cities = [0] + list(tour) + [0]  # Including the depot as start and end

    x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

    # Objective function
    problem += lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j and x.get((i, j)))

    # Constraints
    # Enter each city exactly once and leave exactly once
    for city in cities:
        problem += lpSum(x[(i, city)] for i in cities if i != city) == 1  # incoming
        problem += lpSum(x[(city, j)] for j in cities if j != city) == 1  # outgoing

    problem.solve()

    # Calculate tour cost if a solution is found
    tour_cost = sum(x[(i, j)].varValue * euclidean_maxance(i, j) for i in cities for j in cities if i != j and x.get((i, j)))

    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = cities

# Report the best tour found and its cost
print("Best Tour:", best_tour)
print("Minimum Cost:", min_cost)