import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour():
    # Define the cities coordinates
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # Solution provided
    tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
    total_travel_cost = 418.32344417340323
    max_distance = 69.42621983083913

    # [Requirement 1] Start and end at depot city 0
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot city."
    
    # [Requirement 2] Each city visited exactly once, excluding depot city (visited twice)
    assert all(tour.count(city) == 1 for city in range(1, 10)), "Each city is not visited exactly once."
    assert tour.count(0) == 2, "Depot city is not visited exactly twice."
    
    # [Requirement 3] Travel cost is Euclidean distance
    computed_total_cost = 0
    computed_max_distance = 0
    
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_distance(cities[city1], cities[city2])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_text = f"Computed max distance ({distance}) is greater than provided max distance ({max_distance})."
            assert distance <= max_distance + 0.01, computed_max_text
    
    # [Requirement 4] [Optional] this might not be necessary if max constraint is not strict.
    assert abs(computed_total_cost - total_travel_cost) < 0.01, "Computed total cost does not match provided total cost."

    # [Requirement 5] These checks already performed implicitly by other assertions.

    # If test reaches this point, everything passed
    print("CORRECT")

test_tour()