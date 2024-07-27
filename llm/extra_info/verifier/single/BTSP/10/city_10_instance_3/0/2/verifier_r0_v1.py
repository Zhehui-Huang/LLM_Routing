import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost, max_distance):
    # Validate Requirement 1 - Check if all cities are visited exactly once and tour starts/ends at depot 0
    if sorted(tour[:-1]) != sorted(range(len(cities))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate travel costs and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Validate Requirement 2 - Check if max_distance matches
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"

    # Validate Requirement 3 - Check if total_cost matches
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

def main():
    # Coordinates of cities
    cities = [
        (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), 
        (8, 62), (74, 56), (85, 71), (6, 76)
    ]

    # Given solution
    tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
    total_travel_cost = 315.5597914831042
    max_distance_consecutive_cities = 78.5175139698144

    # Test Case
    verify_result = verify_tour(cities, tour, total_travel_cost, max_distance_consecutive_cities)
    print(verify_result)

if __name__ == "__main__":
    main()