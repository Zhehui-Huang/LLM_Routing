import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.hypot(city2[0] - city1[0], city2[1] - city1[1])

def verify_tour(tour):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Requirement 1: Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if every city is visited exactly once (excluding the depot appearing twice)
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city_index1, city_index2 = tour[i], tour[i+1]
        distance = calculate_distance(cities[city_index1], cities[cityIndex2])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Print details if needed
    # print(f"Total travel cost calculated: {total_travel_cost}")
    # print(f"Max distance between consecutive cities calculated: {max_distance}")
    
    # Currently no strict value checks for Requirement 3 in the requirements
        
    return "CORRECT"

# Given solution that needs to be verified
solution_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
result = verify_tour(solution_tour)
print(result)