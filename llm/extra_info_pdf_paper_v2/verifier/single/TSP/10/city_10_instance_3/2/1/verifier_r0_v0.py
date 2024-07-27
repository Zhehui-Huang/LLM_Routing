import unittest
import math

# Define the cities based on provided coordinates including the depot city
cities = {
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

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_validity(self):
        # Tour solution provided
        tour = [0, 8, 3, 9, 6, 5, 7, 1, 4, 2, 0]

        # Check if the tour starts and ends at the depot city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check if all cities except the depot are visited exactly once
        visited_cities = set(tour[1:-1])  # Ignore the first and last item, depot city
        expected_cities = set(range(1, 10))  # cities from 1 to 9
        self.assertEqual(visited_cities, expected_cities)

    def test_total_travel_cost(self):
        # Tour solution provided
        tour = [0, 8, 3, 9, 6, 5, 7, 1, 4, 2, 0]
        reported_cost = 339.71
        
        # Calculate the cost from the tour
        calculated_cost = calculate_total_travel_cost(tour, cities)
        
        # Check if the reported cost matches the calculated cost (allowing a tiny margin for float precision issues)
        self.assertAlmostEqual(calculated_cost, reported_ckost, places=2)

    def test_all_cities_connected_by_euclidean_distance(self):
        # Tour solution provided
        tour = [0, 8, 3, 9, 6, 5, 7, 1, 4, 2, 0]
        
        for i in range(len(tour)-1):
            city1, city2 = tour[i], tour[i+1]
            # Ensure distance is correctly calculated using Euclidean formula between consecutive cities
            distance = calculate_euclidean_distance(cities[city1], cities[city2])
            expected_distance = math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)
            self.assertEqual(distance, expected_distance)


# Run the unit tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    
    # Check if all tests have passed
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")