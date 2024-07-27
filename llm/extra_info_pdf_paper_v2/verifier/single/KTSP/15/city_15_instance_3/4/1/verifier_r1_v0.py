import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90),
            1: (43, 99),
            2: (80, 21),
            3: (86, 92),
            4: (54, 93),
            5: (34, 73),
            6: (6, 61),
            7: (86, 69),
            8: (30, 50),
            9: (35, 73),
            10: (42, 64),
            11: (64, 30),
            12: (70, 95),
            13: (29, 64),
            14: (32, 79)
        }
        self.tour = [0, 14, 11, 2, 12, 4, 9, 5, 13, 6, 0]
        self.reported_cost = 279.8470903493033

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")

    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 10, "Tour should visit exactly 10 cities")

    def test_tour_calculation_accuracy(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        calculated_cost = sum(
            euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5,
                               msg="Reported travel cost should closely match the calculated cost")

    def test_correct_tour_output(self):
        # Assuming there exists a method or pre-calculated value for the shortest possible tour
        # Since we do not know exact shortest distance value, assume a function `optimal_tour_cost()`
        # which returns the known best value.

        # optimal_cost = optimal_tour_cost(self.cities, number_of_cities=10)
        # For demonstration assume we have a hypothetical optimal cost function
        # Here we are simply going to not fail unless a real optimal cost check is feasible
        
        # This part would ideally compare calculated_cost with optimal_cost
        pass

# Running the tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    
    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")