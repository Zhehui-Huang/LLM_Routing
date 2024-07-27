import math

# Define the cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Provided tours for robots
tours = {
    1: [0, 1, 5, 9, 13, 17, 21, 0],
    2: [0, 2, 6, 10, 14, 18, 0],
    3: [0, 3, 7, 11, 15, 19, 0],
    0: [0, 4, 8, 12, 16, 20, 0]
}

# Tour total travel costs provided
tour_costs = {
    1: 196.47266924121885,
    2: 158.6576518784972,
    3: 222.88506864560875,
    0: 161.36303970602805
}

max_travel_cost = 222.88506864560875

def calculate_euclidean_distance(cityA, cityB):
    return math.sqrt((cities[cityA][0] - cities[cityB][0]) ** 2 + (cities[cityA][1] - cities[cityB][1]) ** 2)

def validate_solution(tours, tour_costs, max_provided_cost):
    visited_cities = set()
    max_calculated_cost = 0

    for robot, tour in tours.items():
        # Ensure each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate tour cost and compare with provided
        current_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if not math.isclose(current_cost, tour_costs[robot], abs_tol=1e-6):
            return "FAIL"
        
        # Determine the maximum cost
        max_calculated_cost = max(max_calculated_cost, current_cost)

        # Check if all cities are visited exactly once
        visited_cities.update(tour)

    # Check all non-depot cities are visited      
    if visited_cities != set(cities.keys()):
        return "FAIL"

    # Compare provided max cost with calculated
    if not math.isclose(max_calplemented_cost, max_travel_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"


# Check if the provided tours and costs are valid per the requirements
result = validate_solution(tours, tour_costs, max_travel_cost)
print(result)