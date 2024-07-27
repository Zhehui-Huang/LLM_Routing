import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tours(robots_tours, cities, demands, capacities, city_coords):
    """
    Validate tours based on the provided requirements.
    
    Args:
    robots_tours (dict): Dictionary with robot ID as key and list of visited city indices as value.
    cities (list): List of city indices.
    demands (dict): Dictionary with city indices as keys and demands as values.
    capacities (dict): Dictionary with robot ID as key and capacity value as value.
    city_coords (dict): Dictionary with city indices as keys and coordinates (tuple) as values.
    
    Returns:
    str: "CORRECT" if all validations pass, otherwise "FAIL".
    """
    total_cost = 0.0
    city_supplied = {city: 0 for city in cities}
    
    # Check all robots' tours
    for robot_id, tour in robots_tours.items():
        route_capacity_used = 0
        
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        previous_city = tour[0]
        for city in tour[1:]:
            # Calculate distance and sum up for total cost
            total_cost += calculate_distance(city_coords[previous_city], city_coords[city])
            previous_city = city
            
            # Only count demands if it's not the depot city
            if city != 0:
                route_capacity_used += demands[city]
                city_supplied[city] += demands[city]
        
        # Check route capacity
        if route_capacity_used > capacities[robot_id]:
            return "FAIL"
    
    # Check if all demands are met
    if any(city_supplied[city] != demands[city] for city in cities if city != 0):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Hypothetical examples assumed here since no specific robot tours were output in your example
# Define city coordinates and other information for validation
city_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
                    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 
                    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)} 

demands = {0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8, 11: 7, 12: 14,
           13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15}

capacities = {0: 160, 1: 160}

# Test tours (These would be output from an actual solution calculation)
test_robots_tours = {
    0: [0, 1, 2, 4, 0],
    1: [0, 3, 5, 6, 0]
}

# Validate the tours based on the requirements
result = validate_tours(test_robots_tours, list(city_coordinates.keys()), demands, capacities, city_coordinates)
print(result)