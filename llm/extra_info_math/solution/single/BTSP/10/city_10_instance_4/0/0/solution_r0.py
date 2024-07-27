import math
import pulp

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def solve_tsp_bottleneck(cities):
    # Calculate distances between all pairs of cities
    dist = { (i, j): calculate_distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j }
    
    # Create the problem variable to contain the problem data
    problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
    
    # Create variable x_ij and D (max distance)
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j), 0, 1, pulp.LpBinary)
    max_distance = pulp.LpVariable("Max_Distance", lowBound=0, cat=pulp.LpContinuous)
    
    # Objective function
    problem += max_distance

    # Constraint: Exactly one outgoing edge from each city
    for i in range(len(cities)):
        problem += pulp.lpSum(x[i, j] for j in range(len(cities)) if i != j) == 1
    
    # Constraint: Exactly one incoming edge to each city
    for j in range(len(cities)):
        problem += pulp.lpSum(x[i, j] for i in range(len(cities)) if i != j) == 1

    # Subtour elimination constraints (Miller-Tucker-Zemlin formulation)
    u = pulp.LpVariable.dicts("u", range(len(cities)), 0, len(cities) - 1, pulp.LpInteger)
    for i in range(1, len(cities)):
        for j in range(1, len(cities)):
            if i != j:
                problem += u[i] - u[j] + len(cities)*x[i, j] <= len(cities) - 1

    # Max distance constraint
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                problem += dist[i, j] * x[i, j] <= max_distance

    problem.solve()

    tour = [0]
    total_cost = 0
    max_leg_distance = 0
    while True:
        next_city = [j for j in range(len(cities)) if pulp.value(x[tour[-1],j]) == 1][0]
        max_leg_distance = max(max_leg_distance, dist[tour[-1], next_city])
        total_cost += dist[tour[-1], next_city]
        tour.append(next_city)

        if next_city == 0:
            break

    return {
        'Tour': tour,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_leg_distance
    }

# Define cities based on given coordinates
cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), 
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Solve the problem
result = solve_tsp_bottleneck(cities)
print("Tour:", result['Tour'])
print("Total travel cost:", round(result['Total travel cost'], 2))
print("Maximum distance between consecutive cities:", round(result['Maximum distance between consecutive cities'], 2))