import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution():
    # Provided coordinates for each city indexed by city number
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # Solution to test
    proposed_tour = [0, 4, 3, 1, 5, 7, 8, 9, 0]
    proposed_cost = 292.36
    
    # Check if tour starts and ends with the depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes exactly 8 cities
    if len(set(proposed_tour)) != 9:  # including city 0 twice
        return "FAIL"
    
    # Calculate the actual cost of the proposed tour
    actual_cost = calculate_total_travel_cost(proposed_tour, cities)
    
    # Allow some tolerance for floating point arithmetic
    if not math.isclose(proposed_cost, actual_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Call the test function
print(test_solution())