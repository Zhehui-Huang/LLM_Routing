import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Coordinates and demands of each city including depot (index 0)
        self.cities = {
            0: (30, 40, 0),
            18: (62, 63, 17),
            19: (63, 69, 6)
        }
        
        # Tours and their reported total costs
        self.tours = [
            ([0, 18, 19, 0], 89.42),
            ([0, 19, 18, 0], 89.42)
        ]
        
        # Robot capacity
        self.capacity = 160
    
    def test_tours_start_and_end_at_depot(self):
        for tour, _ in self.tours:
            self.assertEqual(tour[0], 0, "Tour should start at the depot")
            self.assertEqual(tour[-1], 0, "Tour should end at the depot")
    
    def test_capacity_not_exceeded(self):
        for tour, _ in self.tours:
            load = sum(self.cities[city][2] for city in tour if city != 0)
            self.assertLessEqual(load, self.capacity, "Robot capacity exceeded")

    def test_demand_met_exactly(self):
        total_demand = {city: 0 for city in self.cities}
        for tour, _ in self.tours:
            for city in tour:
                if city != 0:
                    total_demand[city] += self.cities[city][2]
        for city, (_, _, demand) in self.cities.items():
            self.assertEqual(total_demand[city], demand, "Demand not met exactly for city {}".format(city))

    def test_correct_travel_cost(self):
        def distance(city1, city2):
            x1, y1, _ = self.cities[city1]
            x2, y2, _ = self.cities[city2]
            return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        for tour, reported_cost in self.tours:
            calculated_cost = 0
            for i in range(len(tour) - 1):
                calculated_cost += distance(tour[i], tour[i + 1])
            self.assertAlmostEqual(calculated_cost, reported_cost, places=2, msg="Reported travel cost does not match calculated travel cost")

    def test_minimize_total_travel_cost(self):
        actual_total_cost = sum(cost for _, cost in self.tours)
        expected_total_cost = 178.85  # Adjusted correct variable naming and syntax
        self.assertAlmostEqual(actual_total_cost, expected_total_cost, places=2, msg="Total travel cost is not minimal")

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTours))
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)  # Correct syntax to execute tests

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()