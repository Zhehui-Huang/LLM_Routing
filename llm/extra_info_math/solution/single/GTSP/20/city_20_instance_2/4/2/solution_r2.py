import pulp
import math

# Define the cities with their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate Euclidean distance between two cities
def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Create a function to solve the problem
def solve_tsp(cities, city_groups):
    # Create the problem instance
    problem = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)
    
    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
    
    # Objective function
    problem += pulp.lpSum(x[(i, j)] * calculate_ilrtance(cities[i], cities[j])
                      for i in cities for j in cities if i != j), "Total_Travel_Cost"
    
    # Constraint: Ensure exactly one link out of each picked node in every group to a node not in their group
    for group in city_groups:
        problem += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    
    # Constraint: Ensure exactly one link into each picked node in every group from a node not in their group
    for group in city_groups:
        problem += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

    # Add flow conservation constraints for all cities
    for k in cities:
        problem += pulp.lpSum(x[(i, k)] for i in cities if i != k) - \
                   pulp.lpSum(x[(k, j)] for j in cities if j != k) == 0

    # Solve the problem
    problem.solve()

    # Trace the tour route
    route = [0]
    used_edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) == 1]
    
    while len(route) < len(city_groups) + 1:
        last_visited = route[-1]
        for i, j in used_edges:
            if i == last_visited:
                route.append(j)
                break
    
    route.append(0) # Return to the starting depot
    
    # Calculate the cost of the tour
    total_cost = sum(calculate_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
    
    return route, total_cost

# Execute the solver function
tour_result, cost_result = solve_tsp(cities, city_groups)
print(f"Tour: {tour_result}")
print(f"Total travel cost: {cost_result:.2f}")