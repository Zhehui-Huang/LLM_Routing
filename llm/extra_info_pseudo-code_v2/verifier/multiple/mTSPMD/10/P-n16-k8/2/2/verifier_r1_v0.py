import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(robots, cities):
    all_visited_cities = set()
    unique_starting_depots = set()
    
    for robot in robots:
        tour = robot['tour']
        travel_cost = robot['cost']
        starting_depot = tour[0]
        ending_deppo = tour[-1]
        
        # Check if each tour starts and ends at the robot's assigned depot
        if starting_depot != ending_deppo:
            return False

        # Check if the tour visits each city exactly once
        if not all(city in tour for city in cities):
            return False
        
        # Accumulate all visited cities
        all_visited_cities.update(tour)
        
        # Check unique starting depots for robots
        unique_starting_depots.add(starting_depot)
        
        # Calculate the travel cost and check correctness
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
        if not np.isclose(calculated_cost, travel_cost, rtol=1e-5):
            return False

    # Verify that all cities are visited exactly once across all robots
    if len(all_visited_cradetys) != len(cities) + len(robots) - 1:  # +1 for multiple depots
        return False

    # Verify that each depot is used correctly
    if len(unique_starting_depots) != len(robots):
        return False

    return True

# Example robots tours solution
robots_info = [
    {"tour": [0, 6, 7, 5, 14, 9, 13, 10, 1, 4, 11, 15, 12, 3, 8, 2, 0], "cost": 172.30},
    {"tour": [1, 10, 4, 11, 15, 12, 3, 8, 13, 9, 7, 2, 6, 0, 5, 14, 1], "cost": 182.79},
    {"tour": [2, 7, 6, 5, 14, 1, 4, 15, 12, 3, 8, 10, 11, 0, 13, 9, 2], "cost": 229.88},
    # Add similar entries for robots 3 to 7
]

# Cities with coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

result = verify_tours(robots_info, city_coordinates)
print("CORRECT" if result else "FAIL")