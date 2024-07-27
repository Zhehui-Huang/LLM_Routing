import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost, max_distance):
    try:
        # Define city coordinates based on the provided mapping
        cities = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
            5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
            10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
        }

        # [Requirement 1] Start and end at the depot city 0
        assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at city 0."

        # [Requirement 2] Each city is visited exactly once
        unique_cities = set(tour[1:-1])
        assert len(unique_cities) == 14 and len(tour) == 16, "Each city must be visited exactly once."

        # Calculate total distance and max distance between consecutive cities
        calculated_total_distance = 0
        calculated_max_distance = 0

        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            calculated_total_distance += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance

        # Check totals with a small margin for floating point comparison
        assert abs(calculated_total_distance - total_travel_cost) < 1e-4, "Total travel cost mismatch."
        assert abs(calculated_max_distance - max_distance) < 1e-4, "Max distance mismatch."

        print("CORRECT")
    except AssertionError as error:
        print(f"FAIL: {str(error)}")

# Given solution details
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.57
max_distance = 85.21

# Run the test
test_solution(tour, total_travel_cost, max_distance)