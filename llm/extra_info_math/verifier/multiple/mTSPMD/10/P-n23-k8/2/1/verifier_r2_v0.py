import numpy as np

# Cities coordinates
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

# Tours reported by the solver
tours = {
    0: [0, 21, 0],
    1: [1, 10, 1],
    2: [2, 13, 2],
    3: [3, 8, 3],
    4: [4, 15, 4],
    5: [5, 20, 5],
    6: [6, 16, 6],
    7: [7, 22, 7]
}

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Validate the solution
def validate_tours(tours, coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0

    # Verification of tour validity
    for robot, tour in tours.items():
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"  # Tour doesn't start and end at the robot's designated depot
        
        # Check all cities are visited once
        for city in tour[1:-1]:  # Ignore the depot start/end in check
            if city in all_visited_cities:
                return "FAIL"  # City visited more than once
            all_visited_cities.add(city)

        # Calculate the travel cost for this tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        print(f"Robot {robot} Calculated Travel Cost: {tour_cost:.2f}")

        # Verify reported and calculated costs
        total_calculated_cost += tour_cost

    print(f"Total Calculated Cost: {total_calculated_cost:.2f}")

    # Check if all cities are visited
    if all_visited_cities != set(range(23)):
        return "FAIL"  # Not all cities are visited

    return "CORRECT"

# Execute validation
result = validate_tours(tours, coordinates)
result