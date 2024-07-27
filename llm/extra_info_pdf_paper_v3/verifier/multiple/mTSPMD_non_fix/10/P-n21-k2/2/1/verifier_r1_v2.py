import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(total_cost, robot_tours, cities):
    # Initialize city visit count
    visited_cities = [0] * len(cities)
    
    computed_total_cost = 0
    
    for tour in robot_tours:
        # Initiate the city index from the tour's start
        last_city_idx = tour[0]
        if tour[0] != 0:  # Check that tour starts at depot 0
            return "FAIL"

        # Calculate the tour cost and update city visits
        for next_city_idx in tour[1:]:
            tour_cost = euclidean_distance(cities[last_city_idx], cities[next_city_idx])
            computed_total_cost += tour_cost
            last_city_idx = next_city_idx
            visited_cities[next_city_idx] += 1
        visited_cities[tour[0]] += 1  # Increase count for the depot start
        
    # Ensure all cities are visited exactly once (since each should be in one tour)
    if any(count != 1 for count in visited_cities):
        return "FAIL"
    
    # Check total cost matches
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City Coordinates
cities = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 49),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69),  # City 15
    (38, 46),  # City 16
    (61, 33),  # City 17
    (62, 63),  # City 18
    (63, 69),  # City 19
    (45, 35)   # City 20
]

# Provided solution
overall_total_cost = 312.7553174015587
robot_tours = [
    [0, 2, 10, 3, 12, 5, 7, 17, 20, 14, 6, 0],
    [0, 16, 11, 4, 15, 19, 18, 8, 13, 9, 0]
]

# Verify the solution
result = verify_solution(overall_total_cost, robot_tours, cities)
print(result)