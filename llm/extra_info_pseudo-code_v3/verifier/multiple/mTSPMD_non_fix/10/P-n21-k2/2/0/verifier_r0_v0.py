import math

# Given data and solution
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 63), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]
robot_tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2],
    [1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19]
]
reported_travel_costs = [187.82, 205.81]
reported_total_cost = 393.64

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return round(total_cost, 2)

def test_solution():
    # Test if two depots are considered and each robot starts at Depot 0
    assert robot_tours[0][0] == 0 and robot_tours[1][0] == 1, "Depots are not correctly used as start points."
    
    # All cities must be visited exactly once
    all_visited_cities = sorted(robot_tours[0] + robot_tours[1])
    all_cities = list(range(21))
    assert all_visited_cities == all_cities, "Some cities are not visited or are visited more than once."
    
    # Each tour's travel cost must be correct
    calculated_costs = [calculate_tour_cost(tour, cities_coordinates) for tour in robot_tours]
    for reported, calculated in zip(reported_travel_costs, calculated_costs):
        assert math.isclose(reported, calculated, abs_tol=0.05), "Travel costs do not match calculations."
    
    # Overall total cost must be correct
    calculated_total_cost = sum(calculated_costs)
    assert math.isclose(reported_total_cost, calculated_total_energy, abs_tol=0.05), "Total travel costs do not match calculations."
    
    return "CORRECT"

# Run the test
test_result = test_solution()
print(test_result)