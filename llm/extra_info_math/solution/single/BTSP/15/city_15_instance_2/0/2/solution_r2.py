import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, PULP_CBC_CMD

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp(cities):
    n = len(cities)  # Including the depot
    
    # Distance matrix
    distances = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i, j] = euclidean_distance(cities[i], cities[j])
            else:
                distances[i, j] = float('inf')  # Prevent looping to the same city

    # Define the problem
    prob = LpProblem("TSP", LpMinimize)

    # Decision variables
    x = LpVariable.dicts('x', distances, 0, 1, LpBinary)

    # The 'largest' distance as our minimization target
    max_dist = LpVariable("max_dist", 0)

    # Objective
    prob += max_dist

    # Constraints
    for k in range(n):
        # Exactly one outgoing edge
        prob += lpSum([x[(i, j)] for i, j in distances if i == k]) == 1
        # Exactly one incoming edge
        prob += lpSum([x[(i, j)] for i, j in distances if j == k]) == 1

    # Max distance constraint
    for i, j in distances:
        prob += distances[i, j] * x[(i, j)] <= max_dist

    # Subtour Elimination
    u = LpVariable.dicts('u', range(n), 0, n-1, cat='Continuous')
    for i, j in distances:
        if i != j and i != 0 and j != 0:
            # n - 1 is maximum number of nodes that could be in any subtour
            prob += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=0))

    # Extract the tour
    edges = [(i, j) for i, j in x if x[(i, j)].value() == 1]
    tour = [0]
    while len(tour) < n:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                break

    tour.append(0)  # To return to the starting point

    # Calculate cost and maximum consecutive distance
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(n))
    max_consecutive_dist = max(distances[tour[i], tour[i+1]] for i in range(n))

    return tour, total_cost, max_consecutive_dist

# City coordinates including depot
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
          (56, 58), (72, 43), (6, 99)]

tour, total_travel_cost, max_consecutive_distance = solve_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")