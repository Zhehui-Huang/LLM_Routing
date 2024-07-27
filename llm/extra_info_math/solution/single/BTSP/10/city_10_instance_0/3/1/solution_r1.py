import pulp
import math
from itertools import combinations

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def solve_tsp_with_minmax_distance(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Create the problem
    prob = pulp.LpProblem("TSP_MinMax_Distance", pulp.LpMinimize)
    
    # Decision variables
    x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)
    max_distance = pulp.LpVariable("max_distance", lowBound=0)

    # Objective function
    prob += max_body

    # Constraints
    for i in range(n):
        # Sum of outgoing edges from each node
        prob += pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1
        # Sum of incoming edges to each node
        prob += pulp.lpSum([x[j][i] for j in range(n) if i != j]) == 1
    
    for i in range(n):
        for j in range(n):
            if i != j:
                prob += distances[i][j] * x[i][j] <= max_distance

    # Subtour elimination constraints
    for s in range(2, n):
        for subset in combinations(range(1, n), s):
            prob += pulp.lpSum([x[i][j] for i in subset for j in subset if i != j]) <= len(subset) - 1
    
    # Solve the problem
    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))  # Silent mode

    if status != pulp.LpStatusOptimal:
        return {"Message": "No optimal solution found."}

    # Retrieve the solution
    tour = []
    cur_location = 0
    remaining_cities = list(range(1, n))
    while remaining_cities:
        for j in range(n):
            if pulp.value(x[cur_location][j]) == 1 and j in remaining_cities:
                tour.append(j)
                remaining_cities.remove(j)
                cur_location = j
                break
    tour = [0] + tour + [0]  # Start and end at the depot

    max_dist = pulp.value(max_distance)
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return {"Tour": tour, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_dist}

# Define the coordinates of each city
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Solve the problem
result = solve_tsp_with_minmax_distance(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']:.2f}")