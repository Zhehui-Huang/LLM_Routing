import math

# Define the coordinates of the cities
cities_coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Given tour and total travel cost
given_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
given_total_cost = 0.0

# Validate the provided solution against the requirements
def is_valid_tour(tour):
    if len(tour) == 11 and len(set(tour[:-1])) == 10 and tour[0] == 0 and tour[-1] == 0:
        # Validate the list size and that it both starts and ends with the depot (city 0)
        return True
    return False

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        from_city = cities_coordinates[tour[i]]
        to_city = cities_coordinates[tour[i + 1]]
        total_cost += math.sqrt((from_city[0] - to_city[0]) ** 2 + (from_city[1] - to_city[1]) ** 2)
    return total_cost

def test_tour_and_cost(tour, reported_cost):
    # Check if the tour is valid
    if not is_valid_tour(tour):
        return "FAIL"

    # Calculate the actual total cost
    actual_cost = calculate_total_travel_cost(tour)
    
    # Allow a small error margin for floating point comparisons
    if abs(actual_cost - reported_cost) < 1e-6:
        return "CORRECT"
    else:
        return "FAIL"

# Execute the test
result = test_tour_and_cost(given_tour, given_total_cost)
print(result)