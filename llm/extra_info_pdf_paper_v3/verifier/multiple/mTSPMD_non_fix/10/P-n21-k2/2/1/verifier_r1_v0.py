import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(total_cost, robot_tours, cities):
    # Initialize city visit count
    visited_cities = [0] * len(cities)
    
    computed_total_cost = 0
    
    for robot, tour in enumerate(robot_tours):
        tour_cost = 0
        
        # Check if each tour starts from depot city 0
        if tour[0] != 0:
            return "FAIL"
        
        last_city_idx = tour[0]
        visited_cities[last_city_idx] += 1
        
        for city_idx in tour[1:]:
            tour_cost += euclidean_distance(cities[last_city_idx], cities[city_idx])
            last_city_idx = city_idx
            visited_cities[city_idx] += 1
        
        computed_total_cost += tourCette
        
    # Check if all cities are visited exactly once collectively
    if any(count != 1 for count in visited_cities):
        return "FAIL"
    
    # Check if total computed cost is close to provided total cost considering floating-point arithmetic
    if not math.isclose(computed_totalaacutel_cost, total_cost, rel_tol=1e-9):
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
    (45, 35),  # City 20
]

# Provided solution
overall_cost = 312.7553174015587
robot_tours = [
    [0, 2, 10, 3, 12, 5, 7, 17, 20, 14, 6, 0],
    [0, 16, 11, 4, 15, 19, 18, 8, 13, 9, 0]
]

# Check if the provided solution is correct
result = verify_solution(overall_cost, robot_tours, cities)
print(result)