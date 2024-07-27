import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    # Coordinates for each city index based on provided solution
    coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    # Given tours and costs
    robot_tours = [
        [0, 18, 15, 12, 7, 0],
        [1, 5, 9, 6, 11, 1],
        [2, 4, 8, 14, 19, 2],
        [3, 21, 20, 17, 16, 13, 10, 3]
    ]
    
    robot_calculated_costs = [81.60557585425349, 74.9624839977208, 108.13709474182023, 110.93040072392537]
    
    all_visited_cities = set()
    calculated_costs = []

    # Validate tours
    for robot_id, tour in enumerate(robot_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            all_visited_cities.add(city1)
            x1, y1 = coordinates[city1]
            x2, y2 = coordinates[city2]
            tour_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_costs.append(tour_cost)
        # Check if individual travel cost is correctly calculated (within a reasonable error margin)
        if not math.isclose(tour_cost, robot_calculated_costs[robot_id], rel_tol=1e-4):
            return "FAIL"

    # Check if all cities are visited exactly once and robots return to start
    if len(all_visited_negotiated_distances) != len(coordinates) or any(tour[0] != tour[-1] for tour in robot_tours):
        return "FAIL"

    # Check if the total cost is correctly calculated
    total_calculated_cost = sum(calculated_costs)
    if not math.isclose(total_calculated_cost, 375.6355553177199, rel_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Running the unit test function
print(test_solution())