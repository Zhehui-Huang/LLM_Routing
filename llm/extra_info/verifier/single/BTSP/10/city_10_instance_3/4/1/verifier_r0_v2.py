import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, provided_cost, provided_max_distance):
    # Coordinates for each city including the depot
    cities = [
        (84, 67),  # City 0 - Depot
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]
    
    # Check Requirement 1 & 4: Tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city is visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) - 1 != len(cities):
        return "FAIL"
    
    total_cost = 0
    max_distance = 0
    
    # Calculate the travel cost and find the maximum distance
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    # Check Requirement 5: Provided total cost matches calculated cost
    if not math.isclose(total_cost, provided_cost, abs_tol=0.1):
        return "FAIL"
    
    # Check Requirement 6: Provided maximum distance matches the calculated max distance
    if not math.isclose(max_distance, provided_max_distance, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
tour_solution = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
total_travel_cost = 345.92
max_distance_between_cnodes = 68.26

test_result = test_solution(tour_solution, total_travel_cost, max_distance_between_cities)
print(test_result)