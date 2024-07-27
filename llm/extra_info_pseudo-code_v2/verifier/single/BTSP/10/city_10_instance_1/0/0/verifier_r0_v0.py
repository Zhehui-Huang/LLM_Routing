def verify_solution(tour, total_travel_cost, max_distance):
    # Coordinates of cities indexed from 0 to 9
    coordinates = [(53, 68), (75, 11), (91, 95), (22, 80),
                   (18, 63), (54, 91), (70, 14), (97, 44),
                   (17, 69), (95, 89)]
    
    import math
    
    # Function to calculate euclidean distance between two cities
    def euclidean_distance(city1, city2):
        return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                         (coordinates[city1][1] - coordinates[city2][1]) ** 2)
    
    # [Requirement 1] Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once (ignoring the depot city revisited)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(tour[1:-1]) or len(unique_cities) != 9:
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance
    calculated_total_travel_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        calculated_total_travel_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the total travel cost matches
    if not math.isclose(total_travel_cost, calculated_total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 3] Check if the longest distance between two consecutive cities matches
    if not math.isclose(max_distance, calculated_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Test input from your solution example
tour = [0, 1, 6, 1, 0]
total_travel_cost = 11.661903789690601
max_distance_between_cities = 5.830951894845301

# Verify the solution
result = verify_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)