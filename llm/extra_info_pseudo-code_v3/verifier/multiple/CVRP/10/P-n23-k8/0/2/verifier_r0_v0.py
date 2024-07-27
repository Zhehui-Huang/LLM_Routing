import math

# Hypothetical solution for demonstration.
# This should be replaced with the actual output from the solution.
solution_tours = {
    0: [0, 1, 2, 0],
    1: [0, 3, 4, 0],
    2: [0, 5, 6, 0],
    3: [0, 7, 8, 0],
    4: [0, 9, 10, 0],
    5: [0, 11, 12, 0],
    6: [0, 13, 14, 0],
    7: [0, 15, 16, 0]
}

# Coordinates and demand as provided in the example.
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 7},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    # Add more cities based on the need.
}

# Capacity of one robot.
robot_capacity = 40

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to validate the solution
def validate_solution(tours, cities, robot_capacity):
    all_cities_delivered = set()
    total_cost = 0

    # Check all tours meet requirements
    for robot_id, tour in tours.items():
        load = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            load += cities[city_to]['demand']
            tour_cost += calculate_distance(cities[city_from]['coord'], cities[city_to]['coord'])
            all_cities_delivered.add(city_to)
        
        # Check load does not exceed capacity
        if load > robot_capacity:
            return "FAIL"

        # Add cost of returning to depot
        last_city = tour[-2]
        tour_cost += calculate_distance(cities[last_city]['coord'], cities[0]['coord'])
        total_cost += tour_cost
    
    # Check if all cities are visited
    if all_cities_delivered != set(cities.keys()) - {0}:
        return "FAIL"

    # If all conditions are satisfied, consider solution correct
    return "CORRECT"

# Run the validation function
result = validate_solution(solution_tours, cities, robot_capacity)
print(result)