import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_robot_tours():
    # City coordinates starting from the depot
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
        (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    # Demands at each city, starting from the depot
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

    # Robot tours provided:
    robot_tours = [
        [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
        [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
    ]

    # Check if all cities are visited exactly once
    all_visited_cities = set(city for tour in robot_tours for city in tour if city != 0)
    if len(all_visited_cities) != 20:
        return "FAIL"

    # Robot capacity
    capacity = 160

    # Tour checking
    for tour in robot_tours:
        load = 0
        total_distance = 0
        previous_city = tour[0]  # Start at the depot

        for i in range(1, len(tour)):
            city = tour[i]
            load += demands[city]
            if load > capacity:
                return "FAIL"  # Overloaded robot check

            # Calculate travel distance
            distance = calculate_euclidean_distance(
                *coordinates[previous_city], *coordinates[city]
            )
            total_distance += distance
            previous_city = city

        # Back to depot
        distance_back_to_depot = calculate_euclidean_distance(
            *coordinates[previous_city], *coordinates[tour[0]]
        )
        total_distance += distance_back_to_depot

    # If it checks out without failing:
    return "CORRECT"

# Testing the function
print(test_robot_tours())