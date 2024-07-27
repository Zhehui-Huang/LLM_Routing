import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robot_tours, city_coords):
    cities_visited = set()
    max_distance = 0

    # Test each robot tour
    for robot_id, tour in enumerate(robot_tours):
        # Check for starting and ending at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate tour distance and check visited cities
        tour_distance = 0
        for i in range(len(tour) - 1):
            tour_distance += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
            if i != 0:  # exclude the depot from the visitation check
                cities_visited.add(tour[i])

        # Update maximum distance traveled
        if tour_distance > max_distance:
            max_distance = tour_distance

    # Check if all cities were visited exactly once and exclude the depot
    if len(cities_visited) != len(city_coords) - 1:
        return "FAIL"

    # Check calculated max distance against provided
    if not math.isclose(max_distance, 178.22357880921848, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# City coordinates as given in the problem statement
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

robot_tours = [
    [0, 14, 17, 20, 10, 5, 4, 0],
    [0, 16, 19, 21, 9, 2, 0],
    [0, 12, 15, 18, 7, 1, 0],
    [0, 13, 11, 8, 6, 3, 0]
]

# Run the unit test on the provided tours
result = check_solution(robot_tours, city_coords)
print(result)