import math

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def test_solution():
    # City coordinates indexed by city ID (including depot city at index 0)
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]

    # Provided robot tours
    robot_tours = {
        0: [0, 1, 2, 5, 7, 9, 0],
        1: [0, 15, 12, 14, 16, 13, 0],
        2: [0, 10, 8, 6, 3, 4, 11, 0],
        3: [0, 20, 21, 19, 17, 18, 0]
    }

    # Compute and check the maximum distance claimed in the solution
    max_distance = 124.61612543560025
    actual_max_distance = 0
    all_visited_cities = set()

    for robot, tour in robot_tours.items():
        last_city = 0
        sum_distance = 0
        for city in tour[1:]:  # Skip the starting depot initially in the calculation
            dist = euclidean_distance(coordinates[last_city], coordinates[city])
            sum_distance += dist
            last_city = city
        
        # Check if the calculated distance matches (or at least is very close) to the provided distance
        if abs(sum_distance - max_distance) > 1e-5 and sum_distance > actual_max_distance:
            actual_max_distance = sum_distance

        all_visited_cities.update(tour[1:-1])  # Exclude the depot from checks
    
    # Check requirements
    correct_number_of_cities = len(all_visited_cities) == 21
    correct_tour_start_end = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours.values())
    correct_maximum_distance = abs(actual_max_distance - max_distance) < 1e-5

    if correct_number_of_cities and correct_tour_start_end and correct_maximum_distance:
        return "CORRECT"
    else:
        return "FAIL"

# Running test
print(test_solution())