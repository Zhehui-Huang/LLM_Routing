import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tours, coordinates, num_robots):
    # Check if the number of robots is correct
    if len(tours) != num_robots:
        return "FAIL"
    
    visited_cities = set()
    max_travel_cost = 0
    for tour in tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the total travel cost of the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            dist = calculate_distance(*coordinates[city1], *coordinates[city2])
            tour_cost += dist
            
            # Exclude depot in the midway of tour for checking visited cities
            if i != 0:
                if city1 in visited_cities:
                    return "FAIL"
                visited_cities.add(city1)
        
        if tour_cost > max_travel_cost:
            max_travel_cost = tour_cost
    
    # Check if all non-depot cities are visited exactly once
    if len(visited_cities) != len(coordinates) - 1:  # excluding the depot city
        return "FAIL"
    
    # Calculating expected max cost based on provided output specs
    # For example purposes, we assume the output maximum cost is known here as 50.25
    # This should be higher than or match this expected maximum to accommodate edge cases
    expected_max_cost = 50.25  # This should be set based on given problem statement results or other reference
    if max_travel_cost != expected_max_cost:
        return "FAIL"

    return "CORRECT"

# Given tours
tours = [
    [0, 15, 12, 3, 0],
    [0, 2, 7, 22, 9, 13, 0],
    [0, 8, 18, 19, 0],
    [0, 21, 16, 6, 0],
    [0, 14, 17, 0],
    [0, 4, 11, 0],
    [0, 1, 10, 0],
    [0, 20, 5, 0]
]

# Assume city coordinates are stored in order from 0 to 22
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 64), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Check the solution and print the result
result = verify_solution(tours, city_coordinates, num_robots)
print(result)