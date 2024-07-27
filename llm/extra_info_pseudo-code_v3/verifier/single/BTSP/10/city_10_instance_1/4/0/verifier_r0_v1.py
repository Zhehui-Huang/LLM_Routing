import math

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_solution(tour, city_coords):
    """Validate the tour against provided requirements."""
    total_cost = 0
    max_distance = 0
    visited = set(tour)
    
    # Check if all cities are visited exactly once and start/end at depot city 0
    if len(visited) != len(city_coords) or len(tour) != len(city_coords) + 1:
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total cost and maximum distance between consecutive cities
    for i in range(len(tour) - 1):
        city_index_from = tour[i]
        city_index_to = tour[i + 1]
        distance = euclidean_substance(city_coords[city_index_from], city_coords[city_index_to])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check provided tour cost and max distance with calculated values
    expected_cost = 291.41
    expected_max_distance = 56.61

    if math.isclose(total_cost, expected_cost, rel_tol=1e-2) and math.isclose(max_distance, expected_max_distance, rel_tol=1e-2):
        return "CORRECT"
    else:
        print(f"Calculated cost: {total_cost:.2f}, Expected cost: {expected_cost:.2f}")
        print(f"Calculated max_distance: {max_distance:.2f}, Expected max_distance: {expected_max_distance:.2f}")
        return "FAIL"

# Dataset based on problem statement
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
cities_coordinates = {
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

result = validate_solution(tour, cities_coordinates)
print(result)