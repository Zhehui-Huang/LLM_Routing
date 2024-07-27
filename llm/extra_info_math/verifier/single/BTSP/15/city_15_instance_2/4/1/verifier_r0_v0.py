import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour(tour, total_cost, max_distance):
    # Cities coordinates
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
        (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
        (56, 58), (72, 43), (6, 99)
    ]
    
    # Requirement 1: Tour must start and end at depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Every city visited once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Compute total and max distances explicitly
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check calculated total cost and max_distance
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution values
tour = [0, 6, 2, 12, 10, 9, 7, 13, 3, 5, 4, 11, 8, 14, 1, 0]
total_travel_cost = 366.18016548742736
maximum_distance = 39.05124837953327

# Running the test
result = test_tour(tour, total_travel_cost, maximum_distance)
print(result)