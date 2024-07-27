import math

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tour_and_cost(tour, total_distance):
    coordinates = [
        (9, 93),  # City 0
        (8, 51),  # City 1
        (74, 99), # City 2
        (78, 50), # City 3
        (21, 23), # City 4
        (88, 59), # City 5
        (79, 77), # City 6
        (63, 23), # City 7
        (19, 76), # City 8
        (21, 38), # City 9
        (19, 65), # City 10
        (11, 40), # City 11
        (3, 21),  # City 12
        (60, 55), # City 13
        (4, 39)   # City 14
    ]

    # Requirements checks
    if len(coordinates) != 15:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != 5:
        return "FAIL"
    if any(city < 0 or city >= 15 for city in tour):
        return "FAIL"

    calculated_total_distance = 0
    for i in range(len(tour) - 1):
        calculated_total_distance += calculate_euclidean_distance(
            coordinates[tour[i]],
            coordinates[tour[i + 1]]
        )

    if round(calculated_total_distance, 2) != round(total_distance, 2):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 8, 10, 11, 0]
total_cost = 110.01

# Test the solution against the requirements
output = verify_tour_and_cost(tour, total_cost)
print(output)