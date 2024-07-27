import pulp
import math

# Define the city coordinates
cities = {
    0: (90, 3),  # depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define city groups
city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a list of all vertices and a list of possible nodes except the depot to be visited
V = list(cities.keys())
k = len(city_groups)  # number of groups
n = len(V)
perms = []

# Generate permutations including one city from each group and the depot
from itertools import product

for group_perm in product(*(city_groups[group] for group in range(k))):
    perms.append(list(group_perm))

# Define the problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variable x_ij, where x_ij = 1 if travel from city i to city j, else 0
x = pulp.LpVariable.dicts("x", (V, V), cat='Binary')

# Objective Function
problem += pulp.lpSum(x[i][j] * euclidean_distance(i, j) for i in V for j in V if i != j)

# Constraints
# Ensure that start and end at depot, having exactly one exit and one entrance
problem += pulp.lpSum(x[0][j] for j in V if j != 0) == 1
problem += pulp.lpSum(x[i][0] for i in V if i != 0) == 1

for perm in perms:
    chosen_cities = [0] + perm
    # Flow conservation for intermediate cities in each tour permutation
    for city in chosen_cities:
        problem += pulp.lpSum(x[city][j] for j in chosen_cities if j != city) == 1
        problem += pulp.lpSum(x[i][city] for i in chosen_cities if i != city) == 1

# Solve the problem
status = problem.solve()

# Extract the results
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    tour.append(current_city)
    
    visited = set()
    visited.add(current_city)
    
    while len(tour) < len(V):
        for next_city in V:
            if pulp.value(x[current_city][next_city]) == 1 and next_city not in visited:
                current_city = next_city
                tour.append(current_city)
                visited.add(current_city)
                break

    # Complete the tour back to the depot
    tour.append(0)
    total_distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("Failed to find an optimal solution.")