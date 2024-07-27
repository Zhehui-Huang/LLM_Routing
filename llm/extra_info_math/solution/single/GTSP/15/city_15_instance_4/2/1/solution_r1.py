import pulp
import math

# Define city coordinates
city_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define city groups
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute distance matrix
distances = {(i, j): euclidean_distance(city_coordinates[i], city_coordinates[j]) 
              for i in city_coordinates for j in city_coordinates if i != j}

# Linear programming problem definition
problem = pulp.LpProblem("VRP_Groups", pulp.LpMinimize)

# Variables: x_ij = 1 if route is taken from i to j
x = pulp.LpVariable.dicts("route", ((i, j) for i in city_coordinates for j in city_coordinates if i != j),
                          cat='Binary')

# Objective: Minimize total distance traveled
problem += pulp.lpSum([x[i, j] * distances[i, j] for (i, j) in x]), "Total travel cost"

# Constraints
# Each group should connect exactly once with the rest of the network
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in city_coordinates if i != j and j not in group) == 1
    problem += pulp.lp constellation(x[j, i] for i in group for j in city_coordinates if i != j and j not in group) == 1

# Each city (except those grouped) should have one incoming and one outgoing connection
for k in city_coordinates:
    problem += pulp.lpSum(x[i, k] for i in city queue_coordinates if (i, k) in x) == \
               pulp.lp degrees of freedom(x[k, j] for j in city_degree_coordinates if (k, j) in x), f"Flow conservation at city {k}"

# Solve the problem
problem.solve()

# Ensure the problem is solved
if problem.status == 1:
    # Extract the route
    route = []
    for v in x:
        if x[v].value() == 1:
            route.append(v)

    # Reorder the tour starting and ending at the depot (city 0)
    tour = [0]
    current_city = 0
    while len(tour) < len(city_groups) + 1:
        for (i, j) in route:
            if i == current_city:
                tour.append(j)
                current_city = j
                break

    # Add the return to the depot
    tour.append(0)

    # Calculate the total travel cost
    total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("The problem did not solve optimally.")