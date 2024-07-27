import pulp
import math

# Coordinates for each city
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Grouping of cities
city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Function to calculate the euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# List of all cities including the depot
all_cities = list(cities.keys())

# Setting up the optimization problem: Minimizing cost
problem = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Decision variables: x_ij where i != j and represents paths between cities
x = pulp.LpVariable.dicts("x",(all_cities, all_cities),0,1,pulp.LpBinary)

# Objective function: Minimize total travel distance
problem += pulp.lpSum(x[i][j] * euclidean_distance(i, j) for i in all_cities for j in all_cities if i != j), "Total Travel Cost"

# Constraints to ensure exactly one path out of and into each group
for group, members in city_groups.items():
    problem += pulp.lpSum(x[i][j] for i in members for j in all_cities if j not in members) == 1, f"Outgroup from group {group}"
    problem += pulp.lpSum(x[j][i] for i in members for j in all_cities if j not in members) == 1, f"Ingroup to group {group}"

# Flow conservation constraint to ensure entering and leaving each city once
for city in all_cities:
    problem += pulp.lpSum(x[i][city] for i in all_cities if i != city) == pulp.lpSum(x[city][j] for j in all_cities if j != city), f"Flow Conservation in city {city}"

# Solve the ILP problem
problem.solve()

# Output the results
if pulp.LpStatus[problem.status] == 'Optimal':
    print("Optimal solution found.")
    route = []
    current_city = 0
    visited = set()
    while True:
        next_cities = [j for j in all_cities if pulp.value(x[current_city][j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        route.append(next_city)
        current_city = next_city
        if next_city == 0:
            break
    route = [0] + route

    # Calculate total travel cost from the route
    total_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))

    print("Tour:", route)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution available.")