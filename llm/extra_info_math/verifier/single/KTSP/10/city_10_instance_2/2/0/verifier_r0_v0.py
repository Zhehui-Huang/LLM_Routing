import math

# Define the cities with their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their indices."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour):
    """Check the three requirements described above, and verify the total distance."""
    requirement_1 = tour[0] == 0 and tour[-1] == 0  # Tour starts and ends at depot city
    requirement_2 = len(set(tour)) == 7  # Including depot city, should visit exactly 6 cities
    expected_distance = 223.41  # Provided expected distance

    # Calculate the total distance traveled in the provided tour
    total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    # Check if the total calculated distance matches the provided distance (with a tolerance for floating point comparison)
    requirement_3 = math.isclose(total_distance, expected_distance, rel_tol=1e-2)

    # Print "CORRECT" if all requirements and the distance check pass
    if requirement_1 and requirement_2 and requirement_3:
        return "CORRECT"
    else:
        return "FAIL"

# Provided tour and the expected total distance
tour = [0, 1, 2, 4, 5, 8, 0]

# Execute the verification function and print the result
result = verify_tour(tour)
print(result)