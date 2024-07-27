import math

# Given data
city_locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), 
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), 
    (63, 69), (45, 35), (32, 39), (56, 37)
]
city_demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 
    6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
robot_capacity = 40

# Tours provided in the solution
robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

# Function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Validate the solution
def validate_solution(tours, demands, capacity):
    # Check if all demands are met
    demand_fulfilled = [0] * len(demands)
    actual_travel_cost = 0.0

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at depot"
        
        current_carry = 0
        prev_city = tour[0]
        
        for city in tour[1:]:
            current_carry += city_demands[city]
            demand_fulfilled[city] += city_demands[city]
            actual_travel_cost += euclidean_distance(prev_city, city)
            prev_city = city
        
        # Check if exceeds the capacity
        if current_carry > capacity:
            return "FAIL: Exceeds robot capacity"

        # Close the tour
        actual_travel_cost += euclidean_distance(prev_city, tour[0])
    
    # Check if all demands are exactly met
    if any(fulfilled != demand for fulfilled, demand in zip(demand_fulfilled, city_demands)):
        return "FAIL: City demands not correctly met"

    return "CORRECT"

# Invoking the validation
validation_result = validate_solution(robot_tours, city_demands, robot_capacity)
print(validation_result)