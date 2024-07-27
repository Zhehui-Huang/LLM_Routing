import math

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost, max_distance):
    # Corrected coordinates of the cities with index matching their respective order
    cities = [(30, 56), (53, 42), (1, 95), (25, 61),   (69, 57), 
              (6, 58),   (12, 84), (72, 77), (98, 95), (11, 0), 
              (61, 25), (52, 0),  (60, 95), (10, 94),  (96, 73), 
              (14, 47), (18, 16), (4, 43),  (53, 76),  (19, 72)]

    # Initialize sum of travel costs and track maximum distance found
    calculated_cost = 0
    calculated_max_distance = 0

    # Validate the tour and compute costs
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check for requirements fulfillment
    if len(set(tour)) != len(cities) or tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL"
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-4):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 1, 7, 14, 8, 12, 18, 4, 10, 11, 9, 16, 17, 15, 3, 5, 2, 13, 6, 19, 0]
total_travel_cost = 482.40
maximum_distance_between_cities = 41.00

# Check if the solution meets the specifications
result = check_solution(tour, total_travel_cost, maximum_distance_between_cities)
print(result)