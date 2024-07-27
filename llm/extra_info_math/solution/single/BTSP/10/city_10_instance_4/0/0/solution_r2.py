import math
import pulp

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def solve_tsp_bottleneck(cities):
    # Number of cities
    n = len(cities)
    # Create a problem instance
    problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
    
    # Distance dictionary
    distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}
    
    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
    D = pulp.LpVariable("D", lowBound=0, cat=pulp.LpContinuous)
    
    # Objective: minimize the maximum distance D
    problem += D
    
    # Constraints: exactly one outgoing and one incoming edge for each node
    for i in range(n):
        problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
        problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1
    
    # Limit D to be at least the distance of any edge in the tour
    for i in range(n):
        for j in range(n):
            if i != j:
                problem += x[(i, j)] * distances[(i, j)] <= D
    
    # Subtour elimination
    u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                problem += u[i] - u[j] + n * x[(i, j)] <= n - 1
    
    # Solve the problem
    problem.solve()
    
    # Extract the tour
    tour = []
    for i in range(n - 1):
        for j in range(n):
            if i != j and pulp.value(x[(i, j)]) == 1:
                tour.append((i, j))

    # Sort tour into a readable format, starting at the depot
    if len(tour) == 0:
        return "No solution found."
    
    route = [0]
    while len(route) < n:
        current = route[-1]
        for link in tour:
            if link[0] == current:
                route.append(link[1])
                break
    
    route.append(0)  # complete tour by returning to depot

    # Calculate tour metrics
    max_distance = pulp.value(D)
    total_distance = sum(distances[tour[i]] for i in range(len(tour) - 1))

    return {
        "Tour": route,
        "Total travel cost": total_distance,
        "Maximum distance between consecutive cities": max_distance
    }

# Define cities based on given coordinates
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
               (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solve and print the TSP solution.
result = solve_tsp_bottleneck(coordinates)
print("Tour:", result['Tour'])
print("Total travel cost:", round(result['Total travel cost'], 2))
print("Maximum distance between consecutive cities:", round(result['Maximum distance between consecutive cities'], 2))