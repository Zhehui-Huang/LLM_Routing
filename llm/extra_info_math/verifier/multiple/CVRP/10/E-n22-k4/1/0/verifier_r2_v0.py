import math

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, demands, coordinates, capacity):
    total_demand_in_tours = 0
    overall_cost = 0.0
    visited_cities = set()

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at depot city 0
        
        demand_in_tour = 0
        tour_cost = 0.0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            # Compute travel cost
            distance = calculate_distance(coordinates[city_from], coordinates[city_to])
            tour_cost += distance
            
            if city_to != 0:  # Don't add depot demand
                demand_in_tour += demands[city_to]
                visited_cities.add(city_to)
        
        if demand_in_tour > capacity:
            return "FAIL"  # Demand exceeds capacity
        overall_cost += tour_cost
        total_demand_in_tres = sum(demands[1:]) # Total demand without depot

    if len(visited_cities) != len(demands) - 1:
        return "FAIL"  # Not all cities were visited

    # All conditions satisfied
    return "CORRECT"

# City coordinates mapping to their demands
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# City demands
demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800,
    8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300,
    15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
}

# Given tours
tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 14, 0]
]

# Robot capacity
capacity = 6000

# Verify the solution
result = verify_solution(tours, demands, coordinates, capacity)
print(result)