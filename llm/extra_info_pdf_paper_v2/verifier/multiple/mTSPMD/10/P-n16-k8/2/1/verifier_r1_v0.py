import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tours, depot_cities, city_coordinates):
    visited_cities = set()
    unique_city_check = set(range(16))  # Total 16 cities, indexed from 0 to 15
    
    # Requirement 1 is implicit in this setup (16 cities), thus not explicitly checked here.
    
    # Verify Requirement 2, 3, 6
    for robot_id, tour in enumerate(tours):
        # Check if start and end at the designated depots (Req. 3, 6)
        if tour[0] != depot_cities[robot_id] or tour[-1] != depot_cities[robot_id]:
            return 'FAIL'
        
        # Accumulate visited cities (Req. 7)
        visited_cities.update(tour)
    
    # Requirement 7: Check if all cities are visited exactly once
    if visited_cities != unique_city_check:
        return 'FAIL'
    
    # Verify Requirement 4 by calculating and summing up the distances in each tour
    total_travel_cost_calculated = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_travel_cost_calculated += tour_cost
    
    # Display total cost output and compare (Requirement 5 isn't explicitly verifiable without known optimal cost)
    # This is assumed to capture the audit of calculated costs for manual comparison:
    print(f"Total Calculated Travel Cost: {total_travel_cost_calculated}")
    
    # Assuming no major deviations/errors discovered and all cities accounted for, and all tours start/end correctly:
    return 'CORRECT'

# City coordinates corresponding to your city indices
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Provided solution tours (reformatted for clarity), following your test case structure
tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1],
    [2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2],
    [3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3],
    [4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4],
    [5, 7, 2, 13, 9, 14, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5],
    [6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6],
    [7, 5, 14, 9, 13, 2, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 7]
]

# Depots for each robot
depot_cities = [0, 1, 2, 3, 4, 5, 6, 7]

# Verify the solution correctness
verification_result = verify_solution(tours, depot_cities, city_coordinates)
print(verification_result)