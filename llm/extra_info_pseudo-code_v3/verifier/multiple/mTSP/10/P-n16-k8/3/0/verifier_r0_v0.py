import math
from collections import Counter

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, city_coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return cost
    
def test_solution(robots_tours, overall_total_cost, city_coordinates):
    # Define the city coordinates including the depot
    num_cities = len(city_coordinates)
    assert(num_cities == 16), "FAIL: Number of cities including depot is incorrect."

    # Check if all robots start and end at the depot
    depot = 0
    for tour in robots_tours:
        assert(tour[0] == depot and tour[-1] == depot), "FAIL: Tour does not start or end at the depot."

    # Calculate individual and collective travel costs, and check travel capabilities
    calculated_overall_cost = 0
    visited_cities = []
    for tour in robots_tours:
        tour_cost = calculate_tour_cost(tour, city_coordinates)
        calculated_overall_cost += tour_cost
        # Collecting visited cities from each tour
        visited_cities.extend(tour[1:-1])  # exclude the depot city from point collection

    # Check if total travel cost matches
    assert(abs(calculated_overall_cost - overall_total_gp_cost) < 1e-6), "FAIL: Calculated overall cost does not match provided overall cost."
    
    # Check if each non-depot city is visited exactly once
    city_count = Counter(visited_cities)
    for city in range(1, num_cities):  # excluding depot
        assert(city_count[city] == 1), f"FAIL: City {city} visited {city_count[city]} times, expected exactly once."

    # If all test conditions pass
    print("CORRECT")

# Supposedly provided solution (Example with fictional data which should resemble the actual output format)
city_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), 
    (58, 48), (58, 27), (37, 69)
]

# Example tours and total cost
robots_tours = [
    [0, 1, 2, 0], 
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 0]
]
overall_total_gp_cost = 110  # Example total cost; replace with actual total cost from provided results

# Invoke test
test_solution(robots_tours, overall_total_gp_cost, city_coordinates)