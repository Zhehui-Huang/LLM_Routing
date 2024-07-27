import math

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def verify_solution(tour, coords):
    # Requirement: The robot starts and ends its journey at the depot city 0.
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Requirement: Each city must be visited exactly once by the robot.
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9 or any(city not in unique_cities for city in range(1, 10)):
        return "FAIL"

    # Calculate total travel cost and check longest distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(coords[tour[i]], coords[tour[i + 1]])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Requirement: Travel cost between any two cities is computed as the Euclidean distance.
    # Printing for verification; the actual value should match the given total travel cost and max distance
    print(f"Computed total travel cost: {total_travel_cost:.2f}")
    print(f"Computed maximum distance between consecutive cities: {max_distance:.2f}")

    # Verifying computed values (hard-coded from provided solution)
    if not (abs(total_travel_cost - 327.13) < 1e-2 and abs(max_distance - 45.19) < 1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Provided solution for testing
tour_solution = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]

# Verify the solution
result = verify_solution(tour_solution, coordinates)
print(result)