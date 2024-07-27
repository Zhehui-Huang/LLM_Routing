import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Define city coordinates (index corresponds to city number)
        self.cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
                       (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
                       (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
                       (60, 63), (93, 15)]
        # Define city groups
        self.groups = [
            {1, 3, 5, 11, 13, 14, 19},
            {2, 6, 7, 8, 12, 15},
            {4, 9, 10, 16, 17, 18}
        ]

    def test_tour_requirements(self):
        # Hypothetical solution tour and its total travel cost
        tour = [0, 1, 2, 4, 0]  # Replace with the calculated tour
        # Calculate travel cost based on tour
        tour_cost = 0.0
        for i in range(1, len(tour)):
            tour_cost += calculate_distance(self.cities[tour[i]], self.cities[tour[i - 1]])

        # Requirement 1: Check start and end at depot city 0
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")
        
        # Requirement 2: Check one city from each group is visited
        visited_groups = [0] * len(self.groups)
        for city in tour[1:-1]:  # only check cities between start/end
            for group_index, group in enumerate(self.groups):
                if city in group:
                    visited_groups[group_index] += 1

        self.assertTrue(all(count == 1 for count in visited_groups), "One city from each group must be visited exactly once.")
        
        # Announce result based on assertions
        print("CORRECT")

if __name__ == "__main__":
    unittest.main()