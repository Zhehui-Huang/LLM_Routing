import unittest
import math

class TestRobotTour(unittest.TestCase):
    
    def setUp(self):
        # City coordinates
        self.cities = [
            (16, 90),  # Depot city 0
            (43, 99),  # City 1
            (80, 21),  # City 2
            (86, 92),  # City 3
            (54, 93),  # City 4
            (34, 73),  # City 5
            (6, 61),   # City 6
            (86, 69),  # City 7
            (30, 50),  # City 8
            (35, 73),  # City 9
            (42, 64),  # City 10
            (64, 30),  # City 11
            (70, 95),  # City 12
            (29, 64),  # City 13
            (32, 79)   # City 14
        ]

        # City groups
        self.groups = [
            [1, 6, 14],  # Group 0
            [5, 12, 13], # Group 1
            [7, 10],     # Group 2
            [4, 11],     # Group 3
            [2, 8],      # Group 4
            [3, 9]       # Group 5
        ]
        
        # Robot's tour and tour cost (provided solution)
        self.tour = [0, 14, 5, 10, 11, 8, 9, 0]
        self.provided_cost = 166.75801920718544

    def test_coordinates(self):
        # Ensure the depot and other cities' coordinates are unchanged
        self.assertEqual(self.cities[0], (16, 90))
        self.assertEqual(len(self.cities), 15)

    def test_groups(self):
        # Check that all city groups are mentioned and the numbers are correct
        self.assertEqual(len(self.groups), 6)
        unique_cities = set([c for g in self.groups for c in g])
        self.assertTrue(all(city in unique_cities for city in range(1, 15)))

    def test_tour_start_and_end_at_depot(self):
        # Tour should start and end at the depot (city index 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_one_city_per_group(self):
        # Gathering visited cities from the tour
        visited = set(self.tour[1:-1])  # exclude the depot at start and end

        # Check if exactly one city from each group was visited
        for group in self.groups:
            self.assertTrue(len(visited.intersection(group)) == 1)

    def test_tour_calculates_correct_travel_cost(self):
        # Calculate the Euclidean distance for the provided tour
        def euclidean(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        total_cost = sum(euclidean(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        
        # Check if the travel cost is approximately equal to the provided cost
        self.assertAlmostEqual(total_cost, self.provided_cost, places=5)

unittest.main(argv=[''], verbosity=2, exit=False)