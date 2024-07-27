import numpy as np

# Data provided in the solution example
robots_tours = {
    0: [0, 6],
    1: [1, 10, 2],
    2: [2, 7],
    3: [3, 8, 13, 9, 14, 5],
    4: [4, 11, 15, 12, 3],
    5: [5, 7],
    6: [6, 0],
    7: [7, 6]
}

# Collect existing costs from submission for comparison
submitted_costs = {
    0: 12.04,
    1: 17.7,
    2: 8.54,
    3: 49.08,
    4: 33.07,
    5: 8.0,
    6: 12.04,
    7: 10.0
}

# City coordinates as provided
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Ensure all tours meet requirements
all_nodes_visited = set()
all_costs_calculated = 0

# Euclidean distance function
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Check the conditions
for robot_id, tour in robots_tours.items():
    # Check the starting condition
    if tour[0] != 0:  # As per the requirement, robots should start from city 0.
        print("FAIL")
        break
    
    # Calculate travel costs and check if each city is visited once
    prev_city = None
    total_cost = 0
    for city in tour:
        if prev_city is not None:
            dist = euclidean_distance(city_coords[prev_city], city_coords[city])
            total_cost += dist
        prev_city = city
        if city in all_nodes_visited and city != 0:
            print("FAIL")  # City visited more than once
            break
        all_nodes_visited.add(city)
    
    all_costs_calculated += total_cost

    # Check approximate match in cost (allow slight floating point differences)
    if not np.isclose(total_cost, submitted_costs[robot_id], atol=0.01):
        print("FAIL")
        break
else:
    # Check if all cities were visited exactly once
    if len(all_nodes_visited) != 16:
        print("FAIL")
    else:
        print("CORRECT")