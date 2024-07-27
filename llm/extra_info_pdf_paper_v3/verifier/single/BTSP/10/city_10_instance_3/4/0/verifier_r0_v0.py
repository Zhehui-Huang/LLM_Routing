import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_cost, max_distance):
    # Coordinates of the cities
    cities = [
        (84, 67),  # city 0
        (74, 40),  # city 1
        (71, 13),  # city 2
        (74, 82),  # city 3
        (97, 28),  # city 4
        (0, 31),   # city 5
        (8, 62),   # city 6
        (74, 56),  # city 7
        (85, 71),  # city 8
        (6, 76)    # city 9
    ]
    
    # Check requirement 2: Visit each city exactly once and return to depot
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL"
    
    # Check requirement 3: Tour should start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculating the distances and checking requirement 1, 4, and 5
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check requirement 4: Total travel cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Check requirement 5: Maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Parameters from the provided solution
tour = [0, 4, 8, 2, 1, 7, 6, 5, 9, 3, 0]
total_travel_cost = 353.67205863560105
max_distance_between_cities = 68.26419266350405

# Test the solution
print(test_solution(tour, total_travel_cost, max_distance_between_cities))