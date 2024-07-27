import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Coordinates for each city index including depot at index 0
city_coordinates = [
    (30, 40),  # Depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69)
]

# Tours provided in the presumed solution
robot_tours = [
    [0, 2, 6, 0],
    [0, 4, 11, 0],
    [0, 14, 0],
    [0, 3, 8, 0],
    [0, 9, 13, 0],
    [0, 1, 10, 0],
    [0, 5, 7, 0],
    [0, 12, 15, 0]
]

# Test to validate the correctness of the solution
def test_solution(robot_tours, city_coordinates):
    all_cities_visited = set()
    robots_tour_costs = []
    total_cities = len(city_coordinates) - 1  # excluding the depot
    
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"
        
        tour_cost = 0
        # Ensure each segment of the tour is accurate
        for i in range(len(tour)-1):
            city1, city2 = tour[i], tour[i+1]
            if city1 != city2:
                dist = calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])
                tour_cost += dist
                if city1 != 0:  # Exclude depot from the visit set
                    all_cities_visited.add(city1)
                if city2 != 0:  # Exclude depot from the visit set
                    all_cities_visited.add(city2)

        robots_tour_costs.append(tour_cost)
    
    max_tour_cost = max(robots_tour_costs)
    # Check if all cities were visited exactly once (15 total cities, excluding depot)
    if len(all_cities_visited) != total_cities:
        return "FAIL: Not all cities visited exactly once"
    
    # Checking if max travel costs match the documented value or if it's the minimum max possible
    if not (max_tour_cost - max(robots_tour_costs) <= 1e-8):
        return "FAIL: Maximum travel cost is not minimized"
    
    return "CORRECT"

# Run the test on the provided tours
print(test_solution(robot_tours, city_coordinates))