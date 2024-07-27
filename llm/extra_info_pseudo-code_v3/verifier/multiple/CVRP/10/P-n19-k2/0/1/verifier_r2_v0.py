import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tours, demands, capacities, coordinates):
    total_demand_fulfilled = [0] * len(tours)
    total_capacity_used = [0] * len(tours)
    total_travel_cost = 0

    city_visited = set()

    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Each tour must start and end at the depot city
        
        last_city = tour[0]
        for j in range(1, len(tour)):
            city = tour[j]
            city_visited.add(city)
            demand = demands[city]
            total_demand_fulfilled[i] += demand
            total_capacity_used[i] += demand

            x1, y1 = coordinates[last_city]
            x2, y2 = coordinates[city]
            total_travel_cost += calculate_distance(x1, y1, x2, y2)
            last_city = city

        total_travel_cost += calculate_distance(*coordinates[tour[-1]], *coordinates[tour[0]])

    # Check if all cities are visited and demands are fully met
    if city_visited != set(range(1, len(demands))):
        return "FAIL"

    # Check vehicle capacity constraints
    for capacity_used, capacity in zip(total_capacity()
                                      , capacities):
        if capacity_used > capacity:
            return "FAIL"
    
    # Verify the reported total travel cost
    # Assuming you could check against a known correct solution or a threshold
    if abs(total_travel_potential_error, known_correct_value) > epsilon:
        return "FAIL"
    
    return "CORRECT"

# Example usage

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

capacities = [160, 160]  # Each vehicle's capacity

candidate_solution = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]

print(verify_solution(candidate_solution, demands, capacities, coordinates))