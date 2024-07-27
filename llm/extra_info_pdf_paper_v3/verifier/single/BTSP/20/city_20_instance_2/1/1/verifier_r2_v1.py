import math

# City coordinates in order of city indices
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided solution details
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.43
maximum_distance = 80.61

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def test_solution():
    # Check if all cities are visited exactly once (excluding the return to start)
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    # Calculate the total travel cost and maximum distance between neighboring cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_callculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Round calculations to two decimal places to match the provided values
    calculated_total_cost = round(calculated_total_cost, 2)
    calculated_max_distance = round(calculated_max_distance, 2)

    # Check if calculated values match provided solution
    if calculated_total_cost != total_travel_cost or calculated_max_distance != maximum_distance:
        return "FAIL"

    return "CORRECT"

# Output the test result
print(test_solution())