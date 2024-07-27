import unittest
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11),
            13: (61, 25),
            12: (20, 97),
            16: (13, 43)
        }
        self.tour = [0, 13, 12, 16, 0]
        self.reported_cost = 224.51
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

    def test_tour_length(self):
        # Including the depot city at the start and the end, the tour should visit exactly 4 cities
        self.assertEqual(len(set(self.tour)), 4, "Tour does not visit exactly 4 cities.")

    def test_travel_cost(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            total_distance += euclidean_distance(x1, y1, x2, y2)
        # Compare the computed total distance with reported cost
        self.assertAlmostEqual(total_distance, self.reported_cost, places=2, msg="Reported travel cost is incorrect.")

# Running the tests and capturing the results
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")