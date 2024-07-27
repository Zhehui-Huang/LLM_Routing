import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour_and_cost():
    # Pre-defined city coordinates indexed by city index
    city_coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }
    # Groups of cities
    city_groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }
    
    # Solution provided
    proposed_tour = [0, 6, 7, 5, 0]
    proposed_cost = 74.94753083872993
    
    # Check starts and ends at depot city, city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check it visits exactly one city from each group in the order 0, 1, 2
    visited_groups = [0 if city in city_groups[0] else 1 if city in city_groups[1] else 2 for city in proposed_tour[1:-1]]
    if visited_groups != sorted(visited_groups):
        return "FAIL"

    # Check the calculated tour cost matches the provided cost
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = proposed_tour[i]
        city2 = proposed_tour[i + 1]
        calculated_cost += calculate_euclidean_distance(city_coordinates[city1], city_coordinates[city2])
    
    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Run the test
print(test_tour_and_cost())