import math

# Given data
cities_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Proposed tour and metrics
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
proposed_total_cost = 458.37
proposed_max_dist = 68.15

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((cities_coordinates[city_a][0] - cities_coordinates[city_b][0])**2 + (cities_coordinates[city_a][1] - cities_coordinates[city_b][1])**2)

def validate_tour(tour, proposed_total_cost, proposed_max_dist):
    # Verifying Requirement 1 and 5
    if not (tour[0] == tour[-1] == 0):
        return "FAIL"

    # Verifying Requirement 2
    if len(set(tour[1:-1])) != 19 or len(tour) - 1 != 20:
        return "FAIL"

    # Calculate metrics
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i+1])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Verifying calculated cost and max distance
    if not (math.isclose(total_travel_cost, proposed_total_cost, abs_tol=0.01) and math.isclose(max_distance, proposed_max_dist, abs_tol=0.01)):
        return "FAIL"

    return "CORRECT"

# Running the validation
result = validate_tour(tour, proposed_total_cost, proposed_max_dist)
print(result)