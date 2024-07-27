import math

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 38),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Provided tours by robots
tours_by_robots = {
    0: [0, 0],
    1: [0, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
}

def calculate_travel_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        p1 = cities[tour[i-1]]
        p2 = cities[tour[i]]
        cost += math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return cost

def test_solution():
    # Test the number of cities
    if len(cities) != 21:
        return "FAIL"
    
    # Test for two robots
    if len(tours_by_robots) != 2:
        return "FAIL"
    
    # Check if all cities except depot are visited exactly once
    all_cities_visited = set()
    for tour in tours_by_robots.values():
        for city in tour:
            if city != 0:
                all_cities_visited.add(city)
    if sorted(all_cities_visited) != list(range(1, 21)):
        return "FAIL"
    
    # Check if tours start and end at the depot
    for tour in tours_by_robots.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check if each robot returns to the depot and the travel cost estimation
    total_cost = 0
    for robot_id, tour in tours_by_robots.items():
        if tour[0] != tour[-1]:
            return "FAIL"
        computed_cost = calculate_travel_cost(tour)
        if computed_cost != 0:   # Adjust based on expected correct cost calculations
            return "FAIL"
        total_cost += computed_cost

    # Check the all robots visit all cities and the ending condition
    if len(set().union(*[set(tour[1:-1]) for tour in tours_by_robots.values()])) != 20:
        return "FAIL"
    
    return "CORRECT"

# Run the test and print the result
print(test_solution())