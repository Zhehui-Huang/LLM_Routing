import unittest

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # The given tours as per output
        self.tours = [
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        ]
    
    def test_salesmen_departure(self):
        for tour in self.tours:
            departs = sum(1 for i in tour if (i == 0 and tour.index(i) == 0))
            self.assertEqual(departs, 1, f"Failed: Each salesman should leave the depot once. Found {departs}")
    
    def test_salesmen_return(self):
        for tour in self.tours:
            returns = sum(1 for i in tour if (i == 1 and tour.index(i) == len(tour) - 1))
            self.assertEqual(returns, 0, f"Failed: No salesman should return to the depot. Found {returns}")

    def test_customer_visit_once(self):
        all_visits = []
        for tour in self.tours:
            all_visits.extend(tour[1:-1])
        for city in set(all_visits):
            self.assertEqual(all_visits.count(city), 1, f"Failed: Each customer city should be visited exactly once. City {city} visited {all_visits.count(city)} times.")

    def test_prohibit_single_customer_service(self):
        for tour in self.tours:
            for city in set(tour[1:-1]):
                visits = tour.count(city)
                self.assertTrue(visits > 1, f"City {city} is served only once by a salesman.")

    def test_subtour_elimination(self):
        # Check all subtours are eliminated, i.e., no cycles except the entire tour
        for tour in self.tours:
            self.assertEqual(len(set(tour)), len(tour)//2 + 1, f"Subtour detected in the tour {tour}")

    def test_binary_constraints(self):
        # Checking if all values are either 0 or 1
        for tour in self.tours:
            for node in tour:
                self.assertIn(node, [0, 1], "Tours should only have binary values 0 or 1.")

    def test_correct_solution(self):
        for tour in self.tours:
            if tour.count(0) != 8 or tour.count(1) != 8:
                return "FAIL"
        return "CORRECT"

# Create Test Suite
suite = unittest.TestSuite()
suite.addTest(TestRobotTours('test_salesmen_departure'))
suite.addTest(TestRobotTours('test_salesmen_return'))
suite.addTest(TestRobotTours('test_customer_visit_once'))
suite.addTest(TestRobotTours('test_prohibit_single_customer_service'))
suite.addTest(TestRobotTours('test_subtour_elimination'))
suite.addTest(TestRobotTours('test_binary_constraints'))
result = unittest.TextTestRunner().run(suite)

# Outputting result
msg = "CORRECT" if all(result.wasSuccessful() for result in result.failures) else "FAIL"
print(msg)