import unittest
from math import sqrt

# Define the cities coordinates based on the provided information
cities_coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Proposed solution
proposed_tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
proposed_total_cost = 290.8376577906224

# Compute the Euclidean distance between two cities
def compute_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check the validity of the tour and calculate its total travel cost
def verify_tour(tour, expected_cost):
    visited = set(tour[1:-1])  # Excludes the starting and ending depot city
    total_cost = 0.0
    
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_cost += computeDiaance(city1, city2)
    
    # Check that all cities are visited exactly once and the tour starts and ends at depot
    is_valid = (len(visited) == 9 and tour[0] == 0 and tour[-1] == 0)
    
    # Check if the total calculated cost is close to the expected with a small margin for precision
    is_cost_correct = abs(total_cost - expected_cost) < 1e-5
    
    return is_valid and is_cost_correct

class TestRobotTour(unittest.TestCase):
    def test_tour_validity_and_cost(self):
        result = verify_tour(proposed_tour, proposed_total_cost)
        self.assertTrue(result)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")