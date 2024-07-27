import numpy as np

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def verify_solution(tours, costs, max_cost, city_coords, depot_city, num_robots):
    # Check number of robots
    if len(tours) != num_robots or len(costs) != num_robots:
        return "FAIL"
    
    visited_cities = set()
    for tour in tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != depot_city or tour[-1] != depot_city:
            return "FAIL"

        # Add visited cities from this tour excluding the depot
        visited_cities.update(tour[1:-1])
    
    # Check if all cities are visited exactly once
    if len(visited_cities) != len(city_coords) - 1:  # excluding the depot city
        return "FAIL"
    
    calculated_costs = []
    for tour in tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
        calculated_costs.append(total_cost)
    
    # Check costs
    if not all(np.isclose(cost, calc_cost) for cost, calc_cost in zip(costs, calculated_costs)):
        return "FAIL"

    # Check if the max cost matches the calculated max cost
    if not np.isclose(max(costs), max_cost):
        return "FAIL"
    
    # The primary objective: minimize the maximum distance traveled by any robot
    if max_cost != max(costs):
        return "FAIL"
    
    return "CORRECT"

# City coordinates (including depot city)
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tests
tours = [
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 17, 18, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0],
    [0, 12, 13, 14, 15, 16, 0]
]

costs = [124.24, 150.44, 111.84, 107.31]
max_cost = 150.44
depot_city = 0
num_robots = 4

# Verify the solution
result = verify_solution(tours, costs, max_cost, city_coords, depot_city, num_robots)
print(result)