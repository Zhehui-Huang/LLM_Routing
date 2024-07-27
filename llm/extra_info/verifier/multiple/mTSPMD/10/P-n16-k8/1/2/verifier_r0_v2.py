import unittest
import math

def calculate_distance(city1, city2):
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestRobotTours(unittest.TestCase):
    def test_robot_tours(self):
        tours = [
            [0, 0],
            [1, 10, 1],
            [2, 13, 2],
            [3, 8, 12, 3],
            [4, 11, 15, 4],
            [5, 14, 5],
            [6, 6],
            [7, 9, 7]
        ]
        
        expected_total_cost = 129.7441421535715

        all_visited_cities = set()
        calculated_total_cost = 0

        for tour in tours:
            self.assertEqual(tour[0], tour[-1], "Robot does not start and end at the same depot")

            cities_in_tour = len(tour) - 1
            last_city = tour[0]

            for i in range(1, cities_in_tour + 1):
                city = tour[i]
                all_visited_cities.add(city)
                calculated_total_cost += calculate_distance(last_city, city)
                last_city = city

            # Add the distance back to the start depot
            calculated_total_cost += calculate_distance(tour[-1], tour[0])

        self.assertEqual(len(all_visited_cities), 15, "Not all unique cities visited")
        self.assertAlmostEqual(calculated_total_cost, expected_total_size, places=5, "Total travel cost is incorrect")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTours('test_robot_tours'))
    
    runner = unittest.TextTestRunner()
    
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()