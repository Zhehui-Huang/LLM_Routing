import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_solution():
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    tour = [0, 3, 8, 4, 5, 2, 9, 7, 1, 6, 0]
    calculated_bottleneck = 56.61271941887264
    calculated_total_cost = 288.5902143298751
    calculated_max_distance = 56.61271941887264

    # Checking Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking Requirement 2: Each city must be visited exactly once (except depot)
    visited_cities = set(tour)
    if len(visited_cities) != len(cities) + 1 or any(tour.count(city) != 1 for city in cities if city != 0):
        return "FAIL"

    # Compute total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max distance:
            max_distance = distance

    # Checking Requirement 4
    if not (abs(total_cost - calculated_total_cost) < 0.01 and abs(max_distance - calculated_max_distance) < 0.01):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Running the test
print(test_tour_solution())