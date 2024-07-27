import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def validate_solution(tours, city_coordinates, provided_total_cost):
    depot = city_coordinates[0]
    visited_cities = set()
    
    total_calculated_cost = 0.0
    
    for tour in tours:
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            distance = calculate_distance(city_coordinates[from_city], city_coordinates[to_city])
            tour_cost += distance
        
        total_calculated_cost += tour_cost
        
        # Check starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Add visited cities, excluding depot (based on tour excluding the repeated depot at the end)
        visited_cities.update(tour[1:-1])
    
    # Check if all cities except depot are visited exactly once
    if len(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Verify total travel cost calculation
    if abs(total_calculated_cost - provided_total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# City coordinates; index corresponds to city number, with (x, y) coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Provided solution tours and the overall provided calculate cost
solution_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]
]

provided_total_cost = 195.35657055684135

# Check solution correctness
verify_result = validate_solution(solution_tours, city_coordinates, provided_total_cost)
print(verify_topt)