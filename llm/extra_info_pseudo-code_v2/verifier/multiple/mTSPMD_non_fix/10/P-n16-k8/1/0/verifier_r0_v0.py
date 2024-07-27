import math

def calc_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution():
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
    }
    
    tours = {
        0: [0, 5, 0],
        1: [0, 13, 0],
        2: [0, 15, 0],
        3: [0, 14, 0],
        4: [0, 9, 0],
        5: [0, 12, 0],
        6: [0, 8, 0],
        7: [0, 6, 4, 1, 11, 2, 3, 7, 10, 0]
    }

    reported_costs = [46.17, 58.24, 59.67, 61.74, 64.12, 59.93, 64.90, 173.32]
    calculated_costs = []

    # Verify all cities are visited exactly once
    all_visited_cities = set()
    for robot, tour in tours.items():
        # Exclude the starting and ending depot from checking the unique visit
        visited_cities = set(tour[1:-1])  
        all_visited_cities.update(visited_cities)

        # Calculate tour travel cost
        cost = 0
        for i in range(len(tour) - 1):
            cost += calc_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        calculated_costs.append(round(cost, 2))

    # Check if all cities are visited
    if len(all_visited_cities) != 16:
        return "FAIL"

    # Check if cost calculations match
    for reported, calculated in zip(reported_costs, calculated_costs):
        if reported != calculated:
            return "FAIL"
    
    return "CORRECT"

# Output the result of the verification
print(verify_solution())