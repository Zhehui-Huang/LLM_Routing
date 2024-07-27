import math

# Data for the cities and demands
cities_coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

demands = {
    0: 0,
    1: 19,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 31,
    7: 15,
    8: 28,
    9: 14,
    10: 8,
    11: 7,
    12: 14,
    13: 19,
    14: 11,
    15: 26,
    16: 17,
    17: 6,
    18: 15,
}

# Given tours and costs
tours = {
    0: [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    1: [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
}

capacities = {
    0: 160,
    1: 160
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities_coords[city1][0] - cities_coords[city2][0]) ** 2 +
                     (cities_coords[city1][1] - cities_coords[city2][1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Unit tests for requirements
def validate_solution(tours, demands, capacities):
    visited_cities = set()
    for robot_id, tour in tours.items():
        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate total demand in tour
        tour_demand = sum(demands[city] for city in tour if city != 0)
        
        # Check capacity constraint
        if tour_demand > capacities[robot_id]:
            return "FAIL"
        
        # Track visited cities
        visited_cities.update(tour)
        
    # Check if each city is visited exactly once (excluding depot)
    if len(visited_cities) != 19:
        return "FAIL"
    
    return "CORRECT"

# Validate the provided solution and output result
result = validate_solution(tours, demands, capacities)
print(result)