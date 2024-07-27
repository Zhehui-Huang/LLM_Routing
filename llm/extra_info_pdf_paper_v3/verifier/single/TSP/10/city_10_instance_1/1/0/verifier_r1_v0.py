import math

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def validate_tour(tour, positions, expected_cost):
    # Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    visited_cities = set(tour)
    if len(visited_cities) != len(positions) or len(tour) != len(positions) + 1:
        return "FAIL"
    
    # Check if the travel cost is correctly calculated
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(positions[tour[i]], positions[tour[i+1]])
    
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities positions
positions = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution
tour_solution = [0, 3, 8, 4, 6, 1, 7, 9, 2, 5, 0]
total_travel_cost = 280.8414894850646

# Validate and output the result
result = validate_tour(tour_solution, positions, total_travel_cost)
print(result)