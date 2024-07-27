import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of each city, indexed from 0 to 9
cities = [
    (84, 67),  # Depot 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def verify_solution(tour, max_consecutive_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at depot city 0."
    
    if len(set(tour)) != 11 or sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return "FAIL", "Tour does not include all cities exactly once."

    max_distance_found = 0
    total_distance = 0

    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += distance
        if distance > max_distance_found:
            max_distance_found = distance

    if abs(max_distance_found - max_consecutive_distance) > 0.0001:
        return "FAIL", f"Reported max consecutive distance does not match with the calculated maximum."

    return "CORRECT", None

# Example output from the MILP solver
# Note: There seems to be duplicated 0 at the end of the tour list in the problem provided, here we assume the correct tour as the first given.
tour = [0, 3, 9, 5, 6, 7, 2, 4, 1, 8, 0]
max_consecutive_distance = 68.26419266350405
result, error = verify_solution(tour, max_consecutive_distance)
if error:
    print(f"FAIL: {error}")
else:
    print(result)