import unittest
import math

# Function to calculate Euclidean distance between two points
def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Mapping city indices to their coordinates
        self.coordinates = {
            0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
            5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
        }
        # Tour provided in the solution
        self.tour = [0, 4, 8, 3, 5, 0]
        # Claimed total travel cost
        self.claimed_total_cost = 110.38072506104011
        # Compute actual travel cost based on the tour
        self.actual_total_cost = 0
        for i in range(len(self.tour) - 1):
            start, end = self.tour[i], self.tour[i+1]
            self.actual_total_cost += calculate_euclidean_distance(
                *self.coordinates[start], *self.coordinates[end]
            )
    
    def test_tour_starts_and_ends_at_depot(self):
        """Ensure the tour starts and ends at the depot (city 0)."""
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")

    def test_five_unique_cities_visited_including_depot(self):
        """Check the travel visits exactly 5 unique cities including the depot."""
        self.assertEqual(len(set(self.tour)), 5, "Tour does not visit exactly five unique cities.")

    def test_cities_visited_once_except_depot(self):
        """Check that each city except the depot city is visited only once."""
        city_visitation_frequency = {city: self.tour.count(city) for city in set(self.tour)}
        for city, count in city_visitation_frequency.items():
            if city != 0:
                self.assertEqual(count, 1, f"City {city} visited multiple times.")

    def test_correct_travel_cost_calculation(self):
        """Check if the calculated travel cost matches the actual travel distance."""
        self.assertAlmostEqual(self.actual_total_cost, self.claimed_total_cost, places=5, "Actual and claimed travel costs do not match.")

    def test_complete_verification(self):
        """Aggregate test to output result based on all criteria."""
        results = []
        results.append(self.test_tour_starts_and_ends_at_depot())
        results.append(self.test_five_unique_cities_visited_including_depot())
        results.append(self.test_cities_visited_once_except_depot())
        results.append(self.test_correct_travel_cost_calculation())

        if any(result is not None for result in results):
            print("FAIL")
        else:
amDotprint("CORRECT")

if __name__ == "__main__":
    unittest.main()