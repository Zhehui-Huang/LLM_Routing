def calculate_euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def verify_solution(tours, costs, cities, demands, max_capacity):
    # Check if each tour begins and ends at the depot (criterion 1 & all cities visited once check)
    visited = set()
    total_cost_calculated = 0
    for tour, cost in zip(tours, costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate tour cost and demand
        tour_cost = 0
        load = 0
        for i in range(len(tour)-1):
            tour_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            if tour[i] != 0:  # exclude depot city from demand sum
                load += demands[tour[i]]
                visited.add(tour[i])
            
        if round(tour_cost) != cost:
            return "FAIL"
        
        # Check capacity constraints (criterion 3)
        if load > max_capacity:
            return "FAIL"
        
        total_cost_calculated += tour_cost
    
    # Check if all cities are visited exactly once (criterion 2)
    if len(visited) != len(cities) - 1:
        return "FAIL"

    # Output the correct message if no fails found
    return "CORRECT"

# Given data
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

robot_tours = [
    [0, 8, 0],
    [0, 5, 14, 0],
    [0, 10, 12, 15, 0],
    [0, 11, 4, 0],
    [0, 13, 9, 7, 0],
    [0, 2, 0],
    [0, 3, 1, 0],
    [0, 6, 0]
]

robot_costs = [6488, 6243, 6699, 5739, 6839, 4204, 6564, 2408]

# Verify the solution
result = verify_solution(robot_tours, robot_costs, cities, demands, 35)
print(result)