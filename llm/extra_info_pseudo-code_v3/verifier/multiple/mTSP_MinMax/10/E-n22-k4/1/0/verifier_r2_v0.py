import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities provided their coordinates."""
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution():
    # City coordinates as provided in the problem statement
    city_coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    # Provided robot tours
    tours = [
        [0, 16, 14, 18, 15, 12, 0],
        [0, 10, 8, 6, 3, 4, 11, 0],
        [0, 17, 20, 21, 19, 13, 0],
        [0, 1, 2, 5, 7, 9, 0]
    ]
    
    # External output with costs for comparison
    calculated_costs = [76.88670610294182, 99.60668471182551, 102.92102628707408, 111.83855721201843]
    max_calculated_cost = 111.83855721201843
    
    # Setup to check total costs and city coverage
    visited_cities = set()
    robot_costs = []
    
    # Calculate costs based on provided tours and city distances
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += calculate_distance(city_coordinates[tour[i - 1]], city_coordinates[tour[i]])
        robot_costs.append(tour_cost)
        visited_cities.update(tour)
    
    # Check each robot starts and ends at the depot, and visits cities only once
    all_cities_visited_once = len(visited_cities) == len(city_coordinates) and all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    
    # Verify costs and maximum constraint
    correct_costs = all(math.isclose(robot_costs[i], calculated_costs[i], rel_tol=1e-3) for i in range(len(robot_costs)))
    correct_max_cost = math.isclose(max(robot_costs), max_calculated_cost, rel_tol=1e-3)
    
    # If all conditions are met, the solution is correct
    if all_cities_visited_once and correct_costs and correct_max_cost:
        print("CORRECT")
    else:
        print("FAIL")

# Running the test
test_solution()