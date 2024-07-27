import unittest
import math

# Cities and their coordinates
cities = {
    0: (14, 77),
    9: (27, 45),
    14: (21, 79),
    13: (26, 29),
    2: (19, 38),
    6: (4, 56)
}

# Provided solution
tour_solution = [0, 14, 9, 13, 2, 6, 0]
total_cost_solution = 115.9285924123634

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    coord1 = cities[city1]
    coord2 = cities[city2]
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestKVRP(unittest.TestCase):
    def test_tour_start_and_end_at_depot(self):
        """ The tour must start and end at the depot city, which is city 0 """
        self.assertEqual(tour_solution[0], 0)
        self.assertEqual(tour_solution[-1], 0)

    def test_tour_visits_exactly_7_cities(self):
        """ The robot must visit exactly 7 cities, including the depot city """
        self.assertEqual(len(set(tour_solution)), 7)

    def test_tour_total_travel_cost(self):
        """ Checking the total travel cost of the tour """
        total_travel_cost = sum(euclidean_distance(tour_solution[i], tour_solution[i + 1]) for i in range(len(tour_solution) - 1))
        self.assertAlmostEqual(total_travel_cost, total_cost_solution, places=6)
    
    def test_output_tour_indices_and_cost(self):
        """ Tour outputs as a list of city indices and total travel cost """
        expected_tour_indices = [0, 14, 9, 13, 2, 6, 0]
        expected_total_cost = 115.9285924123634  # This is given as correct
        self.assertEqual(tour_solution, expected_tour_indices)
        self.assertAlmostEqual(total_cost_solution, expected_total_cost, places=6)

# Running the tests to validate the tour
if __name__ == "__main__":
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestKVRP)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")