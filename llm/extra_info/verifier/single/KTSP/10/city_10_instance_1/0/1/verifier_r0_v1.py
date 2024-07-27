import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_cost += euclidean_distance(city_coordinates[city_a][0], city_coordinates[city_a][1],
                                         city_coordinates[city_b][0], city_coordinates[city_b][1])
    return total_cost

def test_solution():
    # City coordinates based on the given problem
    city_coordinates = {
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
    
    # Provided tour
    tour = [0, 4, 8, 3, 5, 0]
    expected_cost = 110.38
    
    # Testing each requirement
    # Check if the tour starts and ends at the depot city
    starts_at_depot = tour[0] == 0
    ends_at_depot = tour[-1] == 0
    
    # Check the tour visits exactly 5 cities
    number_of_cities = len(set(tour)) == 5
    
    # Check all city indices in the tour are correctly bounded
    correct_city_indices = all(0 <= city <= 9 for city in tour)
    
    # Calculate and check if the total travel cost is close to the expected value
    calculated_cost = calculate_total_travel_cost(tour, city_coordinates)
    cost_is_correct = math.isclose(calculated_cost, expected_cost, rel_tol=1e-2)  # using some tolerance for floating point comparison
    
    # Check all conditions
    if starts_at_depot and ends_at_depot and number_of_cities and correct_city_indices and cost_is_correct:
        print("CORRECT")
    else:
        print("FAIL")

# Calling the test function
test_solution()