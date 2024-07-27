import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Provided solution
tour = [0, 8, 10, 1, 11, 14, 12, 9, 4, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost_provided = 363.59
maximum_distance_provided = 63.60

# City coordinates
cities = {
    0: (9, 93),  1: (8, 51),  2: (74, 99),  3: (78, 50),
    4: (21, 23),  5: (88, 59),  6: (79, 77),  7: (63, 23),
    8: (19, 76),  9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21),  13: (60, 55), 14: (4, 39)
}

def unit_test_tour_requirements(tour, cities, max_distance_provided, total_cost_provided):
    # Requirement 1: Start and end at Depot city (index 0).
    start_end_correct = tour[0] == 0 and tour[-1] == 0
    
    # Requirement 2: Every city visited exactly once, except the depot (twice).
    cities_visited = set(tour)
    all_cities_checked = len(cities_visited) == len(cities) and all(cities[count] == 1 or (count == 0 and cities[count] == 2) for count in cities_visited)
    
    # Calculate distances and total cost
    max_distance_calculated = 0
    total_cost_calculated = 0
    for i in range(len(tour)-1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        dist = calculate_distance(x1, y1, x2, y2)
        total_cost_calculated += dist
        max_distance_calculated = max(max_distance_calculated, dist)
    
    # Requirement 3: Check for distance calculations
    distance_correct = abs(max_distance_calculated - max_distance_provided) < 1e-2
    total_cost_correct = abs(total_cost_calculated - total_cost_provided) < 1e-2
    
    if start_end_correct and all_cities_checked and distance_correct and total_cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Running the test
result = unit_test_tour_requirements(tour, cities, maximum_distance_provided, total_travel_cost_provided)
print(result)