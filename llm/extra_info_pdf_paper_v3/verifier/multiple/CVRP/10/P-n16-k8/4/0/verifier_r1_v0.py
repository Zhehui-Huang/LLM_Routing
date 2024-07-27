import math

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# City demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Tours provided by the robots
tours = [
    [0, 6, 0], [0, 1, 10, 13, 0], [0, 2, 0], [0, 4, 11, 0], 
    [0, 7, 5, 9, 0], [0, 15, 12, 0], [0, 14, 3, 0], [0, 8, 0]
]

# Capacity of each robot
capacity = 35

# Function to calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Verify Requirements
def verify_solution(tours, demands, coordinates, capacity):
    delivered = [0] * len(demands)
    total_cost = 0.0
    all_cities = set(range(1, len(demands)))  # Exclude depot city

    for tour in tours:
        load = 0
        last_city = 0
        tour_cost = 0.0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at the depot
        
        for city in tour[1:-1]:  # Exclude the depot city at start and end
            load += demands[city]
            if load > capacity:
                return "FAIL"  # Capacity exceeded
            tour_cost += calc_distance(coordinates[last_city], coordinates[city])
            last_city = city
            delivered[city] += demands[city]
            all_cities.discard(city)
        
        tour_cost += calc_distance(coordinates[last_city], coordinates[0])  # Return to depot
        total_cost += tour_cost
    
    if any(delivery < demand for delivery, demand in zip(delivered, demands)):
        return "FAIL"  # Not all demands are met
    
    if all_cities:
        return "FAIL"  # Not all cities are visited

    # Outputting the calculated total cost (not required to match exactly due to floating-point arithmetic)
    print(f"Calculated Overall Total Travel Cost: {total_cost}")
    return "CORRECT"

# Run the verification
result = verify_solution(tours, demands, coordinates, capacity)
print(result)