import math
import unittest

# Define the data structure for city coordinates
city_coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Provided solution
tour = [0, 4, 2, 1, 7, 3, 8, 0]
reported_cost = 159.97188184793015

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Test class
class TestSolution(unittest.TestCase):
    def test_tour_validation(self):
        # Check if the tour contains the correct number of unique cities, including the depot city
        self.assertEqual(len(set(tour)), 7 + 1)  # Including depot city, visited twice
        self.assertTrue(all(city in range(10) for city in tour))  # All cities should be within the defined range

        # Check if the tour starts and ends at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check if the tour length is 8, considering return to depot
        self.assertEqual(len(tour), 8)

        # Check the travel cost calculation
        calculated_cost = calculate_tour_cost(tour)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

# Running the test
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")