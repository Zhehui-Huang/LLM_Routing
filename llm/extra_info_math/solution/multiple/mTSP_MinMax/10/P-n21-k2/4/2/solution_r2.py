import numpy as np
from scipy.spatial.distance import euclidean
import pulp

def calculate_distance_matrix(coordinates):
    """ Calculate a distance matrix based on euclidean distance. """
    n = len(coordinates)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])
    return dist_matrix

def solve_mTSP(num_robots, coordinates):
    """ Solves the multiple Traveling Salesman Problem using linear programming (PuLP) """
    n = len(coordinates)
    dist_matrix = calculate_distance_matrix(coordinates)
    
    problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(num_robots) if i != j),
                              cat='Binary')

    # Objective: Minimize the maximum route distance travelled by any robot
    max_distance = pulp.LpVariable("max_distance")
    problem += max_distance

    # Constraints
    # Each non-depot city must be visited exactly once by exactly one robot
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(n) if i != j) == 1
    
    # Each robot starts and ends at the depot
    for k in range(num_robots):
        problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
        problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1
    
    # Flow conservation: enter and leave each city just once for each robot
    for k in range(num_robots):
        for j in range(1, n):
            problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)
    
    # Max distance constraint
    for k in range(num_robots):
        problem += pulp.lpSum(x[i, j, k] * dist_matrix[i][j] for i in range(n) for j in range(n) if i != j) <= max_distance

    # Solve
    problem.solve()

    routes = {}
    costs = {}
    
    for k in range(num_robots):
        route = [0]
        current_city = 0
        while True:
            next_city = next(j for j in range(1, n) if pulp.value(x[current_city, j, k]) == 1)
            route.append(next_city)
            current_city = next_city
            if current_city == 0:
                break
        routes[k] = route
        costs[k] = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

    max_cost = pulp.value(max_distance)

    results = {
        "routes": routes,
        "costs": costs,
        "max_cost": max_cost
    }
    return results

# Usage
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

num_robots = 2
results = solve_mTSP(num_robots, coordinates)

for k in results["routes"]:
    print(f"Robot {k} Tour: [{', '.join(map(str, results['routes'][k]))}]")
    print(f"Robot {k} Total Travel Cost: {results['costs'][k]}")
print(f"Maximum Travel Cost: {results['max_cost']}")