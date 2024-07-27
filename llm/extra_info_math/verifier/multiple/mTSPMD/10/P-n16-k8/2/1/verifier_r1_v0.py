import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, city_coords):
    visited_cities = set()
    total_travel_cost = 0

    for robot_id, tour in enumerate(tours):
        # Check if each tour starts and ends at its depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL"

        # Check if cities are visited only once
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculate travel cost
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        total_travel_cost += cost

    # Check if all cities are visited exactly once
    if len(visited_cities) != len(city_coords) - 8:  # excluding depots
        return "FAIL"

    # Output total travel cost and collect costs for assert in testing
    print(f"Total Travel Cost: {total_travel_cost}")
    return "CORRECT"

# Sample data setup
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Hypothetical tours example, replace with actual tours and dispatch each robot to its route
tours_example = [
    [0, 8, 1, 0], [1, 9, 2, 1], [2, 10, 3, 2], [3, 11, 4, 3],
    [4, 12, 5, 4], [5, 13, 6, 5], [6, 14, 7, 6], [7, 15, 7]
]

# Function call assuming output from solver is available
# This is a hypothetical input example
output_verification = verify_solution(tours_example, city_coords)
print(output_verification)