import unittest
from math import sqrt

# Define positions of the cities
positions = [
    (29, 51),  # city 0 (depot)
    (49, 20),  # city 1
    (79, 69),  # city 2
    (17, 20),  # city 3
    (18, 61),  # city 4
    (40, 57),  # city 5
    (57, 30),  # city 6
    (36, 12),  # city 7
    (93, 43),  # city 8
    (17, 36),  # city 9
    (4, 60),   # city 10
    (78, 82),  # city 11
    (83, 96),  # city 12
    (60, 50),  # city 13
    (98, 1)    # city 14
]

# Define groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Proposed solution
tour = [0, 4, 11, 13, 5, 0]
total_travel_cost = 148.86963273650017

def calculate_euclidean_distance(city1, city2):
    return sqrt((positions[city1][0] - positions[city2][0]) ** 2 + (positions[city1][1] - positions[city2][1]) ** 2)

def calculate_total_cost(tour):
    return sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestRobotTour(unittest.TestCase):
    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(tour[0], 0, "Tour should start at depot city.")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city.")
    
    def test_robot_visits_one_city_from_each_group(self):
        group_visits = set()
        for city in tour[1:-1]:  # Exclude the depot city
            for idx, group in enumerate(groups):
                if city in group:
                    group_visits.add(idx)
                    break
        self.assertEqual(len(group_visits), len(groups), "Robot must visit one city from each group.")
    
    def test_calculates_euclidean_distance(self):
        calculated_cost = calculate_total_cost(tour)
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=5, 
                               msg="Calculated travel cost should match the given total travel cost.")
    
    def test_output_tour_format_and_cost(self):
        self.assertIsInstance(tour, list, "Tour should be a list of city indices.")
        self.assertIsInstance(total_travel_cost, float, "Total travel cost should be a float.")
        self.assertEqual(tour[0], 0, "Output tour must start at city 0.")
        self.assertEqual(tour[-1], 0, "Output tour must end at city 0.")

if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")