import math
import pulp

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def solve_tsp_bottleneck(cities):
    dist = { (i, j): calculate_distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j }
    
    # Optimisation problem
    problem = pulp.LpProblem('Minimax_TSP', pulp.LpMinimize)
    
    # x_ij are binary variables
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j), 0, 1, pulp.LpBinary)
    D = pulp.LpVariable("D", lowBound=0)
    
    # Objective function to minimize maximum travel distance between any two visited consecutive cities
    problem += D

    # Constraints
    # Ensure every city except depot sends and receives 1 traveled path
    for i in range(1, len(cities)):
        problem += pulp.lpSum([x[i, j] for j in range(len(cities)) if j != i]) == 1
        problem += pulp.lpSum([x[j, i] for j in range(len(cities)) if j != i]) == 1

    # Departure from and return to the depot constraints
    problem += pulp.lpSum(x[0, j] for j in range(1, len(cities))) == 1
    problem += pulp.lpSum(x[i, 0] for i in range(1, len(cities))) == 1

    # Subtour elimination constraints
    u = pulp.LpVariable.dicts("u", range(1, len(cities)), 1, len(cities)-1, cat=pulp.LpInteger)
    for i in range(1, len(cities)):
        for j in range(1, len(cities)):
            if i != j:
                problem += u[i] - u[j] + (len(cities) * x[i, j]) <= len(cities)-1

    # Distances for max D constraints
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                problem += x[i, j] * dist[i, j] <= D

    # Solving the problem
    status = problem.solve()

    # Checking if the problem is solved correctly
    if status != pulp.LpStatusOptimal:
        print("Failed to find optimal solution.")
        return

    # Retrieve results
    tour = []
    current = 0
    while True:
        tour.append(current)
        next_city = [j for j in range(len(cities)) if x[current, j].varValue > 0.99]
        if not next anderen):
            break
        current = next_city[0]
    
    tour.append(0)  # Returning to the depot

    # Calculate the total cost and maximum leg distance
    total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_leg_distance = max(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))

    return {
        'Tour': tour,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_leg_distance
    }

# Specify the location of the cities
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), 
          (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Call the function and display the results
result = solve_tsp_bottleneck(cities)
print("Tour:", result['Tour'])
print("Total travel cost:", round(result['Total travel cost'], 2))
print("Maximum distance between consecutive cities:", round(result['Maximum distance between consecutive cities'], 2))