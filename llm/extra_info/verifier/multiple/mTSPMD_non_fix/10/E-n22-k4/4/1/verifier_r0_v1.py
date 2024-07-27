import math

# Define the cities coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided solution
solution_tours = [
    [0, 14, 17, 20, 10, 5, 4],
    [0, 16, 19, 21, 9, 2],
    [0, 12, 15, 18, 7, 1],
    [0, 13, 11, 8, 6, 3]
]

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Validate the complete coverage and uniqueness of city visits
def test_unique_city_coverage():
    all_visited = sum(solution_tours, [])
    return len(set(all_visited)) == 22 and len(all_visited) == 22

# Validate that each tour starts from the depot 0
def test_correct_start_for_all_tours():
    return all(tour[0] == 0 for tour in solution_tours)

# Validate individual and total distances
def test_distances():
    expected_distances = [137.505, 127.275, 111.480, 75.136]
    calculated_distances = []
    for tour in solution_tours:
        tour_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        calculated_distances.append(tour_distance)
    
    # Compare distances allowing small floating point discrepancies
    if not all(abs(calculated_distances[i] - expected_distances[i]) < 0.001 for i in range(len(calculated_distances))):
        return False

    # Check the overall distance
    total_calculated_distance = sum(calculated_distances)
    total_expected_distance = sum(expected_distances)
    if not (450 < total_calculated_distance < 452): # Approximate expected total
        return False

    return True

# Running tests
def run_tests():
    if not test_unique_city_coverage():
        return "FAIL: Cities not uniquely or completely covered."
    
    if not test_correct_start_for_all_tours():
        return "FAIL: Not all tours start from the designated depot."

    if not test_distances():
        return "FAIL: Distance calculations do not match the expected results."

    return "CORRECT"

# Evaluate the tests
print(run_tests())