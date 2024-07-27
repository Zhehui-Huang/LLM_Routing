import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours_and_costs():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    
    tours = [
        [0, 8, 0],
        [1, 9, 1],
        [2, 14, 2],
        [3, 11, 3],
        [4, 13, 4],
        [5, 15, 5],
        [6, 10, 6],
        [7, 12, 7]
    ]
    
    provided_costs = [64.90, 53.85, 47.54, 50.64, 60.83, 78.00, 32.00, 55.03]
    calculated_costs = []
    overall_cost = 0

    # Check all cities are visited exactly once except depots where each appears twice
    all_cities = sum(tours, [])
    visited_counts = {city: all_cities.count(city) for city in range(len(coordinates))}
    
    for idx, city_count in visited_counts.items():
        if idx < 8:  # depot cities
            if city_count != 2:
                return "FAIL"
        else:
            if city_count != 1:
                return "FAIL"
    
    # Calculate costs and verify against provided costs
    for tour, provided_cost in zip(tours, provided_costs):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        
        calculated_costs.append(round(tour_cost, 2))
        overall_cost += tour_cost

    # Comparing provided costs with calculated costs
    if any(abs(provided - calculated) > 0.1 for provided, calculated in zip(provided_costs, calculated_costs)):
        return "FAIL"

    # If sum of individual costs matches the provided overall cost reasonably
    provided_overall_cost = 442.78
    if abs(provided_overall_cost - round(overall_cost, 2)) > 0.1:
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = verify_tours_and_costs()
print(result)