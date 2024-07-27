import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, total_cost, cities, groups):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city per group is visited
    visited = set(tour[1:-1])  # excluding depot which is at start and end
    required_visited = set()
    for group in groups:
        if not visited.intersection(group):
            return "FAIL"
        required_visited.update(visited.intersection(group))
    
    if len(required_visited) != len(groups):
        return "FAIL"
    
    # Calculate the total travel cost and verify its correctness
    calculated_cost = 0
    for i in range(len(tour)-1):
        city_index1, city_index2 = tour[i], tour[i+1]
        calculated_cost += euclidean_distance(cities[city_index1], cities[city_index2])
    
    # Check for approximate equality due to float operations
    if not math.isclose(calculated_L_ost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

def test_verify_tour_and_cost():
    cities = {0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
              5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)}
    groups = [{3, 6}, {5, 8}, {4, 9}, {1, 7}, {2}]
    
    # Example solution details
    tour_solution = [0, 0]
    total_cost_solution = 162.44206978476444

    # Verify the provided solution
    result = verify_tour_and_cost(tour_solution, total_cost_solution, cities, groups)
    print(result)

test_verify_tour_and_cost()