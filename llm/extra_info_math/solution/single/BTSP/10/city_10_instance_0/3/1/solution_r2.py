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
    max_distance = pulp.LpVariable("max_distance", 0)

    # Objective function
    prob += max_distance

    # Constraints
    for i in range(n):
        # Sum of outgoing edges from each node
        prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
        # Sum of incoming edges to each node
        prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1
    
    # Maximum distance constraint for each arc
    for i in range(n):
        for j in range(n):
            if i != j:
                prob += x[i][j] * distances[i][j] <= max_distance

    # Subtour Elimination
    for S in range(2, n):
        for subset in combinations(range(1, n), S):
            prob += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

    # Solve the problem
    prob.solve()

    # Build the tour list from the decision variables
    tour = [0]
    while len(tour) < n:
        next_city = [j for j in range(n) if pulp.value(x[tour[-1]][j]) == 1][0]
        tour.append(next_city)

    tour.append(0)  # Complete the tour by returning to the depot

    # Calculate the total travel cost and max distance
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_dist = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    return {"Tour": tour, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_dist}

# Define the coordinates of each city
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Solve the problem
result = solve_tsp_with_minmax_distance(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel and