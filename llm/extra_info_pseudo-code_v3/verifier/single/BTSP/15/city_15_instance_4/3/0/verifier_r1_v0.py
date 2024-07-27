import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # [Requirement 1] Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visits each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != 16 or len(tour) != 16:  # Includes the return to the depot city
        return "FAIL"

    # [Requirement 5] Tour format
    if not all(isinstance(city, int) for city in tour):
        return "FAIL"

    # Calculate the travel cost and check max distance
    calculated_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Requirement 6] Total travel cost
    if not math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 7] Max distance between consecutive cities
    if not math.isclose(max_distance, calculated_max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test data provided
tour = [0, 14, 13, 10, 11, 4, 12, 5, 2, 7, 9, 1, 8, 6, 3, 0]
total_travel_cost = 427.8319143703631
max_distance = 35.85684178029928

# Verify the solution
result = verify_solution(tour, total_travel_rent_cost, max_distance)
print(result)  # This should output "CORRECT" if all tests are satisfied.