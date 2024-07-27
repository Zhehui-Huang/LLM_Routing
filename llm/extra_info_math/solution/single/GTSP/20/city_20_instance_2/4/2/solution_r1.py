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


def solve_tsp(cities, city_groups):
    # Problem instance
    problem = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)
    
    # Variables
    x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
    
    # Objective
    problem += pulp.lpSum(x[(i, j)] * calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j), "Total_Distance_Traveled"
    
    # Constraints
    for group in city_groups:
        problem += pulp.lpSum(x[(i, j)] for i in group for j in set(cities) - set(group)) == 1  # Exactly one outgoing arc
        problem += pulp.lpSum(x[(j, i)] for i in group for j in set(cities) - set(group)) == 1  # Exactly one incoming arc

    # Flow conservation
    for i in cities:
        problem += pulp.lpSum(x[(j, i)] for j in cities if i != j) == pulp.lpSum(x[(i, j)] for j in cities if i != j), f"flow_conservation_{i}"
    
    # Solve the model
    status = problem.solve()
    
    # Check if there is an optimum solution
    if status != pulp.LpStatusOptimal:
        return None, None
    
    # Gather the tour from the solution
    tour = [0]
    while len(tour) < len(city_groups) + 1:
        current = tour[-1]
        next_city = next(j for j in cities if pulp.value(x[(current, j)]) == 1)
        tour.append(next_city)
    tour.append(0)  # Return to depot
    
    # Calculate the travel cost of the tour
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    return tour, total_cost

# Solve the problem
optimal_tour, total_travel_cost = solve_tsp(cities, city_groups)

if optimal_tour and total_travel_cost:
    print(f"Tour: {optimal_tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
else:
    print("No optimal tour found.")