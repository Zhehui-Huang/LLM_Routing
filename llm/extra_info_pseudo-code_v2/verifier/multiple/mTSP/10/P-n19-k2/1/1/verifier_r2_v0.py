import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tours(city_coords, tours, expected_costs):
    number_of_cities = len(city_coords)
    visited_cities = set()
    
    # Verify each robot's tour
    for tour_index, tour in enumerate(tours):
        start_city = tour[0]
        end_city = tour[-1]

        # Check start and end city
        if start_city != 0 or end_city != 0:
            return "FAIL"

        # Calculating the travel cost for current tour
        actual_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            visited_cities.add(city1)
            actual_cost += calculate_euclidean_distance(*city_coords[city1], *city_coords[city2])

        # Compare costs with a tolerance because of floating-point arithmetic
        if not math.isclose(actual_cost, expected_costs[tour_index], rel_tol=1e-5):
            return "FAIL"
        
        visited_cities.add(tour[-1])
    
    # Check all cities visited exactly once (excluding depot)
    if len(visited_cities) != number_of_cities or any(i != 0 and visited_cities.count(i) != 1 for i in range(number_of_cities)):
        return "FAIL"

    return "CORRECT"

# Define city coordinates based on problem statement, index 0 is depot
cities_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                      (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Tours provided in solution
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 16, 0]
robot_1_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 0]

# Expected costs from solution
robot_0_cost = 142.067115100104
robot_1_cost = 143.35854658836402

# Combining tours and their costs
tours = [robot_0_tour, robot_1_tour]
costs = [robot_0_cost, robot_1_cost]

# Perform verification
result = verify_tours(cities_coordinates, tours, costs)
print(result)