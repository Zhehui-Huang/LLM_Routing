def test_tsp_solution(tour, total_travel_cost, cities):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once (excluding the depot city revisited at the end)
    visited_cities = set(tour[1:-1])  # Collect all cities visited (excluding start and end depot)
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Requirement 3: Output both tour and total travel cost
    if not isinstance(tour, list) or not isinstance(total_travel_cost, (int, float)):
        return "FAIL"
    
    return "CORRECT"

# Example data for unit test
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
# Hypothetical solution output for checking, assuming this data format
example_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
example_total_travel_cost = 200

# Running the test
result = test_tsp_solution(example_tour, example_total_travel_cost, cities)
print(result)