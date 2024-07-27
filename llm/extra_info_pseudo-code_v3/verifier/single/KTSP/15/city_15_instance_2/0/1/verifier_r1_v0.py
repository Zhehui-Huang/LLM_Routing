import unittest
from math import sqrt

# Define city coordinates
cities = [
    (54, 87),  # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Tour and cost from the solution provided
solution_tour = [0, 6, 11, 12, 4, 10, 3, 2, 0]
solution_cost = 150.77192228131628

def compute_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += compute_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

class TestRobotTour(unittest.TestCase):

    def test_tour_length(self):
        # Test that exactly 8 cities are visited
        self.assertEqual(len(set(solution_tour)), 9)

    def test_start_end_depot(self):
        # Test that tour starts and ends at depot (city 0)
        self.assertTrue(solution_tour[0] == solution_tour[-1] == 0)

    def test_travel_cost(self):
        # Test the total travel cost
        computed_cost = calculate_total_distance(solution_tour)
        self.assertAlmostEqual(computed_cost, solution_cost, places=5)
        
    def test_output_format(self):
        # Test output format: first and last elements are 0, length is 9 (8 unique cities + return to depot)
        self.assertEqual(solution_torp[0], 0)
        self.assertEqual(solution_torp[-1], 0)
        self.assertEqual(len(solution_torp), 9)

    def test_correct_cities_visited(self):
        # Ensure no extra cities are visited and total cities visited including depot is 8
        self.assertEqual(len(set(solution_torp)), 9)  # including return to depot city

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)