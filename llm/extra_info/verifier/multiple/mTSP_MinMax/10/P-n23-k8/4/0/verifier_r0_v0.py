import math

# Define the coordinates for each city based on the provided information
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Define the respective robot tours
robot_tours = {
    0: [0, 2, 8, 13, 9, 0],
    1: [0, 3, 12, 15, 0],
    2: [0, 6, 21, 0],
    3: [0, 14, 17, 0],
    4: [0, 1, 10, 16, 0],
    5: [0, 18, 19, 0],
    6: [0, 4, 11, 0],
    7: [0, 7, 22, 5, 20, 0]
}

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def verify_solution():
    visited_cities = set()
    max_travel_cost = 0
    
    for robot, tour in robot_tours.items():
        tour_cost = 0
        
        # Check all robots start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            # Calculate cost and add to tour cost
            distance = calculate_distance(city1, city2)
            tour_cost += distance

            # Ensure each city is visited once excluding depot
            if city1 != 0:
                visited_cities.add(city1)
        
        # Update the max travel cost
        if tour_cost > max_travel_cost:
            max_travel_cost = tour_cost
    
    # Check for each city visit
    if len(visited_cities) != 22:  # Excluding depot
        return "FAIL"

    return "CORRECT"

# Invoke the test
print(verify_solution())