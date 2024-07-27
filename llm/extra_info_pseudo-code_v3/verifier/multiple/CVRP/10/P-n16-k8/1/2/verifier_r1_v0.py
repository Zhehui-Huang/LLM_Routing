import math

# Input data preparation
cities_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35

# Result data preparation
robot_tours = [
    ([0, 6, 0], 24.08),
    ([0, 1, 10, 13, 0], 68.44),
    ([0, 2, 0], 42.05),
    ([0, 4, 11, 0], 57.39),
    ([0, 7, 5, 9, 0], 75.54),
    ([0, 15, 12, 0], 66.12),
    ([0, 14, 3, 0], 100.91),
    ([0, 8, 0], 64.9)
]

# Calculating overall travel cost
calculated_overall_cost = sum([cost for _, cost in robot_tours])

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Validate tours and costs
def validate_solution():
    all_visited_cities = set()
    total_demands = {i: 0 for i in range(16)}

    for tour, reported_cost in robot_tours:
        last_city = tour[0]
        travel_cost = 0
        tour_capacity = 0

        for city in tour[1:]:
            travel_cost += calculate_distance(cities_coordinates[last_city], cities_coordinates[city])
            tour_capacity += demands[city]
            total_demands[city] += demands[city]
            last_city = city
            all_visited_cities.add(city)
        
        if round(travel_cost, 2) != reported_cost:
            return "FAIL"

        if tour_capacity > robot_capacity:
            return "FAIL"
    
    if any(total != demands[i] for i, total in total_demands.items()):
        return "FAIL"

    if all_visited_cities != set(range(1, 16)):  # Exclude depot
        return "FAIL"
    
    if round(calculated_overall_cost, 2) != 499.44:
        return "FAIL"

    return "CORRECT"

# Run the validation
result = validate_solution()
print(result)