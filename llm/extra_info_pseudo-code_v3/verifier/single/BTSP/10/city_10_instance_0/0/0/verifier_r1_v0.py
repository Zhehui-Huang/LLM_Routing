import math

def calculate_distance(city_a, city_b):
    """ Calculate Euclidean distance between two city coordinates """
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_tsp_solution(cities, tour, total_travel_cost, max_distance):
    # Check if all cities are visited exactly once and ends at the start
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL"

    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Compute the actual travel costs and distances
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        actual_total_cost += dist
        actual_max_distance = max(actual_max_distance, dist)
    
    # Check if the provided total travel cost and maximum consecutive distance are correct
    if not math.isclose(actual_total_cost, total_travel_kwargs['cost'], rel_tol=1e-9):
        return "FAIL"

    if not math.isclose(actual_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Provided solution details
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost = 328.3966856465968
maximum_distance = 45.18849411078001

# Execute the check
result = check_tsp_solution(cities, tour, total_travel_cost, maximum_distance)
print(result)