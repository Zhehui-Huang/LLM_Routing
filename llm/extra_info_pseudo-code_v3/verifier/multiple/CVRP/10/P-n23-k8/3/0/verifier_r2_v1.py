import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, city_coordinates, city_demands, robot_capacity):
    total_demand_met = [0] * len(city_demands)
    total_delivered = 0

    for tour in tours:
        capacity_used = 0
        for i in range(1, len(tour) - 1):  # Exclude depot city at start and end
            city_index = tour[i]
            demand = city_demands[city_index]
            total_demand_met[city_index] += demand
            capacity_used += demand

        # Check if the tour exceeds the robot's carrying capacity
        if capacity_used > robot_capacity:
            return "FAIL: Robot capacity exceeded"

    # Check if all city demands are met exactly
    for city_index in range(1, len(city_demands)):  # Exclude depot city
        if total_demand_met[city_index] != city_demands[city_index]:
            return f"FAIL: Demand not met for city {city_index} - Expected {city_demands[city_index]}, Met {total_demand_met[city_index]}"

    # Verify all tours start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start/end at the depot city"

    # Here we presume other conditions such as minimizing total travel cost are met
    return "CORRECT"

# Example data
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Example provided tours; actual solution would replace this
example_tours = [
    [0, 1, 2, 0],  # Robot 0 Tour
    [0, 3, 4, 0]   # Robot 1 Tour
]

# Run the verification
print(verify_solution(example_tours, city_coordinates, city_demands, robot_capacity))