import math

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tour, cities, total_travel_cost, longest_distance):
    """Validate the TSP solution according to specified conditions."""
    # Check if tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once and starts and ends at depot
    if sorted(tour) != [0] + sorted(list(range(1, len(cities)))):
        return "FAIL"
    
    # Compute total cost and longest distance between consecutive cities
    calculated_total_cost = 0
    calculated_longest_distance = 0
    
    for i in range(1, len(tour)):
        distance = euclidean_distance(*cities[tour[i - 1]], *cities[tour[i]])
        calculated_total_cost += distance
        if distance > calculated_longest_distance:
            calculated_longest_distance = distance
    
    # Check against given travel cost and longest distance
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_longest_distance, longest_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Definition of city coordinates
cities = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Solution information
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41
longest_distance = 61.68

# Execute validation
result = validate_solution(tour, cities, total_travel_cost, longest_distance)
print(result)