import unittest
import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total cost of a tour using the city coordinates
def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = city_coordinates[tour[i - 1]]
        x2, y2 = city_coordinates[tour[i]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

# Unit tests class for the robot tour problem
class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ]
        self.robot_tour = [0, 4, 3, 1, 2, 5, 7, 6, 9, 12, 15, 18, 20, 17, 14, 16, 19, 21, 13, 11, 8, 10, 0, 0]
        self.expected_cost = 347.78428120330676

    def test_number_of_cities(self):
        # Ensure the cities count matches the problem statement
        self.assertEqual(len(self.city_coordinates), 22)

    def test_tour_starts_ends_depot(self):
        # Tour should start and end at depot 0
        self.assertEqual(self.robot_tour[0], 0)
        self.assertEqual(self.robot_tour[-1], 0)

    def test_unique_visitation(self):
        # Check if each city except depot 0 is visited exactly once
        tour_without_depot = [city for city in self.robot_tour if city != 0]
        self.assertEqual(sorted(tour_without_depot), sorted(set(tour_without_depot)))

    def test_travel_cost(self):
        # Compare computed tour cost to the expected cost
        computed_cost = calculate_tour_cost(self.robot_tour, self.city_coordinates)
        self.assertAlmostEqual(computed_cost, self.expected_cost)

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)