import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
        7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
        13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
        19: (63, 69), 20: (45, 35)
    }
    robot0_tour = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0]
    robot1_tour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]
    robot0_cost = 315.59626267046633
    robot1_cost = 262.9738751557865
    
    # Check tours both start and end at the depot
    assert robot0_tour[0] == robot0_tour[-1] == 0
    assert robot1_tour[0] == robot1_tour[-1] == 0

    # Check all cities are visited exactly once
    all_cities_visited = set(robot0_tour + robot1_tour)
    assert len(all_cities_visited) == 21  # Total is 21 cities, including the depot city at start and end of each tour

    # Check if city other than depot is visited exactly once
    city_visit_counts = {i: 0 for i in range(1, 21)}
    for city in (robot0_tour + robot1_tour):
        if city != 0:
            city_visit_counts[city] += 1
    assert all(count == 1 for count in city_visit_counts.values())
    
    # Calculate and check costs
    def calculate_tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        return cost
    
    assert abs(calculate_tour_cost(robot0_tour) - robot0_cost) < 1e-5
    assert abs(calculate_tour_cost(robot1_tour) - robot1_cost) < 1e-5
    max_calculated_cost = max(calculate_tour_cost(robot0_tour), calculate_tour_cost(robot1_tour))
    
    # Check the max cost condition
    assert abs(max_calculated_cost - 315.59626267046633) < 1e-5  # Max travel cost is correctly calculated
    
    print("CORRECT")

# Run the test
test_solution()