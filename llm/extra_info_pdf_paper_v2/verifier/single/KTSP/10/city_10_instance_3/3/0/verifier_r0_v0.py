import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost_claimed):
    cities_coordinates = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 7 cities are visited
    if len(set(tour)) != 8:  # including the repeat of depot city
        return "FAIL"

    # Calculate the total cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities_coordinates[city_a], cities_coordinates[city_b])

    # Compare the calculated cost with the claimed total cost
    if not math.isclose(calculated_cost, total_cost_claimed, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Given tour and cost from the task solution
tour = [0, 3, 9, 6, 2, 4, 7, 0]
total_cost_claimed = 261.36

# Verify the solution
result = verify_solution(tour, total_cost_claimed)
print(result)