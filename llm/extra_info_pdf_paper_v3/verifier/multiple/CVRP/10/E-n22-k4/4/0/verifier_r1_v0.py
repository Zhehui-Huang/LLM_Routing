import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_solution(tours, demands, capacities, coordinates):
    num_robots = 4
    total_capacity_violated = False
    all_cities_covered = set(range(1, 22))
    visited_cities = set()
    overall_travel_cost = 0
    
    if len(tours) != num_robots:
        return "FAIL: Number of tours does not match number of robots."

    for tour_index, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at the depot city."
        
        tour_demand = 0
        tour_cost = 0
        prev_city = tour[0]
        
        for city in tour[1:]:
            visited_cities.add(city)
            tour_demand += demands[city]
            tour_cost += euclidean_distance(coordinates[prev_city], coordinates[city])
            prev_city = city
        
        # Add distance back to depot
        tour_cost += euclidean_distance(coordinates[prev_city], coordinates[0])
        
        overall_travel_cost += tour_cost
        
        if tour_demand > capacities[tour_index]:
            total_capacity_violated = True
        
    if total_capacity_violated:
        return "FAIL: Capacity constraints violated."
    
    if visited_cities != all_cities_covered:
        return "FAIL: Not all cities' demands have been met."
    
    return f"CORRECT: Overall Total Travel Cost = {overall_travel_cost}"

coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}
demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100,
    9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100,
    17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
}
capacities = [6000, 6000, 6000, 6000]

tours = [
    [0, 19, 5, 4, 0],
    [0, 16, 20, 12, 3, 0],
    [0, 13, 11, 1, 17, 15, 9, 0],
    [0, 18, 7, 2, 21, 10, 6, 14, 8, 0]
]

result = verify_solution(tours, demands, capacities, coordinates)
print(result)