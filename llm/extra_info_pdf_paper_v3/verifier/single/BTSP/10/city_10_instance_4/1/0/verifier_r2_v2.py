import math

def calculate_euclidean_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def test_tour_verification(tour, reported_total_cost, reported_max_distance):
    """ Function to check the provided TSP solution. """
    # Positions of 10 cities including depot
    positions = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)];
    
    # Check if all cities are visited exactly once, excluding the final return to the start
    if sorted(tour[:-1]) != sorted(range(len(positions))):
        return "FAIL"
    
    # Validate starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Validate total cost and max distance
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-9) or not math.isclose(max_distance, reported_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
provided_tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
reported_total_cost = 337.1694332678818
reported_max_distance = 61.68468205316454

# Run the test
result = test_tour_verification(provided_tour, reported_total_cost, reported_max_distance)
print(result)