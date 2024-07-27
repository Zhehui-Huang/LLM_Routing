import math

def calculate_distance(c1, c2):
    """ Calculate the Euclidean distance between two coordinates. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution():
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69)
    }
    
    robots_tours = {
        0: [0, 0, 0], 1: [1, 1, 1], 2: [2, 2, 2], 3: [3, 3, 3], 4: [4, 4, 4],
        5: [5, 5, 5], 6: [7, 7, 7], 7: [11, 14, 11]
    }
    
    robots_tours_costs = {
        0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 102.80077820717118
    }
    
    total_given_cost = 102.80077820717118

    city_visit_count = {i: 0 for i in range(16)}
    total_calculated_cost = 0.0

    # Check robot tours for validity and calculate cumulative cost
    for robot_id, tour in robots_tours.items():
        last_city = tour[0]
        city_visit_count[last_city] += 1  # Count the starting city
        
        # Calculate cumulative tour cost
        tour_cost = 0.0
        for city in tour[1:]:
            if city not in cities_coordinates:
                return "FAIL"
            current_cost = calculate_distance(cities_coordinates[last_city], cities_coordinates[city])
            tour_cost += current_cost
            last_city = city
            city_visit_count[city] += 1
        
        # Check individual calculated cost against given cost
        if abs(tour_cost - robots_tours_costs[robot_id]) > 0.0001:
            return "FAIL"
        
        total_calculated_cost += tour_cost

    # Ensure every city is visited exactly once
    if any(count != 1 for count in city_visit_count.values()):
        return "FAIL"
    
    # Check total aggregated cost
    if abs(total_calculated_cost - total_given_patchithe_er_cost) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)