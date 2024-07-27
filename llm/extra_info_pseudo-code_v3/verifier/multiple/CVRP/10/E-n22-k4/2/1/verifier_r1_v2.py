import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(cities, demands, robots, robot_tours, robot_capacity, solution):
    city_coords = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
        5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
        10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    demands_fulfilled = {key: 0 for key in range(cities)}
    all_distances_correct = True

    for robot_index, tour in enumerate(robot_tours):
        current_capacity = 0
        total_distance = 0
        previous_city = tour[0]

        for city in tour[1:]:
            if city != 0:  # Ensure we are not calculating depot to depot
                demands_fulfilled[city] += demands[city]
                current_capacity += demands[city]
                if current_capacity > robot_capacity:
                    return "FAIL"

            distance = calculate_distance(*city_coords[previous_city], *city_coords[city])
            total_distance += distance
            previous_city = city

        # Comparing calculated and provided solutions' individual distances
        if not math.isclose(total_distance, solution[robot_index], abs_tol=1.0):
            all_distances_correct = False

    # Validate that all cities demands are satisfied exactly
    if not all(demands[city] == demands_fulfilled[city] for city in range(1, cities)):
        return "FAIL"

    # Ensure all distances are correct within allowed tolerance
    if not all_distances_correct:
        return "FAIL"

    return "CORRECT"

# Input data simulation
result = verify_solution(
    cities=22,
    demands={0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100,
             9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100,
             17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700},
    robots=4,
    robot_tours=[
        [0, 14, 17, 20, 10, 5, 0],
        [0, 16, 19, 21, 9, 0],
        [0, 12, 15, 18, 7, 2, 1, 0],
        [0, 13, 11, 8, 6, 3, 4, 0]
    ],
    robot_capacity=6000,
    solution=[138.86, 129.62, 164.33, 118.68]
)

print(result)  # Outputs "CORRECT" or "FAIL"