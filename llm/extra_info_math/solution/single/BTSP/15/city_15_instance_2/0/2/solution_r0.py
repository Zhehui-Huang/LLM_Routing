import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve_tsp(cities):
    # Number of cities including the depot
    n = len(cities)
    
    # Distance matrix calculation
    distances = [[euclidean_distance(cities[i], cities[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]
    
    # Optimization model
    model = LpProblem("TSP", LpMinimize)
    
    # Variables: x[i][j] = whether we travel from i to j or not
    x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) if i != j else None for j in range(n)] for i in range(n)]
    u = [LpVariable(f"u_{i}", lowBound=0) for i in range(n)]  # For subtour elimination
    
    # Objective function: Using auxiliary variable z to represent maximum distance
    z = LpVariable("z", lowBound=0)
    model += z
    
    # Constraints: Each city is entered and left exactly once
    for i in range(n):
        model += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Enter_City_{i}"
        model += lpSum(x[j][i] for j in range(n) if i != j) == 1, f"Leave_City_{i}"
    
    # Connection between z and x for maximum distance optimization
    for i in range(n):
        for j in range(n):
            if i != j:
                model += distances[i][j] * x[i][j] <= z, f"Max_Dist_{i}_{j}"
    
    # Subtour elimination constraints
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i] - u[j] + (n * x[i][j]) <= n - 1
    
    # Solve model
    model.solve()
    
    # Extract tour
    route = []
    current_city = 0
    visited = set([current_city])
    route.append(current_city)
    
    # Proceed to next city following x
    while len(visited) < n:
        next_city = next(j for j in range(n) if j != current_post and x[current_city][j].varValue == 1)
        visited.add(next_city)
        route.append(next_city)
        current_city = next_city
    
    # Return to the depot
    route.append(0)
    
    # Calculate total travel cost and maximum distance
    total_cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    max_distance = max(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    
    return route, total_cost, max_distance

# Cities coordinates with depot (included)
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

tour, total_travel_cost, max_consecutive_distance = solve_tsp(cities)

# Output part
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")