import pulp
import math

# Coordinates of the cities
cities = {
    0: (90, 3),
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

# Groups of cities
city_groups = [
    [3, 6], # Group 0
    [5, 8], # Group 1
    [4, 9], # Group 2
    [1, 7], # Group 3
    [2]     # Group 4
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Generate all combinations of city routes and their distances
distances = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            distances[(city1, city2)] = calculate_distance(city1, city2)

# Define the problem
problem = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Decision variables: x_ij whether route from city i to city j is used
x = pulp.LpVariable.dicts("route", distances, lowBound=0, upBound=1, cat=pulp.LpInteger)

# Objective function: Minimize the total travel distance
problem += pulp.lpSum([distances[route] * x[route] for route in distances]), "Total travel distance"

# Each group should be visited exactly once, ensure connectivity from one node across groups
for group in city_groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"Exit_{city_groups.index(group)}"
    problem += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"Enter_{city_groups.index(group)}"

# Each city must have one entrance and one exit
for city in cities:
    problem += pulp.lpSum(x[(i, city)] for i in cities if (i, city) in x) == pulp.lpSum(x[(city, j)] for j in cities if (city, j) in x), f"Flow_{city}"

# Solve the problem
problem.solve()

# Output results
if pulp.LpStatus[problem.status] == "Optimal":
    print("An optimal solution has been found.")
    
    # Determine the route
    route = []
    for v in problem.variables():
        if v.varValue > 0 and v.name.startswith('route'):
            i, j = eval(v.name.split('_')[1])
            route.append((i, j))

    # Simplify the route for printout and calculate total cost
    current_location = 0
    total_distance = 0
    tour = [0]
    visited = set(tour)
    
    while len(tour) < len(city_groups) + 1:
        for (i, j) in route:
            if i == current_location and j not in visited:
                tour.append(j)
                visited.add(j)
                total_distance += distances[(i, j)]
                current_location = j
                break
    
    # Closing the tour back to the depot
    tour.append(0)
    total_distance += distances[(current_location, 0)]

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
else:
    print("No optimal solution found.")