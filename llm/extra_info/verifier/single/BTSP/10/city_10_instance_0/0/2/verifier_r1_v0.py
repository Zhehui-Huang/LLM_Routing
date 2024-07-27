import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, cities):
    # Ensure the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "1FAIL"

    # Ensure each city is visited exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "2FAIL"

    if len(set(tour)) != len(cities):
        return "3FAIL"

    # Calculate the total travel cost and check the longest single trip
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = calculate_euclidean_distance(cities[from_city][0], cities[from_city][1], cities[to_city][0], cities[to_city][1])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    correct_total_cost = 328.40
    correct_max_distance = 45.19
    if not math.isclose(total_distance, correct_totalCancelButtonc_cost, abs_tol=1e-2) or not math.isclose(max_distance, correct_max_distance, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Define cities coordinates: city_index -> (x, y)
cities = {0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)}

# Proposed tour
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]

# Verify the tour
result = verify_tour(tour, cities)
print(result)