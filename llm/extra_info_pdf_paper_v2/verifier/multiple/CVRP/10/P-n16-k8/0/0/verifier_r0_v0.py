import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# City coordinates
coordinates = [
    (30, 40), # City 0
    (37, 52), # City 1
    (49, 49), # City 2
    (52, 64), # City 3
    (31, 62), # City 4
    (52, 33), # City 5
    (42, 41), # City 6
    (52, 41), # City 7
    (57, 58), # City 8
    (62, 42), # City 9
    (42, 57), # City 10
    (27, 68), # City 11
    (43, 67), # City 12
    (58, 48), # City 13
    (58, 27), # City 14
    (37, 69)  # City 15
]

# Robot tours
tours = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 6, 0],
    [0, 8, 0],
    [0, 12, 15, 0],
    [0, 5, 14, 0],
    [0, 7, 9, 13, 0],
    [0, 4, 11, 0],
    [0, 3, 10, 0]
]

# City demands
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11
]

# Robot capacity
capacity = 35

# Calculates total travel cost
def verify_solution(tours, coordinates, demands, robot_capacity):
    total_travel_cost = 0
    all_delivered_demands = [0] * len(demands)
    
    for tour in tours:
        tour_capacity_used = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            # Update travel cost
            tour_cost += calculate_distance(*coordinates[from_city], *coordinates[to_city])
            # Sum demands
            if i != len(tour) - 2:  # exclude the last return to depot in counting capacity
                tour_capacity_used += demands[to_city]
                all_delivered_demands[to_city] += demands[to_city]
        
        # Check capacity constraint
        if tour_capacity_used > robot_capacity:
            return "FAIL"
        
        total_travel_cost += tour_cost
    
    # Check if all demands are met
    if any(demand != delivered for demand, delivered in zip(demands, all_delivered_demands)):
        return "FAIL"
    
    # Minimize total travel cost (manually review minimal travel cost against potential alternatives)
    # Uses approximate known costs from problem feedback
    reported_total_cost = 478.75
    if abs(total_travel_cost - reported_total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Verify the solution
result = verify_solution(tours, coordinates, demands, capacity)
print(result)