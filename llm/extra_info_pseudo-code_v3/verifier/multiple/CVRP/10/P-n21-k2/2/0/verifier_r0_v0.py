import math

# Define the capacities and demands
robot_capacity = 160
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Tours provided in the solution
tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 0],  # Robot 0 Tour
    [0, 6, 20, 5, 7, 2, 9, 17, 14, 0]     # Robot 1 Tour
]

# Define the city coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Verify the tours
def verify_solution(tours, demands, capacities, coords):
    all_visited_cities = set()
    for tour_index, tour in enumerate(tours):
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        total_load = 0
        previous_city = 0
        
        for index in range(1, len(tour)):
            city = tour[index]
            all_visited_cities.add(city)
            # Calculate load
            total_load += demands[city]
            if total_load > capacities:
                return "FAIL"
            
            # Reset load at the depot
            if city == 0:
                total_load = 0
            
            # Calculate distance and check metro rule
            distance = euclidean_distance(coords[previous_city], coords[city])
            if distance > 100:  # Customize this if there's a metro radius limit
                return "FAIL"
            
            previous_city = city
    
    # Check if all necessary cities were visited
    if len(all_visited_cities) != len(demands) - 1:
        return "FAIL"

    return "CORRECT"

# Call the verification function
result = verify_solution(tours, demands, robot_capacity, city_coords)
print(result)