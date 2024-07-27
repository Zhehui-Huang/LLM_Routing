import math

# Constants
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58),
    9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46),
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

num_robots = 8
tours = [
    [0, 21, 16, 1, 0],
    [0, 6, 20, 5, 0],
    [0, 10, 12, 15, 0],
    [0, 2, 7, 22, 0],
    [0, 4, 11, 3, 0],
    [0, 13, 9, 17, 0],
    [0, 14, 8, 18, 0],
    [0, 19, 0]
]

def calc_euclidean_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tours):
    all_visited_cities = set()
    for tour in tours:
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Uniqueness check within tours
        if len(set(tour)) != len(tour):
            return "FAIL"
        
        # Aggregate all visited cities (excluding depot multiple times)
        all_visited_cities.update(tour[1:-1])  # excluding depot at start and end
    
    # Check if all cities are visited exactly once
    if all_visited_cities != set(cities.keys()) - {0}:
        return "FAIL"
    
    # Calculate and validate distances
    max_distance = 0
    for tour in tours:
        tour_distance = 0
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            tour_distance += calc_euclidean_dist(*cities[start_city], *cities[end_city])
        
        # Store the maximum distance found
        if tour_distance > max_distance:
            max_distance = tour_distance
    
    # The solution states the maximum travel cost among all tours
    max_travel_cost_solution = 108.36601172174944
    if abs(max_distance - max_travel_cost_solution) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Test the solution
result = verify_solution(tours)
print(result)