def check_tour_validity(tour, max_consecutive_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city 0."

    if len(set(tour)) != 20 or set(tour) != set(range(20)):
        return "FAIL", "Not all cities are visited exactly once."

    # City coordinates including the depot
    city_positions = [
        (8, 11),  # Depot city 0
        (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
        (25, 71), (61, 16), (27, 91), (40, 87), (20, 97), (61, 25), 
        (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    # It appears there was a missing city position for city 19 based on previous index issue.
    city_positions.append((91, 46))  # Position for City 19

    # Euclidean distance function
    def euclidean_distance(pos1, pos2):
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

    consecutive_distances = [
        euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
        for i in range(len(tour) - 1)
    ]

    calculated_max_distance = max(consecutive_distances)
    if not (abs(calculated_max_distance - max_consecutive_distance) <= 1e-5):
        return "FAIL", f"Maximum distance between consecutive cities is incorrect. Expected: {max_consecutive_distance}, Calculated: {calculated_max_distance}"

    return "CORRECT", None

# Solution output from the solver
tour = [0, 4, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 19, 2, 6, 5, 8, 17, 13, 1, 0]
max_consecutive_distance = 32.38826948140329

# Validate the tour and distance
result, error_message = check_tour_validity(tour, max_concessive_distance)
print(result)
if error_message:
    print(error_message)