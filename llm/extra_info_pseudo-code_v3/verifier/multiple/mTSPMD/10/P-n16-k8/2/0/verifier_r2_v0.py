import math

# Define the city coordinates
city_coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 49),  # Depot city 2
    (52, 64),  # Depot city 3
    (31, 62),  # Depot city 4
    (52, 33),  # Depot city 5
    (42, 41),  # Depot city 6
    (52, 41),  # Depot city 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69)   # City 15
]

# Solution provided by the robot tours
robot_tours = {
    'Robot 0': {'tour': [0, 10, 0], 'cost': 41.62},
    'Robot 1': {'tour': [1, 12, 1], 'cost': 32.31},
    'Robot 2': {'tour': [2, 13, 2], 'cost': 18.11},
    'Robot 3': {'tour': [3, 8, 3], 'cost': 15.62},
    'Robot 4': {'tour': [4, 11, 4], 'cost': 14.42},
    'Robot 5': {'tour': [5, 14, 5], 'cost': 16.97},
    'Robot 6': {'tour': [6, 9, 6], 'cost': 40.05},
    'Robot 7': {'tour': [7, 15, 7], 'cost': 63.53}
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Validate the solution
def validate_robot_tours(robot_tours, city_coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0.0
    for robot, info in robot_tours.items():
        tour = info['tour']
        expected_cost = info['cost']
        calculated_cost = 0.0
        for i in range(len(tour) - 1):
            from_city = city_coordinates[tour[i]]
            to_city = city_coordinates[tour[i + 1]]
            calculated_cost += euclidean_distance(from_city, to_city)
            all_visited_cities.add(tour[i])
        all_visited_cities.add(tour[-1])  # Adding the last city
        if round(calculated_cost, 2) != round(expected_cost, 2):
            return "FAIL"
        total_calculated_cost += calculated_cost

    # Check if all cities are visited exactly once
    if len(all_visited_cities) != 16:
        return "FAIL"

    # Check total travel cost
    expected_total_travel_cost = sum(info['cost'] for info in robot_tours.values())
    if round(total_calculated_cost, 2) != round(expected_total_travel_cost, 2):
        return "FAIL"

    return "CORRECT"

# Validate and return the result
result = validate_robot_tours(robot_tours, city_coordinates)
print(result)