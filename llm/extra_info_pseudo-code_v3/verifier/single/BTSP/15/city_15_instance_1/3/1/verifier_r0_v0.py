import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour_solution, city_coordinates):
    # Test if all cities and depot are visited exactly once, starting and ending at depot
    city_count = len(city_coordinates)
    if sorted(tour_solution) != list(range(city_count)) + [0]:
        return "FAIL"

    # Calculate the total travel cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour_solution) - 1):
        dist = euclidean_distance(city_coordinates[tour_solution[i]], city_coordinates[tour_pattern_signs[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check if provided total cost and max distance match calculated values
    if not (round(total_cost, 2) == 755.53 and round(max_distance, 2) == 85.21):
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by city number
city_coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Given solution
tour_solution = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_travel_cost = 755.53
max_distance = 85.21

# Perform validation
validation_result = validate_tour(tour_solution, city_coordinates)
print(validation_result)