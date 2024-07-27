import math
import unittest

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (84, 67),  # Depot city 0
            (74, 40),
            (71, 13),
            (74, 82),
            (97, 28),
            (0, 31),
            (8, 62),
            (74, 56),
            (85, 71),
            (6, 76)
        ]
        self.proposed_tour = [0, 4, 2, 1, 7, 3, 8, 0]
        self.proposed_cost = 159.97188184793015

    def test_tour_validity(self):
        # Check if the tour starts and ends at the depot city
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

        # Check if exactly 7 cities are visited
        self.assertEqual(len(set(self.proposed_tour)), 7)

    def test_tour_cost(self):
        # Calculate the travel cost of the proposed tour
        total_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            city1_idx = self.proposed_tour[i]
            city2_idx = self.proposed_tour[i + 1]
            city1 = self.cities[city1_idx]
            city2 = self.cities[city2_idx]
            total_cost += calculate_distance(city1, city2)
        
        # Check if the calculated total cost matches the proposed cost
        self.assertAlmostEqual(total_cost, self.proposed_cost)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    
    # Check for failures or errors in the test cases
    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")

if __name__ == "__main__":
    main()