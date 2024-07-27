import numpy as np

# Defining the city coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours provided for verification
tours = {
    0: [0, 20, 21, 0],
    1: [1, 15, 11, 1],
    2: [2, 8, 12, 2],
    3: [3, 19, 18, 3],
    4: [4, 16, 10, 4],
    5: [5, 9, 17, 5],
    6: [6, 14, 22, 6],
    7: [7, 13, 7]
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    coord1, coord2 = city_coordinates[city1], city_coordinates[city2]
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Validate the tours and total costs calculation
def validate_tours(tours):
    visited_cities = set()
    overall_cost = 0.0

    for robot_id, tour in tours.items():
        tour_cost = 0.0
        # Check circular tour
        if tour[0] != tour[-1]:
            return "FAIL"

        # Calculate total tour cost
        for i in range(len(tour) - 1):
            cost = calculate_distance(tour[i], tour[i + 1])
            tour_cost += cost
            visited_cities.add(tour[i + 1])

        # Display and accumulate costs
        print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")
        overall_cost += tour_cost

    # Check if every city is visited exactly once (except depots)
    if len(visited_cities) != len(city_coordinates):
        return "FAIL"

    print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")
    return "CORRECT"

# Result of the validation
result = validate_tours(tours)
print(result)