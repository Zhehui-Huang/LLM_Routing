from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp(cities):
    num_cities = len(cities)
    # Cost matrix
    cost = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    # Problem
    model = LpProblem("TSP", LpMinimize)
    
    # Variables: x[i][j] is 1 if the tour moves from city i to city j
    x = [[LpVariable(f"x({i},{j})", cat=LpBinary) if i != j else None for j in range(num_cities)] for i in range(num_cities)]
    
    # Objective
    model += lpSum(cost[i][j] * x[i][j] for i in range(num_cities) for j in range(num_cities) if i != j)
    
    # Constraints
    for i in range(num_cities):
        model += lpSum(x[i][j] for j in range(num_cities) if i != j) == 1  # leave each city once
        model += lpSum(x[j][i] for j in range(num_cities) if i != j) == 1  # enter each city once

    # Sub-tour elimination (using MTZ approach)
    u = [LpVariable(f"u({i})", lowBound=0, cat='Continuous') for i in range(num_cities)]
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                model += u[i] - u[j] + num_cities * x[i][j] <= num_cities - 1
    
    # Solve problem
    model.solve()
    
    # Extract tour
    tour = []
    used_edges = [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j and x[i][j].varValue == 1]
    current_location = 0
    while len(used_edges) > 0:
        for i, j in used_edges:
            if i == current_location:
                tour.append(current_location)
                current_location = j
                used_edges.remove((i, j))
                break
    tour.append(0)  # return to the depot

    total_cost = sum(cost[i][j] for i, j in zip(tour[:-1], tour[1:]))
    
    return tour, total_cost

# Define the cities based on the given coordinates
cities = [
    (53, 68),  # depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Find the shortest tour
tour, total_cost = solve_tsp(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")