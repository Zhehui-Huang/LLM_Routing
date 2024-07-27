import math
import unittest

# Provided solution
solution_tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
solution_total_cost = 555.3286513454195
solution_max_distance = 97.04638066409278

# Coordinates of each city including depot at index 0
city_coordinates = [
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

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_cities_count(self):
        self.assertEqual(len(city_coordinates), 10, "There should be 10 cities including the depot.")
    
    def test_path_validity(self):
        visited = set(solution_tour)
        self.assertEqual(len(visited), 10, "All cities must be visited exactly once.")
        self.assertEqual(min(visited), 0, "City indices should start at 0.")
        self.assertEqual(max(visited), 9, "City indices should end at 9.")
        self.assertEqual(solution_tour[0], solution_tour[-1], "The tour should start and end at the depot.")
    
    def test_distance_calculation(self):
        calculated_total_cost = sum(euclidean_distance(city_coordinates[solution_tour[i]], city_coordinates[solution_tour[i+1]]) for i in range(len(solution_tour) - 1))
        self.assertAlmostEqual(calculated_total_cost, solution_total_cost, places=5, msg="Total cost should match the provided solution.")
    
    def test_max_distance(self):
        calculated_max_distance = max(euclidean_distance(city_coordinates[solution_tour[i]], city_coordinates[solution_tour[i+1]]) for i in range(len(solution_tour) - 1))
        self.assertAlmostEqual(calculated_max_distance, solution_max-v_distance, places=5, msg="Maximum distance between consecutive cities should match the provided solution.")
    

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    test_runner = unittest.TextTestRunner()
    
    result = test_runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")