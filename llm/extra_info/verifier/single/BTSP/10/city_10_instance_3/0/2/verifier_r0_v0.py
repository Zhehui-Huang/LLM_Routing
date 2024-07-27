import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost, max_distance):
    # Validate Requirement 1 - Check if all cities are visited once and starts/ends at depot
    if sorted(tour) != list(range(len(cities))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
        
    # Validate Requirement 3 - Using Euclidean formula for distance calculations
    # Requirement already implemented in calculate_distance function
  
    # Validate Requirement 2 - Check if total cost and max distance are correct
    if not math.isclose(calculated_total range(10)])

    # Test Case
    verify_result = verify_tour(cities, tour, total_travel_cost, max_distance_consecutive_cities)
    print(verify_result)

if __name__ == "__main__":
    main()