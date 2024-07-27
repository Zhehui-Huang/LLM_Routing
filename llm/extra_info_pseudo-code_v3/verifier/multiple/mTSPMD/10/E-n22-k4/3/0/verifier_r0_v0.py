import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, costs, cities_coordinates):
    all_cities_set = set(range(22))
    visited_cities = set()
    total_calculated_cost = 0

    for robot_id, tour in enumerate(tours):
        # Check if tour starts and ends at the robot's depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL"

        # Check if each city in the tour (except the last/depot) is visited only once
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculating travel costs for verification
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])

        # Check if costs match
        if not math.isclose(calculated_cost, costs[robot_id], abs_tol=1e-5):
            return "FAIL"

        total_calculated_cost += calculated_cost

    # Check if all cities are visited exactly once
    if visited_cities != all_cities_set:
        return "FAIL"

    return "CORRECT"

# Example inputs for testing purposes
sample_cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Example output that would be provided by a function implementing the solution logic
# These are just made up tours and may not be optimal or feasible; 
# replace them with actual outputs from a TSP or VRPTW solver for accurate testing
sample_tours = [
    [0, 12, 14, 16, 17, 21, 20, 18, 15, 0],  # Sample tour for robot 0
    [1, 5, 7, 9, 10, 8, 6, 11, 4, 13, 1],    # Sample tour for robot 1
    [2, 19, 2],                               # Sample tour for robot 2
    [3, 3]                                   ,                               # Sample tour for robot 3
]
sample_costs = [
    212.5,  # Made up cost for robot 0's tour
    203.0,  # Made up cost for robot 1's tour
    26.0,   # Made up cost for robot 2's tour
    0.0,    # Made up cost for robot 3's tour
]

# Check if the provided solution meets the specified requirements
print(verify_solution(sample_tours, sample_costs, sample_cities_coordinates))