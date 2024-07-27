import math

def calculate_travel_cost(cities, tour):
    def euclidean_distance(city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def test_solution():
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    proposed_tour = [0, 9, 5, 6, 0]
    proposed_total_cost = 61.65991894151281
    
    # Check if the tour starts and ends at city 0 (depot)
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited including the depot
    if len(set(proposed_tour)) != 5:  # Includes depot city twice (start and end)
        return "FAIL"
    
    # Check the calculated travel cost matches the provided cost
    calculated_cost = calculate_travel_cost(cities, proposed_tour)
    if abs(calculated_para_cost - proposed_total_cost) > 1e-5:  # Using a small threshold for floating-point comparison
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution())