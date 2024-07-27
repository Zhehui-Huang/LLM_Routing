import math
import unittest

# Coordinates for the cities
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = {0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14], 4: [5, 9], 5: [7, 12], 6: [10, 11]}

# Provided tour and cost
provided_tour = [0, 1, 10, 3, 6, 12, 4, 5, 0]
provided_cost = 194.99981419918606

def calculate_euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour_and_cost(tour, cost):
    """Check if the tour is valid and if the calculated cost matches the provided cost."""
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:  # exclude the depot city
        for group_index, group in city_groups.items():
            if city in group:
                visited_groups.append(group_index)
                break
    if sorted(set(visited_groups)) != sorted(city_groups.keys()):
        return False
    
    # Calculate the total cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    # Check if calculated cost is approximately equal to provided cost
    return math.isclose(calculated_cost, cost, rel_tol=1e-5)

class TestTravelingSalesmanTour(unittest.TestCase):
    def test_tour_validity_and_cost(self):
        result = check_tour_and_cost(provided_tour, provided_cost)
        self.assertTrue(result, "The tour is incorrect or the tour cost does not match the expected cost.")
        
# Run unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
    if unittest.TestResult().wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")