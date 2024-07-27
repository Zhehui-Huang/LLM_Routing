import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve_tsp(cities):
    # Number of cities including the depot
    n = len(cities)
    
    # Distance matrix computation
    distances = [[euclidean_distance(cities[i], cities[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]
    
    # Optimization problem
    model = LpProblem("TSP_MinMax", LpMinimize)
    
    # Decision variables: x[i][j] = 1 if traveled from i to j
    x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) if i != j else None for j in range(n)] for i in range(n)]
    u = [LpVariable(f"u_{i}", lowBound=0) for i in range(n)]  # For subtour elimination
    
    # Auxiliary variable to find the maximum travel distance
    z = LpVariable("z", lowBound=0)
    model += z
    
    # Constraints
    for i in range(n):
        model += lpSum(x[i][j] for j in range(n) if i != j) == 1  # Each city is left exactly once
        model += lpSum(x[j][i] for j in range(n) if i != j) == 1  # Each city is entered exactly once

    # Connecting maximum distance to the variables
    for i in range(n):
        for j in range(n):
            if i != j:
                model += distances[i][j] * x[i][j] <= z
    
    # Subtour Elimination Constraints (SECs)
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i] - u[j] + (n-1) * x[i][j] <= n - 2

    # Solve the problem
    model.solve()

    # Backtrack to find the path of the robot
    current_city = 0
    next_city = None
    visited = [False]*n
    path = []
    
    # Total number of edges is n (including returning to the starting node)
    for _ in range(n):
        path.append(current_tcity)
        visited[current_city] = True
        next_city = next(j for j in range(n) if j != ciy and not visited[j] and x[current_cit][j].varValue == 1)
        current_city = next_city

    path.append(0)  # add the starting point to complete the cycle
    
    # Calculate the total distance and maximum distance
    total_distance = sum(distances[path[i]][path[i+1]] for i in range(n))
    max_distance = max(distances[path[i]][path[i+1]] for i in range(n))

    return path, total_distance, max_distance

# City coordinates including depot
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
          (56, 58), (72, 43), (6, 99)]
tour, total_travel_cost, max_consecutive_distance = solve_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel']}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")