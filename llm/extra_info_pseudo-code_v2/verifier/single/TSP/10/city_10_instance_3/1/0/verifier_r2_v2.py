import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

class TestRobotTourVerification(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
            (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
        ]
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.reported_cost = 315.5597914831042

    def test_solution(self):
        # Check that all cities are visited exactly once, excluding the depot
        visit_count = {i: 0 for i in range(len(self.cities))}
        for city in self.tour:
            visit_count[city] += 1
        
        correct_visits = all(count == 1 for idx, count in visit_count.items() if idx != 0)
        correct_visits &= (visit_count[0] == 2)  # Start and end at depot

        # Check start and end at depot
        starts_and_ends_at_depot = self.tour[0] == self.tour[-1] == 0
        
        # Correct calculation of travel cost
        calculated_cost = calculate_total_cost(self.tour, self.cities)
        correct_cost_calculation = math.isclose(self.reported_cost, calculated_cost, rel_tol=1e-5)
        
        if correct_visits and starts_and_ends_at_depot and correct_cost_calculation:
            output = "CORRECT"
        else:
            output = "FAIL"
        
        print(output)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTourVerification("test_solution"))
    runner = unittest.TextTestRunner()
    runner.run(suite)