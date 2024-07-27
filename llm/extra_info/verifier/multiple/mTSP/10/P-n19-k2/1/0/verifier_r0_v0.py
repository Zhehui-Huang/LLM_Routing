import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
        (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    tours = {
        0: [0, 1, 7, 5, 13, 15, 9, 3, 17, 11, 0],
        1: [0, 6, 18, 2, 10, 12, 14, 4, 8, 16, 0]
    }
    
    expected_costs = {
        0: 165.1656694842428,
        1: 141.72560334081322
    }
    
    total_cost_calculated = 0
    
    # Check each robot
    for robot in tours:
        tour = tours[robot]
        expected_cost = expected_costs[robot]
        
        # Check the tour starts and ends at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check the cost calculation
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        if not math.isclose(tour_cost, expected_cost, rel_tol=1e-5):
            return "FAIL"
        
        total_cost_calputed += tour_cost
        
        # Ensure no city is visited twice excluding the depot
        unique_cities = set(tour[1:-1])
        if len(unique_cities) != len(tour[1:-1]):
            return "FAIL"
    
    # Check if all cities except the depot were visited
    all_cities_visited = set()
    for tour in tours.values():
        all_cities_visited.update(tour[1:-1])
    
    if len(all_cities_visited) != len(cities) - 1:  # minus one for the depot
        return "FAIL"
    
    # Check the overall cost
    expected_total_cost = 306.89127282505603
    if not math.isclose(total_cost_calculated, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"


# Run the unit test
result = test_solution()
print(result)