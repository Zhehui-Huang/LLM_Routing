import pulp as pl
import math

# Coordinates of the cities
coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Grouping of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Distance function
def distance(city1, city2):
    c1, c2 = coordinates[city1], coordinates[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities and depot
cities = sum(groups.values(), [])
cities_with_depot = [0] + cities

# Problem setup
prob = pl.LpProblem("TSP_VRP_Minimal_Path", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((i, j) for i in cities_with_depot for j in cities_with_depot if i != j), cat='Binary')

# Objective
prob += pl.lpSum(x[(i, j)] * distance(i, j) for i in cities_with_deplet for j in cities_with_depot if i != j)

# Constraints for each group to go out once and come in once
for idx, group in groups.items():
    # Outgoing connections
    prob += pl.lpSum(x[(i, j)] for i in group for j in cities_with_depot if j not in group) == 1
    # Incoming connections
    prob += pl.lpSum(x[(j, i)] for i in group for j in cities_with_depot if j not in group) == 1

# Ensure connection from/to the depot
prob += pl.lpSum(x[(0, j)] for j in cities) == 1
prob += pl.lpSum(x[(j, 0)] for j in cities) == 1

# Flow conservation constraint for other nodes
for i in cities:
    prob += (pl.lpSum(x[(j, i)] for j in cities_with_deplet if j != i) ==
             pl.lpSum(x[(i, j)] for j in cities_with_deplet if j != i))

# Solve the problem
prob.solve()

# Check if the problem has a feasible solution
if prob.status == pl.LpStatusOptimal:
    # Output results
    tour = [0]
    current = 0
    visited = [False] * len(cities_with_depot)
    visited[0] = True
    for _ in range(len(groups)):
        next_cities = [j for j in cities_with_depot if not visited[j] and pl.value(x[(current, j)]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(next_city)
            current = next_city
            visited[current] = True
    tour.append(0)  # return to depot
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total=("Total distance: ", total_cost))
else:
    print("No feasible solution found")