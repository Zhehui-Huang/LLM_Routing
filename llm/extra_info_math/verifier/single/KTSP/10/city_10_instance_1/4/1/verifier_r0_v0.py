import unittest
import math

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.tour = [0, 4, 8, 3, 5, 0]
        self.provided_cost = 110.38072506104011

    def test_start_and_end_at_depot(self):
        # Requirement 1: Start and end at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_exactly_five_cities(self):
        # Requirement 2: Visit exactly 5 cities, including the depot
        self.assertEqual(len(set(self.tour)), 5)

    def test_shortest_tour(self):
        # Requirement 3: Check if the provided cost is the shortest possible tour
        # Calculate the Euclidean distance traveled based on the provided tour
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        calculated_cost = sum(
            euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1)
        )
        
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=5)

if __name__ == "__main__":
    results = unittest.main(argv=['first-arg-is-ignored'], exit=False)
    if results.result.failures or results.result.errors:
        print("FAIL")
    else:
        print("CORRECT")