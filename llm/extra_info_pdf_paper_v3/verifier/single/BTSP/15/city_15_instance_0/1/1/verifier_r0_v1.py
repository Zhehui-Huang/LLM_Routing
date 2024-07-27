import numpy as np

def calculate_euclidean_distance(city1, city2):
    """
    Compute the Euclidean distance between two city coordinates.
    """
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost, max_distance):
    """
    Function to test the solution against the requirements.
    """
    # City Coordinates
    cities = {
        0: (9, 93),
        8: (19, 76),
        10: (19, 65)
    }
    
    # [Requirement 1] Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once
    if sorted(set(tour)) != sorted([0, 8, 10]):
        return "FAIL"
    
    # [Requirement 3] Verify the max distance
    computed_max_distance = 0
    distances = []
    for i in range(len(tour) - 1):
        city_idx_1 = tour[i]
        city_idx_2 = tour[i + 1]
        distance = calculate_euclidean_distance(cities[city_idx_1], cities[city_idx_2])
        distances.append(distance)
        computed_max_distance = max(computed_max_distance, distance)
    
    if not np.isclose(computed_max_distance, max_distance):
        return "FAIL"
  
    # Verify the total cost by summing calculated distances
    computed_total_cost = np.sum(distances)
    if not np.isclose(computed_total_cost, total_cost):
        return "FAIL"

    return "CORRECT"

# Provided fixed solution
tour = [0, 8, 10, 0]
total_travel_cost = 60.45522041795303
maximum_distance_between_cities = 29.732137494637012

# Run the test
result = test_solution(tour, total_travel_cost, maximum_distance_between_cities)
print(result)