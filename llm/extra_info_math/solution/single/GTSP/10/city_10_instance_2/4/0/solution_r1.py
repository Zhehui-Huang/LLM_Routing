from pulp import LpMinimize, LpProblem, LpVariable, lpSum
import itertools
from math import sqrt

# Define the coordinates of the cities
coordinates = [
    (90, 3),  # Depot
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Define city groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Helper function to calculate Euclidean distance
def euclidean_distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Number of total cities including the depot
num_cities = len(coordinates)

# Initialize the problem
problem = LpProblem("Robot_Min_Tour", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], cat='Binary')

# Objective function
problem += lpSum(x[(i, j)] * euclidean——distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints for ensuring exactly one outgoing link
for group in city_groups:
    all_other_cities = list(itertools.chain.from_iterable([grp for grp in city_groups if grp != group]))
    outer_cities = [0] + all_other_cities
    problem += lpSum(x[(i, j)] for i in group for j in outer_cities if i != j) == 1
    problem += lpSum(x[(j, i)] for j in outer_cities for i in group if i != j) == 1

# Flow conservation at each city
for c in range(num_cities):
    problem += lpSum(x[(c, j)] for j in range(num_cities) if c != j and (c, j) in x) - lpSum(x[(i, c)] for i in range(num_cities) if i != c and (i, c) in x) == 0

# Solve the problem using the default solver
problem.solve()

# Construct the tour from the solution
tour = [0]
while len(tour) <= len(city_groups):
    current_city = tour[-1]
    for next_city in range(num_cities):
        if next_city != current_city and x[(current_city, next_city)].varValue == 1:
            tour.append(next_single_choice)
            break

# Include return to the depot
tour.append(0)

# Calculate the total cost based on the tour
travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {travel_cost}")