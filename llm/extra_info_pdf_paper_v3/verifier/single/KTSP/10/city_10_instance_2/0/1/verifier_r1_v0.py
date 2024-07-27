import unittest
import math

class TestKTSPSolution(unittest.TestCase):

    def setUp(self):
        # Coordinates of the cities
        self.cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
        # The proposed solution tour
        self.tour = [9, 1, 2, 5, 8, 0, 0]
        # The total travel cost according to the solution
        self.total_cost = 105.59116123237973
        
    def calculate_euclidean_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    def test_tour_starts_and_ends_at_depot(self):
        # First and last city in the tour should be the depot city (index 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_total_cities_visited_including_depot(self):
        # Should visit exactly 6 cities, including the depot
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 6)
        
    def test_total_travel_cost(self):
        # Calculate the total cost of the tour as per the distances provided
        calculated_cost = 0
        previous_city = None
        for current_city_index in self.tour:
            if previous_city is not None:
                calculated_cost += self.calculate_euclidean_distance(self.cities[previous_city], self.cities[current_city_index])
            previous_city = current_city_index
        
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)
    
    def test_solution_correctness(self):
        if (self.test_tour_starts_and_ends_at_depot() and
            self.test_total_cities_visited_including_depot() and
            self.test_total_travel_cost()):
            print("CORRECT")
        else:
            print("FAIL")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)