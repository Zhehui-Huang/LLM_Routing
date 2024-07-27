def test_tours(tours, city_demands, robot_capacity):
    total_demands_met = [0] * len(city_demands)
    all_tours_start_and_end_at_depot = True
    all_capacity_within_limits = True

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            all_tours_start_and_end_at_depot = False

        capacity_used = 0
        for i in range(1, len(tour) - 1):  # exclude the depot city from capacity calculation
            city_index = tour[i]
            total_demands_met[city_index] += city_demands[city_index]
            capacity_used += city_demands[city_index]
        
        if capacity_used > robot_capacity:
            all_capacity_within_limits = False

    all_demands_met = total_demands_met[1:] == city_demands[1:]  # ignore the depot city demand
    
    if all_tours_start_and_end_at_depot and all_demands_met and all_capacity_within_limits:
        return "CORRECT"
    else:
        return "FAIL"

# Test data setup (example, adjust based on actual solution)
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]  # including the depot city
robot_capacity = 35

# Example robot tours (this should be the actual output from the solution; this is just a placeholder for demonstration)
robot_tours = [
    [0, 1, 4, 0],
    [0, 2, 5, 0],
    [0, 3, 7, 0],
    [0, 6, 0],
    [0, 8, 9, 0],
    [0, 10, 11, 0],
    [0, 12, 13, 0],
    [0, 14, 15, 0],
]

# Running the test
print(test_tours(robot_tours, city_demands, robot_capacity))