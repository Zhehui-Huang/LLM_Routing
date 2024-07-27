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

# Create a function to solve the MILP
def solve_tsp(cities, city_groups):
    # Create the problem instance
    problem = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)
    
    # Variables: x_ij = 1 if travel from i to j, 0 otherwise
    x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
    
    # Objective: Minimize the sum of distances traveled
    problem += pulp.lpSum(x[(i, j)] * calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j), "Total_Distance_Traveled"
    
    # Constraints
    # From each group, one node must link to another node not in its group
    for group in city_groups:
        problem += pulp.lpSum(x[(i, j)] for i in group for j in set(cities) - set(group)) == 1, f"outlink_group_{city_groups.index(group)}"
        problem += pulp.lpSum(x[(j, i)] for i in group for j in set(cities) - set(group)) == 1, f"inlink_group_{city_groups.index(group)}"
        
    # Flow conservation
    for i in cities:
        problem += pulp.lpSum(x[(j, i)] for j in cities if i != j) == pulp.lpSum(x[(i, k)] for k in cities if i != k), f"flow_conservation_{i}"
    
    # Solve the problem
    status = problem.solve()
    print(f"Status: {pulp.LpStatus[status]}")
    
    # Extract tour
    tour = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[(i, j)]) == 1:
                tour.append((i, j))
    
    # Since we get many pairs, we need to order them into a proper tour
    # Starting point
    start = 0
    ordered_tour = [start]
    while len(ordered_tour) < len(city_groups) + 1:
        next_city = next(j for i, j in tour if i == ordered_toor[-1])
        ordered_tour.append(next_city)
    
    # Return to start to complete the tour
    ordered_tour.append(start)
    
    # Calculate the total cost of the tour
    total_cost = sum(calculate_distance(cities[ordered_tour[i]], cities[ordered_tour[i+1]]) for i in range(len(ordered_tour)-1))
    
    return ordered_tour, total_cost

# Call the function and print the result
optimal_tour, total_travel_cost = solve_tsp(cities, city_groups)
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")