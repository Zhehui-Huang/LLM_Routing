import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 6, 9, 19, 10, 4, 0]
        self.positions = [(14, 77), (34, 20), (19, 38), (14, 91),
                          (68, 98), (45, 84), (4, 56), (54, 82), 
                          (37, 28), (27, 45), (90, 85), (98, 76),
                          (6, 19), (26, 29), (21, 79), (49, 23),
                          (78, 76), (68, 45), (50, 28), (69, 9)]
        self.expected_cost = 266.41

    def test_start_end_at_depot(self):
        # Checking if the tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_tour_length(self):
        # Confirming that the right number of unique cities are visited, including the depot
        self.assertEqual(len(self.tour), 7)

    def test_tour_format(self):
        # Ensuring the tour is a list and contains only integers
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

    def test_correct_total_travel_cost(self):
        # Calculating the travel cost of the specified tour and comparing with provided value
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            x1, y1 = self.positions[self.tour[i - 1]]
            x2, y2 = self.positions[self.tour[i]]
            calculated_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        calculated_cost = round(calculated_cost, 2)
        self.assertEqual(calculated_cost, self.expected_cost)

if __name__ == "__main__":
    unittest.main()