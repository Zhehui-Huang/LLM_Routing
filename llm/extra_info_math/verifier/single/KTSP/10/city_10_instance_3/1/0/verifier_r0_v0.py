import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.solution_tour = [0, 4, 2, 1, 7, 3, 8, 0]
        self.solution_cost = 159.97188184793015

    def euclidean_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_total_distance(self, tour):
        total_distance = 0
        for i in range(len(tour)-1):
            total_distance += self.euclidean_distance(tour[i], tour[i+1])
        return total_distance

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at city 0")
    
    def test_tour_visits_exactly_seven_cities(self):
        # Including depot city and excluding repeated depot end city to match requirement of 7 unique cities
        unique_cities = len(set(self.solution_tour[:-1]))
        self.assertEqual(unique_cities, 7, "Tour should visit exactly 7 cities")
    
    def test_total_travel_cost_minimized(self):
        calculated_cost = self.calculate_total_distance(self.solution_tour)
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=5, msg="Calculated travel cost does not match the provided solution cost")

    def test_solution(self):
        try:
            self.test_tour_starts_and_ends_at_depot()
            self.test_tour_visits_exactly_seven_cities()
            self.test_total_travel_cost_minimized()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Running the test
test = TestRobotTourSolution()
test.setUp()
test.test_solution()