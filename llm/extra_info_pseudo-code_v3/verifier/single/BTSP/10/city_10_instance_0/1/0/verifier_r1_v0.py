import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour():
    # City coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Provided solution details
    tour = [0, 5, 0]
    total_travel_cost = 8.48528137423857
    max_distance_between_consecutive_cities = 4.242640687119285
    
    # Check that tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that each city except depot is visited exactly once
    visited = set(tour)
    if visited != set(range(len(cities))):
        return "FAIL"
    
    # Calculate actual total travel cost and max distance between consecutive cities
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour)-1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist
    
    # Compare provided and calculated values
    if not math.isclose(total_travel_cost, actual_total_distribution, rel_tol=1e-9):
        return "FAIL"
    
    if not math.isclose(max_distance_between_consecutive_cities, actual_max_distance_distribution, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the verification function
print(verify_tour())