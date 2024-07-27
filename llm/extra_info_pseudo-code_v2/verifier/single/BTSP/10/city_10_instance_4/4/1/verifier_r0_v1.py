import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_robot_tour():
    coordinates = [
        (79, 15),  # Depot
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62)
    ]
    tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    provided_total_cost = 408.41360886151256
    provided_max_distance = 61.68468205316454
    
    def verify_tour_starts_and_ends_at_depot():
        return tour[0] == 0 and tour[-1] == 0
    
    def verify_unique_visit():
        return len(set(tour)) == len(coordinates)
    
    def calculate_total_travel_cost():
        return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    
    def find_max_distance_between_consecutive_cities():
        return max(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    
    if not verify_tour_starts_and_ends_at_depot():
        return "FAIL"
    if not verify_unique_visit():
        return "FAIL"
    
    calculated_total_cost = calculate_total_travel_cost()
    calculated_max_distance = find_max_distance_between_consecutive_cities()
    
    if not math.isclose(calculated_total_cost, provided_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_time, provided_max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Trigger the test function
print(test_robot_tour())